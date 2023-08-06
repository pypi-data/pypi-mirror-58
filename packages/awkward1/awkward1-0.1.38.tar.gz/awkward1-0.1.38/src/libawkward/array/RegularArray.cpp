// BSD 3-Clause License; see https://github.com/jpivarski/awkward-1.0/blob/master/LICENSE

#include <iomanip>
#include <sstream>
#include <stdexcept>

#include "awkward/cpu-kernels/identity.h"
#include "awkward/cpu-kernels/getitem.h"
#include "awkward/type/RegularType.h"
#include "awkward/type/ArrayType.h"
#include "awkward/type/UnknownType.h"

#include "awkward/array/RegularArray.h"

namespace awkward {
  RegularArray::RegularArray(const std::shared_ptr<Identity>& id, const std::shared_ptr<Type>& type, const std::shared_ptr<Content>& content, int64_t size)
      : Content(id, type)
      , content_(content)
      , size_(size) {
    if (type_.get() != nullptr) {
      checktype();
    }
  }

  const std::shared_ptr<Content> RegularArray::content() const {
    return content_;
  }

  int64_t RegularArray::size() const {
    return size_;
  }

  const std::string RegularArray::classname() const {
    return "RegularArray";
  }

  void RegularArray::setid(const std::shared_ptr<Identity>& id) {
    if (id.get() == nullptr) {
      content_.get()->setid(id);
    }
    else {
      if (length() != id.get()->length()) {
        util::handle_error(failure("content and its id must have the same length", kSliceNone, kSliceNone), classname(), id_.get());
      }
      std::shared_ptr<Identity> bigid = id;
      if (content_.get()->length() > kMaxInt32) {
        bigid = id.get()->to64();
      }
      if (Identity32* rawid = dynamic_cast<Identity32*>(bigid.get())) {
        std::shared_ptr<Identity> subid = std::make_shared<Identity32>(Identity::newref(), rawid->fieldloc(), rawid->width() + 1, content_.get()->length());
        Identity32* rawsubid = reinterpret_cast<Identity32*>(subid.get());
        struct Error err = awkward_identity32_from_regulararray(
          rawsubid->ptr().get(),
          rawid->ptr().get(),
          rawid->offset(),
          size_,
          content_.get()->length(),
          length(),
          rawid->width());
        util::handle_error(err, classname(), id_.get());
        content_.get()->setid(subid);
      }
      else if (Identity64* rawid = dynamic_cast<Identity64*>(bigid.get())) {
        std::shared_ptr<Identity> subid = std::make_shared<Identity64>(Identity::newref(), rawid->fieldloc(), rawid->width() + 1, content_.get()->length());
        Identity64* rawsubid = reinterpret_cast<Identity64*>(subid.get());
        struct Error err = awkward_identity64_from_regulararray(
          rawsubid->ptr().get(),
          rawid->ptr().get(),
          rawid->offset(),
          size_,
          content_.get()->length(),
          length(),
          rawid->width());
        util::handle_error(err, classname(), id_.get());
        content_.get()->setid(subid);
      }
      else {
        throw std::runtime_error("unrecognized Identity specialization");
      }
    }
    id_ = id;
  }

  void RegularArray::setid() {
    if (length() < kMaxInt32) {
      std::shared_ptr<Identity> newid = std::make_shared<Identity32>(Identity::newref(), Identity::FieldLoc(), 1, length());
      Identity32* rawid = reinterpret_cast<Identity32*>(newid.get());
      struct Error err = awkward_new_identity32(rawid->ptr().get(), length());
      util::handle_error(err, classname(), id_.get());
      setid(newid);
    }
    else {
      std::shared_ptr<Identity> newid = std::make_shared<Identity64>(Identity::newref(), Identity::FieldLoc(), 1, length());
      Identity64* rawid = reinterpret_cast<Identity64*>(newid.get());
      struct Error err = awkward_new_identity64(rawid->ptr().get(), length());
      util::handle_error(err, classname(), id_.get());
      setid(newid);
    }
  }

  const std::shared_ptr<Type> RegularArray::type() const {
    if (type_.get() != nullptr) {
      return type_;
    }
    else {
      return std::make_shared<RegularType>(Type::Parameters(), content_.get()->type(), size_);
    }
  }

  const std::shared_ptr<Content> RegularArray::astype(const std::shared_ptr<Type>& type) const {
    std::shared_ptr<Type> inner = type;
    if (inner.get() != nullptr) {
      if (RegularType* raw = dynamic_cast<RegularType*>(inner.get())) {
        inner = raw->type();
      }
    }
    return std::make_shared<RegularArray>(id_, type, content_.get()->astype(inner), size_);
  }

  const std::string RegularArray::tostring_part(const std::string& indent, const std::string& pre, const std::string& post) const {
    std::stringstream out;
    out << indent << pre << "<" << classname() << " size=\"" << size_ << "\">\n";
    if (id_.get() != nullptr) {
      out << id_.get()->tostring_part(indent + std::string("    "), "", "\n");
    }
    if (type_.get() != nullptr) {
      out << indent << "    <type>" + type().get()->tostring() + "</type>\n";
    }
    out << content_.get()->tostring_part(indent + std::string("    "), "<content>", "</content>\n");
    out << indent << "</" << classname() << ">" << post;
    return out.str();
  }

  void RegularArray::tojson_part(ToJson& builder) const {
    int64_t len = length();
    builder.beginlist();
    for (int64_t i = 0;  i < len;  i++) {
      getitem_at_nowrap(i).get()->tojson_part(builder);
    }
    builder.endlist();
  }

  int64_t RegularArray::length() const {
    return size_ == 0 ? 0 : content_.get()->length() / size_;   // floor of length / size
  }

  const std::shared_ptr<Content> RegularArray::shallow_copy() const {
    return std::make_shared<RegularArray>(id_, type_, content_, size_);
  }

  void RegularArray::check_for_iteration() const {
    if (id_.get() != nullptr  && id_.get()->length() < length()) {
      util::handle_error(failure("len(id) < len(array)", kSliceNone, kSliceNone), id_.get()->classname(), nullptr);
    }
  }

  const std::shared_ptr<Content> RegularArray::getitem_nothing() const {
    return content_.get()->getitem_range_nowrap(0, 0);
  }

  const std::shared_ptr<Content> RegularArray::getitem_at(int64_t at) const {
    int64_t regular_at = at;
    int64_t len = length();
    if (regular_at < 0) {
      regular_at += len;
    }
    if (!(0 <= regular_at  &&  regular_at < len)) {
      util::handle_error(failure("index out of range", kSliceNone, at), classname(), id_.get());
    }
    return getitem_at_nowrap(regular_at);
  }

  const std::shared_ptr<Content> RegularArray::getitem_at_nowrap(int64_t at) const {
    return content_.get()->getitem_range_nowrap(at*size_, (at + 1)*size_);
  }

  const std::shared_ptr<Content> RegularArray::getitem_range(int64_t start, int64_t stop) const {
    int64_t regular_start = start;
    int64_t regular_stop = stop;
    awkward_regularize_rangeslice(&regular_start, &regular_stop, true, start != Slice::none(), stop != Slice::none(), length());
    if (id_.get() != nullptr  &&  regular_stop > id_.get()->length()) {
      util::handle_error(failure("index out of range", kSliceNone, stop), id_.get()->classname(), nullptr);
    }
    return getitem_range_nowrap(regular_start, regular_stop);
  }

  const std::shared_ptr<Content> RegularArray::getitem_range_nowrap(int64_t start, int64_t stop) const {
    std::shared_ptr<Identity> id(nullptr);
    if (id_.get() != nullptr) {
      id = id_.get()->getitem_range_nowrap(start, stop);
    }
    return std::make_shared<RegularArray>(id_, type_, content_.get()->getitem_range_nowrap(start*size_, stop*size_), size_);
  }

  const std::shared_ptr<Content> RegularArray::getitem_field(const std::string& key) const {
    return std::make_shared<RegularArray>(id_, Type::none(), content_.get()->getitem_field(key), size_);
  }

  const std::shared_ptr<Content> RegularArray::getitem_fields(const std::vector<std::string>& keys) const {
    std::shared_ptr<Type> type = Type::none();
    if (SliceFields(keys).preserves_type(type_, Index64(0))) {
      type = type_;
    }
    return std::make_shared<RegularArray>(id_, type, content_.get()->getitem_fields(keys), size_);
  }

  const std::shared_ptr<Content> RegularArray::carry(const Index64& carry) const {
    Index64 nextcarry(carry.length()*size_);

    struct Error err = awkward_regulararray_getitem_carry_64(
      nextcarry.ptr().get(),
      carry.ptr().get(),
      carry.length(),
      size_);
    util::handle_error(err, classname(), id_.get());

    std::shared_ptr<Identity> id(nullptr);
    if (id_.get() != nullptr) {
      id = id_.get()->getitem_carry_64(carry);
    }
    return std::make_shared<RegularArray>(id, type_, content_.get()->carry(nextcarry), size_);
  }

  const std::pair<int64_t, int64_t> RegularArray::minmax_depth() const {
    std::pair<int64_t, int64_t> content_depth = content_.get()->minmax_depth();
    return std::pair<int64_t, int64_t>(content_depth.first + 1, content_depth.second + 1);
  }

  int64_t RegularArray::numfields() const {
    return content_.get()->numfields();
  }

  int64_t RegularArray::fieldindex(const std::string& key) const {
    return content_.get()->fieldindex(key);
  }

  const std::string RegularArray::key(int64_t fieldindex) const {
    return content_.get()->key(fieldindex);
  }

  bool RegularArray::haskey(const std::string& key) const {
    return content_.get()->haskey(key);
  }

  const std::vector<std::string> RegularArray::keys() const {
    return content_.get()->keys();
  }

  void RegularArray::checktype() const {
    bool okay = false;
    if (RegularType* raw = dynamic_cast<RegularType*>(type_.get())) {
      okay = (raw->type().get() == content_.get()->type().get()  &&  raw->size() == size_);
    }
    if (!okay) {
        throw std::invalid_argument(std::string("cannot assign type ") + type_.get()->tostring() + std::string(" to ") + classname());
    }
  }

  const std::shared_ptr<Content> RegularArray::getitem_next(const SliceAt& at, const Slice& tail, const Index64& advanced) const {
    assert(advanced.length() == 0);

    int64_t len = length();
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    Index64 nextcarry(len);

    struct Error err = awkward_regulararray_getitem_next_at_64(
      nextcarry.ptr().get(),
      at.at(),
      len,
      size_);
    util::handle_error(err, classname(), id_.get());

    std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);
    return nextcontent.get()->getitem_next(nexthead, nexttail, advanced);
  }

  const std::shared_ptr<Content> RegularArray::getitem_next(const SliceRange& range, const Slice& tail, const Index64& advanced) const {
    int64_t len = length();
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();

    assert(range.step() != 0);
    int64_t regular_start = range.start();
    int64_t regular_stop = range.stop();
    int64_t regular_step = std::abs(range.step());
    awkward_regularize_rangeslice(&regular_start, &regular_stop, range.step() > 0, range.start() != Slice::none(), range.stop() != Slice::none(), size_);
    int64_t nextsize = 0;
    if (range.step() > 0  &&  regular_stop - regular_start > 0) {
      int64_t diff = regular_stop - regular_start;
      nextsize = diff / regular_step;
      if (diff % regular_step != 0) {
        nextsize++;
      }
    }
    else if (range.step() < 0  &&  regular_stop - regular_start < 0) {
      int64_t diff = regular_start - regular_stop;
      nextsize = diff / regular_step;
      if (diff % regular_step != 0) {
        nextsize++;
      }
    }

    Index64 nextcarry(len*nextsize);

    struct Error err = awkward_regulararray_getitem_next_range_64(
      nextcarry.ptr().get(),
      regular_start,
      range.step(),
      len,
      size_,
      nextsize);
    util::handle_error(err, classname(), id_.get());

    std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);

    std::shared_ptr<Type> outtype = Type::none();
    if (type_.get() != nullptr) {
      RegularType* raw = dynamic_cast<RegularType*>(type_.get());
      outtype = std::make_shared<RegularType>(Type::Parameters(), raw->type(), nextsize);
    }

    if (advanced.length() == 0) {
      return std::make_shared<RegularArray>(id_, outtype, nextcontent.get()->getitem_next(nexthead, nexttail, advanced), nextsize);
    }
    else {
      Index64 nextadvanced(len*nextsize);

      struct Error err = awkward_regulararray_getitem_next_range_spreadadvanced_64(
        nextadvanced.ptr().get(),
        advanced.ptr().get(),
        len,
        nextsize);
      util::handle_error(err, classname(), id_.get());

      return std::make_shared<RegularArray>(id_, outtype, nextcontent.get()->getitem_next(nexthead, nexttail, nextadvanced), nextsize);
    }
  }

  const std::shared_ptr<Content> RegularArray::getitem_next(const SliceArray64& array, const Slice& tail, const Index64& advanced) const {
    int64_t len = length();
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    Index64 flathead = array.ravel();
    Index64 regular_flathead(flathead.length());

    struct Error err = awkward_regulararray_getitem_next_array_regularize_64(
      regular_flathead.ptr().get(),
      flathead.ptr().get(),
      flathead.length(),
      size_);
    util::handle_error(err, classname(), id_.get());

    if (advanced.length() == 0) {
      Index64 nextcarry(len*flathead.length());
      Index64 nextadvanced(len*flathead.length());

      struct Error err = awkward_regulararray_getitem_next_array_64(
        nextcarry.ptr().get(),
        nextadvanced.ptr().get(),
        regular_flathead.ptr().get(),
        len,
        regular_flathead.length(),
        size_);
      util::handle_error(err, classname(), id_.get());

      std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);

      return getitem_next_array_wrap(nextcontent.get()->getitem_next(nexthead, nexttail, nextadvanced), array.shape());
    }
    else {
      Index64 nextcarry(len);
      Index64 nextadvanced(len);

      struct Error err = awkward_regulararray_getitem_next_array_advanced_64(
        nextcarry.ptr().get(),
        nextadvanced.ptr().get(),
        advanced.ptr().get(),
        regular_flathead.ptr().get(),
        len,
        regular_flathead.length(),
        size_);
      util::handle_error(err, classname(), id_.get());

      std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);
      return nextcontent.get()->getitem_next(nexthead, nexttail, nextadvanced);
    }
  }

}
