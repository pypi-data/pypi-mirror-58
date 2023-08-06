// BSD 3-Clause License; see https://github.com/jpivarski/awkward-1.0/blob/master/LICENSE

#include <sstream>
#include <type_traits>

#include "awkward/cpu-kernels/identity.h"
#include "awkward/cpu-kernels/getitem.h"
#include "awkward/type/ListType.h"
#include "awkward/type/ArrayType.h"
#include "awkward/type/UnknownType.h"
#include "awkward/Slice.h"
#include "awkward/array/ListArray.h"
#include "awkward/array/RegularArray.h"

#include "awkward/array/ListOffsetArray.h"

namespace awkward {
  template <typename T>
  ListOffsetArrayOf<T>::ListOffsetArrayOf(const std::shared_ptr<Identity>& id, const std::shared_ptr<Type>& type, const IndexOf<T>& offsets, const std::shared_ptr<Content>& content)
      : Content(id, type)
      , offsets_(offsets)
      , content_(content) {
    if (type_.get() != nullptr) {
      checktype();
    }
  }

  template <typename T>
  const IndexOf<T> ListOffsetArrayOf<T>::offsets() const {
    return offsets_;
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::content() const {
    return content_;
  }

  template <typename T>
  const std::string ListOffsetArrayOf<T>::classname() const {
    if (std::is_same<T, int32_t>::value) {
      return "ListOffsetArray32";
    }
    else if (std::is_same<T, uint32_t>::value) {
      return "ListOffsetArrayU32";
    }
    else if (std::is_same<T, int64_t>::value) {
      return "ListOffsetArray64";
    }
    else {
      return "UnrecognizedListOffsetArray";
    }
  }

  template <typename T>
  IndexOf<T> make_starts(const IndexOf<T>& offsets) {
    return IndexOf<T>(offsets.ptr(), offsets.offset(), offsets.length() - 1);
  }

  template <typename T>
  IndexOf<T> make_stops(const IndexOf<T>& offsets) {
    return IndexOf<T>(offsets.ptr(), offsets.offset() + 1, offsets.length() - 1);
  }

  template <>
  void ListOffsetArrayOf<int32_t>::setid(const std::shared_ptr<Identity>& id) {
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
        struct Error err = awkward_identity32_from_listoffsetarray32(
          rawsubid->ptr().get(),
          rawid->ptr().get(),
          offsets_.ptr().get(),
          rawid->offset(),
          offsets_.offset(),
          content_.get()->length(),
          length(),
          rawid->width());
        util::handle_error(err, classname(), id_.get());
        content_.get()->setid(subid);
      }
      else if (Identity64* rawid = dynamic_cast<Identity64*>(bigid.get())) {
        std::shared_ptr<Identity> subid = std::make_shared<Identity64>(Identity::newref(), rawid->fieldloc(), rawid->width() + 1, content_.get()->length());
        Identity64* rawsubid = reinterpret_cast<Identity64*>(subid.get());
        struct Error err = awkward_identity64_from_listoffsetarray32(
          rawsubid->ptr().get(),
          rawid->ptr().get(),
          offsets_.ptr().get(),
          rawid->offset(),
          offsets_.offset(),
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

  template <typename T>
  void ListOffsetArrayOf<T>::setid(const std::shared_ptr<Identity>& id) {
    if (id.get() == nullptr) {
      content_.get()->setid(id);
    }
    else {
      if (length() != id.get()->length()) {
        util::handle_error(failure("content and its id must have the same length", kSliceNone, kSliceNone), classname(), id_.get());
      }
      std::shared_ptr<Identity> bigid = id.get()->to64();
      if (Identity64* rawid = dynamic_cast<Identity64*>(bigid.get())) {
        std::shared_ptr<Identity> subid = std::make_shared<Identity64>(Identity::newref(), rawid->fieldloc(), rawid->width() + 1, content_.get()->length());
        Identity64* rawsubid = reinterpret_cast<Identity64*>(subid.get());
        struct Error err = util::awkward_identity64_from_listoffsetarray<T>(
          rawsubid->ptr().get(),
          rawid->ptr().get(),
          offsets_.ptr().get(),
          rawid->offset(),
          offsets_.offset(),
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

  template <typename T>
  void ListOffsetArrayOf<T>::setid() {
    if (length() <= kMaxInt32) {
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

  template <typename T>
  const std::shared_ptr<Type> ListOffsetArrayOf<T>::type() const {
    if (type_.get() != nullptr) {
      return type_;
    }
    else {
      return std::make_shared<ListType>(Type::Parameters(), content_.get()->type());
    }
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::astype(const std::shared_ptr<Type>& type) const {
    std::shared_ptr<Type> inner = type;
    if (inner.get() != nullptr) {
      if (ListType* raw = dynamic_cast<ListType*>(inner.get())) {
        inner = raw->type();
      }
    }
    return std::make_shared<ListOffsetArrayOf<T>>(id_, type, offsets_, content_.get()->astype(inner));
  }

  template <typename T>
  const std::string ListOffsetArrayOf<T>::tostring_part(const std::string& indent, const std::string& pre, const std::string& post) const {
    std::stringstream out;
    out << indent << pre << "<" << classname() << ">\n";
    if (id_.get() != nullptr) {
      out << id_.get()->tostring_part(indent + std::string("    "), "", "\n");
    }
    if (type_.get() != nullptr) {
      out << indent << "    <type>" + type().get()->tostring() + "</type>\n";
    }
    out << offsets_.tostring_part(indent + std::string("    "), "<offsets>", "</offsets>\n");
    out << content_.get()->tostring_part(indent + std::string("    "), "<content>", "</content>\n");
    out << indent << "</" << classname() << ">" << post;
    return out.str();
  }

  template <typename T>
  void ListOffsetArrayOf<T>::tojson_part(ToJson& builder) const {
    int64_t len = length();
    builder.beginlist();
    for (int64_t i = 0;  i < len;  i++) {
      getitem_at_nowrap(i).get()->tojson_part(builder);
    }
    builder.endlist();
  }

  template <typename T>
  int64_t ListOffsetArrayOf<T>::length() const {
    return offsets_.length() - 1;
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::shallow_copy() const {
    return std::make_shared<ListOffsetArrayOf<T>>(id_, type_, offsets_, content_);
  }

  template <typename T>
  void ListOffsetArrayOf<T>::check_for_iteration() const {
    if (id_.get() != nullptr  &&  id_.get()->length() < offsets_.length() - 1) {
      util::handle_error(failure("len(id) < len(array)", kSliceNone, kSliceNone), id_.get()->classname(), nullptr);
    }
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_nothing() const {
    return content_.get()->getitem_range_nowrap(0, 0);
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_at(int64_t at) const {
    int64_t regular_at = at;
    if (regular_at < 0) {
      regular_at += offsets_.length() - 1;
    }
    if (!(0 <= regular_at  &&  regular_at < offsets_.length() - 1)) {
      util::handle_error(failure("index out of range", kSliceNone, at), classname(), id_.get());
    }
    return getitem_at_nowrap(regular_at);
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_at_nowrap(int64_t at) const {
    int64_t start = (int64_t)offsets_.getitem_at_nowrap(at);
    int64_t stop = (int64_t)offsets_.getitem_at_nowrap(at + 1);
    int64_t lencontent = content_.get()->length();
    if (start == stop) {
      start = stop = 0;
    }
    if (start < 0) {
      util::handle_error(failure("offsets[i] < 0", kSliceNone, at), classname(), id_.get());
    }
    if (start > stop) {
      util::handle_error(failure("offsets[i] > offsets[i + 1]", kSliceNone, at), classname(), id_.get());
    }
    if (stop > lencontent) {
      util::handle_error(failure("offsets[i] != offsets[i + 1] and offsets[i + 1] > len(content)", kSliceNone, at), classname(), id_.get());
    }
    return content_.get()->getitem_range_nowrap(start, stop);
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_range(int64_t start, int64_t stop) const {
    int64_t regular_start = start;
    int64_t regular_stop = stop;
    awkward_regularize_rangeslice(&regular_start, &regular_stop, true, start != Slice::none(), stop != Slice::none(), offsets_.length() - 1);
    if (id_.get() != nullptr  &&  regular_stop > id_.get()->length()) {
      util::handle_error(failure("index out of range", kSliceNone, stop), id_.get()->classname(), nullptr);
    }
    return getitem_range_nowrap(regular_start, regular_stop);
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_range_nowrap(int64_t start, int64_t stop) const {
    std::shared_ptr<Identity> id(nullptr);
    if (id_.get() != nullptr) {
      id = id_.get()->getitem_range_nowrap(start, stop);
    }
    return std::make_shared<ListOffsetArrayOf<T>>(id, type_, offsets_.getitem_range_nowrap(start, stop + 1), content_);
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_field(const std::string& key) const {
    return std::make_shared<ListOffsetArrayOf<T>>(id_, Type::none(), offsets_, content_.get()->getitem_field(key));
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_fields(const std::vector<std::string>& keys) const {
    std::shared_ptr<Type> type = Type::none();
    if (SliceFields(keys).preserves_type(type_, Index64(0))) {
      type = type_;
    }
    return std::make_shared<ListOffsetArrayOf<T>>(id_, type, offsets_, content_.get()->getitem_fields(keys));
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::carry(const Index64& carry) const {
    IndexOf<T> starts = make_starts(offsets_);
    IndexOf<T> stops = make_stops(offsets_);
    IndexOf<T> nextstarts(carry.length());
    IndexOf<T> nextstops(carry.length());
    struct Error err = util::awkward_listarray_getitem_carry_64<T>(
      nextstarts.ptr().get(),
      nextstops.ptr().get(),
      starts.ptr().get(),
      stops.ptr().get(),
      carry.ptr().get(),
      starts.offset(),
      stops.offset(),
      offsets_.length() - 1,
      carry.length());
    util::handle_error(err, classname(), id_.get());
    std::shared_ptr<Identity> id(nullptr);
    if (id_.get() != nullptr) {
      id = id_.get()->getitem_carry_64(carry);
    }
    return std::make_shared<ListArrayOf<T>>(id, type_, nextstarts, nextstops, content_);
  }

  template <typename T>
  const std::pair<int64_t, int64_t> ListOffsetArrayOf<T>::minmax_depth() const {
    std::pair<int64_t, int64_t> content_depth = content_.get()->minmax_depth();
    return std::pair<int64_t, int64_t>(content_depth.first + 1, content_depth.second + 1);
  }

  template <typename T>
  int64_t ListOffsetArrayOf<T>::numfields() const {
    return content_.get()->numfields();
  }

  template <typename T>
  int64_t ListOffsetArrayOf<T>::fieldindex(const std::string& key) const {
    return content_.get()->fieldindex(key);
  }

  template <typename T>
  const std::string ListOffsetArrayOf<T>::key(int64_t fieldindex) const {
    return content_.get()->key(fieldindex);
  }

  template <typename T>
  bool ListOffsetArrayOf<T>::haskey(const std::string& key) const {
    return content_.get()->haskey(key);
  }

  template <typename T>
  const std::vector<std::string> ListOffsetArrayOf<T>::keys() const {
    return content_.get()->keys();
  }

  template <typename T>
  void ListOffsetArrayOf<T>::checktype() const {
    bool okay = false;
    if (ListType* raw = dynamic_cast<ListType*>(type_.get())) {
      okay = (raw->type().get() == content_.get()->type().get());
    }
    if (!okay) {
        throw std::invalid_argument(std::string("cannot assign type ") + type_.get()->tostring() + std::string(" to ") + classname());
    }
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_next(const SliceAt& at, const Slice& tail, const Index64& advanced) const {
    assert(advanced.length() == 0);
    int64_t lenstarts = offsets_.length() - 1;
    IndexOf<T> starts = make_starts(offsets_);
    IndexOf<T> stops = make_stops(offsets_);
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    Index64 nextcarry(lenstarts);
    struct Error err = util::awkward_listarray_getitem_next_at_64<T>(
      nextcarry.ptr().get(),
      starts.ptr().get(),
      stops.ptr().get(),
      lenstarts,
      starts.offset(),
      stops.offset(),
      at.at());
    util::handle_error(err, classname(), id_.get());
    std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);
    return nextcontent.get()->getitem_next(nexthead, nexttail, advanced);
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_next(const SliceRange& range, const Slice& tail, const Index64& advanced) const {
    int64_t lenstarts = offsets_.length() - 1;
    IndexOf<T> starts = make_starts(offsets_);
    IndexOf<T> stops = make_stops(offsets_);
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    int64_t start = range.start();
    int64_t stop = range.stop();
    int64_t step = range.step();
    if (step == Slice::none()) {
      step = 1;
    }
    int64_t carrylength;
    struct Error err1 = util::awkward_listarray_getitem_next_range_carrylength<T>(
      &carrylength,
      starts.ptr().get(),
      stops.ptr().get(),
      lenstarts,
      starts.offset(),
      stops.offset(),
      start,
      stop,
      step);
    util::handle_error(err1, classname(), id_.get());

    IndexOf<T> nextoffsets(lenstarts + 1);
    Index64 nextcarry(carrylength);

    struct Error err2 = util::awkward_listarray_getitem_next_range_64<T>(
      nextoffsets.ptr().get(),
      nextcarry.ptr().get(),
      starts.ptr().get(),
      stops.ptr().get(),
      lenstarts,
      starts.offset(),
      stops.offset(),
      start,
      stop,
      step);
    util::handle_error(err2, classname(), id_.get());
    std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);

    if (advanced.length() == 0) {
      return std::make_shared<ListOffsetArrayOf<T>>(id_, type_, nextoffsets, nextcontent.get()->getitem_next(nexthead, nexttail, advanced));
    }
    else {
      int64_t total;
      struct Error err1 = util::awkward_listarray_getitem_next_range_counts_64<T>(
        &total,
        nextoffsets.ptr().get(),
        lenstarts);
      util::handle_error(err1, classname(), id_.get());
      Index64 nextadvanced(total);
      struct Error err2 = util::awkward_listarray_getitem_next_range_spreadadvanced_64<T>(
        nextadvanced.ptr().get(),
        advanced.ptr().get(),
        nextoffsets.ptr().get(),
        lenstarts);
      util::handle_error(err2, classname(), id_.get());
      return std::make_shared<ListOffsetArrayOf<T>>(id_, type_, nextoffsets, nextcontent.get()->getitem_next(nexthead, nexttail, nextadvanced));
    }
  }

  template <typename T>
  const std::shared_ptr<Content> ListOffsetArrayOf<T>::getitem_next(const SliceArray64& array, const Slice& tail, const Index64& advanced) const {
    int64_t lenstarts = offsets_.length() - 1;
    IndexOf<T> starts = make_starts(offsets_);
    IndexOf<T> stops = make_stops(offsets_);
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    Index64 flathead = array.ravel();
    if (advanced.length() == 0) {
      Index64 nextcarry(lenstarts*flathead.length());
      Index64 nextadvanced(lenstarts*flathead.length());
      struct Error err = util::awkward_listarray_getitem_next_array_64<T>(
        nextcarry.ptr().get(),
        nextadvanced.ptr().get(),
        starts.ptr().get(),
        stops.ptr().get(),
        flathead.ptr().get(),
        starts.offset(),
        stops.offset(),
        lenstarts,
        flathead.length(),
        content_.get()->length());
      util::handle_error(err, classname(), id_.get());
      std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);
      return getitem_next_array_wrap(nextcontent.get()->getitem_next(nexthead, nexttail, nextadvanced), array.shape());
    }
    else {
      Index64 nextcarry(lenstarts);
      Index64 nextadvanced(lenstarts);
      struct Error err = util::awkward_listarray_getitem_next_array_advanced_64<T>(
        nextcarry.ptr().get(),
        nextadvanced.ptr().get(),
        starts.ptr().get(),
        stops.ptr().get(),
        flathead.ptr().get(),
        advanced.ptr().get(),
        starts.offset(),
        stops.offset(),
        lenstarts,
        flathead.length(),
        content_.get()->length());
      util::handle_error(err, classname(), id_.get());
      std::shared_ptr<Content> nextcontent = content_.get()->carry(nextcarry);
      return nextcontent.get()->getitem_next(nexthead, nexttail, nextadvanced);
    }
  }

  template class ListOffsetArrayOf<int32_t>;
  template class ListOffsetArrayOf<uint32_t>;
  template class ListOffsetArrayOf<int64_t>;
}
