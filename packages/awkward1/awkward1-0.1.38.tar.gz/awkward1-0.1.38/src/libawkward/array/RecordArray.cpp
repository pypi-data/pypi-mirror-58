// BSD 3-Clause License; see https://github.com/jpivarski/awkward-1.0/blob/master/LICENSE

#include <sstream>

#include "awkward/cpu-kernels/identity.h"
#include "awkward/cpu-kernels/getitem.h"
#include "awkward/type/RecordType.h"
#include "awkward/type/ArrayType.h"
#include "awkward/array/Record.h"

#include "awkward/array/RecordArray.h"

namespace awkward {
  RecordArray::RecordArray(const std::shared_ptr<Identity>& id, const std::shared_ptr<Type>& type, const std::vector<std::shared_ptr<Content>>& contents, const std::shared_ptr<util::RecordLookup>& recordlookup)
      : Content(id, type)
      , contents_(contents)
      , recordlookup_(recordlookup)
      , length_(0) {
    if (contents_.empty()) {
      throw std::runtime_error("this constructor can only be used with non-empty contents");
    }
    if (recordlookup_.get() != nullptr  &&  recordlookup_.get()->size() != contents_.size()) {
      throw std::runtime_error("recordlookup and contents must have the same length");
    }
    if (type_.get() != nullptr) {
      checktype();
    }
  }

  RecordArray::RecordArray(const std::shared_ptr<Identity>& id, const std::shared_ptr<Type>& type, const std::vector<std::shared_ptr<Content>>& contents)
      : Content(id, type)
      , contents_(contents)
      , recordlookup_(nullptr)
      , length_(0) {
    if (contents_.empty()) {
      throw std::runtime_error("this constructor can only be used with non-empty contents");
    }
    if (type_.get() != nullptr) {
      checktype();
    }
  }

  RecordArray::RecordArray(const std::shared_ptr<Identity>& id, const std::shared_ptr<Type>& type, int64_t length, bool istuple)
      : Content(id, type)
      , contents_()
      , recordlookup_(istuple ? nullptr : new util::RecordLookup)
      , length_(length) {
    if (type_.get() != nullptr) {
      checktype();
    }
  }

  const std::vector<std::shared_ptr<Content>> RecordArray::contents() const {
    return contents_;
  }

  const std::shared_ptr<util::RecordLookup> RecordArray::recordlookup() const {
    return recordlookup_;
  }

  bool RecordArray::istuple() const {
    return recordlookup_.get() == nullptr;
  }

  const std::string RecordArray::classname() const {
    return "RecordArray";
  }

  void RecordArray::setid() {
    int64_t len = length();
    if (len <= kMaxInt32) {
      std::shared_ptr<Identity> newid = std::make_shared<Identity32>(Identity::newref(), Identity::FieldLoc(), 1, len);
      Identity32* rawid = reinterpret_cast<Identity32*>(newid.get());
      struct Error err = awkward_new_identity32(rawid->ptr().get(), len);
      util::handle_error(err, classname(), id_.get());
      setid(newid);
    }
    else {
      std::shared_ptr<Identity> newid = std::make_shared<Identity64>(Identity::newref(), Identity::FieldLoc(), 1, len);
      Identity64* rawid = reinterpret_cast<Identity64*>(newid.get());
      struct Error err = awkward_new_identity64(rawid->ptr().get(), len);
      util::handle_error(err, classname(), id_.get());
      setid(newid);
    }
  }

  void RecordArray::setid(const std::shared_ptr<Identity>& id) {
    if (id.get() == nullptr) {
      for (auto content : contents_) {
        content.get()->setid(id);
      }
    }
    else {
      if (length() != id.get()->length()) {
        util::handle_error(failure("content and its id must have the same length", kSliceNone, kSliceNone), classname(), id_.get());
      }
      if (istuple()) {
        for (size_t j = 0;  j < contents_.size();  j++) {
          Identity::FieldLoc fieldloc(id.get()->fieldloc().begin(), id.get()->fieldloc().end());
          fieldloc.push_back(std::pair<int64_t, std::string>(id.get()->width() - 1, std::to_string(j)));
          contents_[j].get()->setid(id.get()->withfieldloc(fieldloc));
        }
      }
      else {
        Identity::FieldLoc original = id.get()->fieldloc();
        for (size_t j = 0;  j < contents_.size();  j++) {
          Identity::FieldLoc fieldloc(original.begin(), original.end());
          fieldloc.push_back(std::pair<int64_t, std::string>(id.get()->width() - 1, recordlookup_.get()->at(j)));
          contents_[j].get()->setid(id.get()->withfieldloc(fieldloc));
        }
      }
    }
    id_ = id;
  }

  const std::shared_ptr<Type> RecordArray::type() const {
    if (type_.get() != nullptr) {
      return type_;
    }
    else {
      std::vector<std::shared_ptr<Type>> types;
      for (auto item : contents_) {
        types.push_back(item.get()->type());
      }
      return std::make_shared<RecordType>(Type::Parameters(), types, recordlookup_);
    }
  }

  const std::shared_ptr<Content> RecordArray::astype(const std::shared_ptr<Type>& type) const {
    if (type.get() == nullptr  ||  dynamic_cast<RecordType*>(type.get()) == nullptr) {
      if (contents_.empty()) {
        return std::make_shared<RecordArray>(id_, type, length(), istuple());
      }
      else {
        return std::make_shared<RecordArray>(id_, type, contents_, recordlookup_);
      }
    }
    RecordType* raw = dynamic_cast<RecordType*>(type.get());
    std::vector<std::shared_ptr<Content>> contents;
    if (raw->recordlookup().get() == nullptr) {
      for (int64_t i = 0;  i < raw->numfields();  i++) {
        if (i >= numfields()) {
          throw std::invalid_argument(std::string("cannot assign type ") + type_.get()->tostring() + std::string(" to ") + classname());
        }
        contents.push_back(contents_[(size_t)i].get()->astype(raw->field(i)));
      }
    }
    else {
      for (auto key : raw->keys()) {
        if (!haskey(key)) {
          throw std::invalid_argument(std::string("cannot assign type ") + type_.get()->tostring() + std::string(" to ") + classname());
        }
        contents.push_back(contents_[(size_t)fieldindex(key)].get()->astype(raw->field(key)));
      }
    }
    if (contents.empty()) {
      return std::make_shared<RecordArray>(id_, type, length(), istuple());
    }
    else {
      return std::make_shared<RecordArray>(id_, type, contents, raw->recordlookup());
    }
  }

  const std::string RecordArray::tostring_part(const std::string& indent, const std::string& pre, const std::string& post) const {
    std::stringstream out;
    out << indent << pre << "<" << classname();
    if (contents_.empty()) {
      out << " length=\"" << length_ << "\"";
    }
    out << ">\n";
    if (id_.get() != nullptr) {
      out << id_.get()->tostring_part(indent + std::string("    "), "", "\n");
    }
    if (type_.get() != nullptr) {
      out << indent << "    <type>" + type().get()->tostring() + "</type>\n";
    }
    for (size_t j = 0;  j < contents_.size();  j++) {
      out << indent << "    <field index=\"" << j << "\"";
      if (!istuple()) {
        out << " key=\"" << recordlookup_.get()->at(j) << "\">";
      }
      else {
        out << ">";
      }
      out << "\n";
      out << contents_[j].get()->tostring_part(indent + std::string("        "), "", "\n");
      out << indent << "    </field>\n";
    }
    out << indent << "</" << classname() << ">" << post;
    return out.str();
  }

  void RecordArray::tojson_part(ToJson& builder) const {
    int64_t rows = length();
    size_t cols = contents_.size();
    std::shared_ptr<util::RecordLookup> keys = recordlookup_;
    if (istuple()) {
      keys = std::make_shared<util::RecordLookup>();
      for (size_t j = 0;  j < cols;  j++) {
        keys.get()->push_back(std::to_string(j));
      }
    }
    builder.beginlist();
    for (int64_t i = 0;  i < rows;  i++) {
      builder.beginrecord();
      for (size_t j = 0;  j < cols;  j++) {
        builder.field(keys.get()->at(j).c_str());
        contents_[j].get()->getitem_at_nowrap(i).get()->tojson_part(builder);
      }
      builder.endrecord();
    }
    builder.endlist();
  }

  int64_t RecordArray::length() const {
    if (contents_.empty()) {
      return length_;
    }
    else {
      int64_t out = -1;
      for (auto x : contents_) {
        int64_t len = x.get()->length();
        if (out < 0  ||  out > len) {
          out = len;
        }
      }
      return out;
    }
  }

  const std::shared_ptr<Content> RecordArray::shallow_copy() const {
    if (contents_.empty()) {
      return std::make_shared<RecordArray>(id_, type_, length(), istuple());
    }
    else {
      return std::make_shared<RecordArray>(id_, type_, contents_, recordlookup_);
    }
  }

  void RecordArray::check_for_iteration() const {
    if (id_.get() != nullptr  &&  id_.get()->length() < length()) {
      util::handle_error(failure("len(id) < len(array)", kSliceNone, kSliceNone), id_.get()->classname(), nullptr);
    }
  }

  const std::shared_ptr<Content> RecordArray::getitem_nothing() const {
    return getitem_range_nowrap(0, 0);
  }

  const std::shared_ptr<Content> RecordArray::getitem_at(int64_t at) const {
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

  const std::shared_ptr<Content> RecordArray::getitem_at_nowrap(int64_t at) const {
    return std::make_shared<Record>(*this, at);
  }

  const std::shared_ptr<Content> RecordArray::getitem_range(int64_t start, int64_t stop) const {
    if (contents_.empty()) {
      int64_t regular_start = start;
      int64_t regular_stop = stop;
      awkward_regularize_rangeslice(&regular_start, &regular_stop, true, start != Slice::none(), stop != Slice::none(), length());
      return std::make_shared<RecordArray>(id_, type_, regular_stop - regular_start, istuple());
    }
    else {
      std::vector<std::shared_ptr<Content>> contents;
      for (auto content : contents_) {
        contents.push_back(content.get()->getitem_range(start, stop));
      }
      return std::make_shared<RecordArray>(id_, type_, contents, recordlookup_);
    }
  }

  const std::shared_ptr<Content> RecordArray::getitem_range_nowrap(int64_t start, int64_t stop) const {
    if (contents_.empty()) {
      return std::make_shared<RecordArray>(id_, type_, stop - start, istuple());
    }
    else {
      std::vector<std::shared_ptr<Content>> contents;
      for (auto content : contents_) {
        contents.push_back(content.get()->getitem_range_nowrap(start, stop));
      }
      return std::make_shared<RecordArray>(id_, type_, contents, recordlookup_);
    }
  }

  const std::shared_ptr<Content> RecordArray::getitem_field(const std::string& key) const {
    return field(key).get()->getitem_range_nowrap(0, length());
  }

  const std::shared_ptr<Content> RecordArray::getitem_fields(const std::vector<std::string>& keys) const {
    RecordArray out(id_, type_, length(), istuple());
    if (istuple()) {
      for (auto key : keys) {
        out.append(field(key).get()->getitem_range_nowrap(0, length()));
      }
    }
    else {
      for (auto key : keys) {
        out.append(field(key).get()->getitem_range_nowrap(0, length()), key);
      }
    }
    return out.shallow_copy();
  }

  const std::shared_ptr<Content> RecordArray::carry(const Index64& carry) const {
    if (contents_.empty()) {
      std::shared_ptr<Identity> id(nullptr);
      if (id_.get() != nullptr) {
        id = id_.get()->getitem_carry_64(carry);
      }
      return std::make_shared<RecordArray>(id, type_, carry.length(), istuple());
    }
    else {
      std::vector<std::shared_ptr<Content>> contents;
      for (auto content : contents_) {
        contents.push_back(content.get()->carry(carry));
      }
      std::shared_ptr<Identity> id(nullptr);
      if (id_.get() != nullptr) {
        id = id_.get()->getitem_carry_64(carry);
      }
      return std::make_shared<RecordArray>(id, type_, contents, recordlookup_);
    }
  }

  const std::pair<int64_t, int64_t> RecordArray::minmax_depth() const {
    if (contents_.empty()) {
      return std::pair<int64_t, int64_t>(0, 0);
    }
    int64_t min = kMaxInt64;
    int64_t max = 0;
    for (auto content : contents_) {
      std::pair<int64_t, int64_t> minmax = content.get()->minmax_depth();
      if (minmax.first < min) {
        min = minmax.first;
      }
      if (minmax.second > max) {
        max = minmax.second;
      }
    }
    return std::pair<int64_t, int64_t>(min, max);
  }

  int64_t RecordArray::numfields() const {
    return (int64_t)contents_.size();
  }

  int64_t RecordArray::fieldindex(const std::string& key) const {
    return util::fieldindex(recordlookup_, key, numfields());
  }

  const std::string RecordArray::key(int64_t fieldindex) const {
    return util::key(recordlookup_, fieldindex, numfields());
  }

  bool RecordArray::haskey(const std::string& key) const {
    return util::haskey(recordlookup_, key, numfields());
  }

  const std::vector<std::string> RecordArray::keys() const {
    return util::keys(recordlookup_, numfields());
  }

  const std::shared_ptr<Content> RecordArray::field(int64_t fieldindex) const {
    if (fieldindex >= numfields()) {
      throw std::invalid_argument(std::string("fieldindex ") + std::to_string(fieldindex) + std::string(" for record with only " + std::to_string(numfields()) + std::string(" fields")));
    }
    return contents_[(size_t)fieldindex];
  }

  const std::shared_ptr<Content> RecordArray::field(const std::string& key) const {
    return contents_[(size_t)fieldindex(key)];
  }

  const std::vector<std::shared_ptr<Content>> RecordArray::fields() const {
    return std::vector<std::shared_ptr<Content>>(contents_);
  }

  const std::vector<std::pair<std::string, std::shared_ptr<Content>>> RecordArray::fielditems() const {
    std::vector<std::pair<std::string, std::shared_ptr<Content>>> out;
    if (istuple()) {
      size_t cols = contents_.size();
      for (size_t j = 0;  j < cols;  j++) {
        out.push_back(std::pair<std::string, std::shared_ptr<Content>>(std::to_string(j), contents_[j]));
      }
    }
    else {
      size_t cols = contents_.size();
      for (size_t j = 0;  j < cols;  j++) {
        out.push_back(std::pair<std::string, std::shared_ptr<Content>>(recordlookup_.get()->at(j), contents_[j]));
      }
    }
    return out;
  }

  const RecordArray RecordArray::astuple() const {
    if (type_.get() == nullptr) {
      return RecordArray(id_, Type::none(), contents_);
    }
    else {
      RecordType* raw = dynamic_cast<RecordType*>(type_.get());
      return RecordArray(id_, raw->astuple(), contents_);
    }
  }

  void RecordArray::append(const std::shared_ptr<Content>& content, const std::string& key) {
    if (recordlookup_.get() == nullptr) {
      recordlookup_ = util::init_recordlookup(numfields());
    }
    contents_.push_back(content);
    recordlookup_.get()->push_back(key);
    if (type_.get() != nullptr) {
      if (RecordType* raw = dynamic_cast<RecordType*>(type_.get())) {
        raw->append(content.get()->type(), key);
      }
    }
  }

  void RecordArray::append(const std::shared_ptr<Content>& content) {
    if (recordlookup_.get() == nullptr) {
      contents_.push_back(content);
    }
    else {
      append(content, std::to_string(numfields()));
    }
    if (type_.get() != nullptr) {
      if (RecordType* raw = dynamic_cast<RecordType*>(type_.get())) {
        raw->append(content.get()->type());
      }
    }
  }

  void RecordArray::checktype() const {
    bool okay = false;
    if (RecordType* raw = dynamic_cast<RecordType*>(type_.get())) {
      if (raw->recordlookup().get() != nullptr  &&  recordlookup_.get() != nullptr) {
        okay = *(raw->recordlookup().get()) == *(recordlookup_.get());
      }
      else {
        okay = (raw->numfields() == numfields());
      }
      if (okay) {
        for (size_t i = 0;  i < contents_.size();  i++) {
          if (!contents_[i].get()->istypeptr(raw->field((int64_t)i).get())) {
            okay = false;
            break;
          }
        }
      }
    }
    if (!okay) {
        throw std::invalid_argument(std::string("cannot assign type ") + type_.get()->tostring() + std::string(" to ") + classname());
    }
  }

  const std::shared_ptr<Content> RecordArray::getitem_next(const std::shared_ptr<SliceItem>& head, const Slice& tail, const Index64& advanced) const {
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    Slice emptytail;
    emptytail.become_sealed();

    if (head.get() == nullptr) {
      return shallow_copy();
    }
    else if (SliceField* field = dynamic_cast<SliceField*>(head.get())) {
      std::shared_ptr<Content> out = getitem_next(*field, emptytail, advanced);
      return out.get()->getitem_next(nexthead, nexttail, advanced);
    }
    else if (SliceFields* fields = dynamic_cast<SliceFields*>(head.get())) {
      std::shared_ptr<Content> out = getitem_next(*fields, emptytail, advanced);
      return out.get()->getitem_next(nexthead, nexttail, advanced);
    }
    else if (contents_.empty()) {
      RecordArray out(Identity::none(), type_, length(), istuple());
      return out.getitem_next(nexthead, nexttail, advanced);
    }
    else {
      std::vector<std::shared_ptr<Content>> contents;
      for (auto content : contents_) {
        contents.push_back(content.get()->getitem_next(head, emptytail, advanced));
      }
      std::shared_ptr<Type> type = Type::none();
      if (head.get()->preserves_type(type_, advanced)) {
        type = type_;
      }
      RecordArray out(Identity::none(), type, contents, recordlookup_);
      return out.getitem_next(nexthead, nexttail, advanced);
    }
  }

  const std::shared_ptr<Content> RecordArray::getitem_next(const SliceAt& at, const Slice& tail, const Index64& advanced) const {
    throw std::invalid_argument(std::string("undefined operation: RecordArray::getitem_next(at)"));
  }

  const std::shared_ptr<Content> RecordArray::getitem_next(const SliceRange& range, const Slice& tail, const Index64& advanced) const {
    throw std::invalid_argument(std::string("undefined operation: RecordArray::getitem_next(range)"));
  }

  const std::shared_ptr<Content> RecordArray::getitem_next(const SliceArray64& array, const Slice& tail, const Index64& advanced) const {
    throw std::invalid_argument(std::string("undefined operation: RecordArray::getitem_next(array)"));
  }

  const std::shared_ptr<Content> RecordArray::getitem_next(const SliceField& field, const Slice& tail, const Index64& advanced) const {
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    return getitem_field(field.key()).get()->getitem_next(nexthead, nexttail, advanced);
  }

  const std::shared_ptr<Content> RecordArray::getitem_next(const SliceFields& fields, const Slice& tail, const Index64& advanced) const {
    std::shared_ptr<SliceItem> nexthead = tail.head();
    Slice nexttail = tail.tail();
    return getitem_fields(fields.keys()).get()->getitem_next(nexthead, nexttail, advanced);
  }

}
