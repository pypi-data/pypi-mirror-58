// BSD 3-Clause License; see https://github.com/jpivarski/awkward-1.0/blob/master/LICENSE

#ifndef AWKWARD_NUMPYARRAY_H_
#define AWKWARD_NUMPYARRAY_H_

#include <cassert>
#include <string>
#include <memory>
#include <vector>

#include "awkward/cpu-kernels/util.h"
#include "awkward/Slice.h"
#include "awkward/Content.h"

namespace awkward {
  class NumpyArray: public Content {
  public:
    static const std::shared_ptr<Type> unwrap_regulartype(const std::shared_ptr<Type>& type, const std::vector<ssize_t>& shape);

    NumpyArray(const std::shared_ptr<Identity>& id, const std::shared_ptr<Type>& type, const std::shared_ptr<void>& ptr, const std::vector<ssize_t>& shape, const std::vector<ssize_t>& strides, ssize_t byteoffset, ssize_t itemsize, const std::string format);

    const std::shared_ptr<void> ptr() const;
    const std::vector<ssize_t> shape() const;
    const std::vector<ssize_t> strides() const;
    ssize_t byteoffset() const;
    ssize_t itemsize() const;
    const std::string format() const;

    ssize_t ndim() const;
    bool isempty() const;
    void* byteptr() const;
    void* byteptr(ssize_t at) const;
    ssize_t bytelength() const;
    uint8_t getbyte(ssize_t at) const;

    bool isscalar() const override;
    const std::string classname() const override;
    void setid() override;
    void setid(const std::shared_ptr<Identity>& id) override;
    bool istypeptr(Type* pointer) const override;
    const std::shared_ptr<Type> type() const override;
    const std::shared_ptr<Content> astype(const std::shared_ptr<Type>& type) const override;
    const std::string tostring_part(const std::string& indent, const std::string& pre, const std::string& post) const override;
    void tojson_part(ToJson& builder) const override;
    int64_t length() const override;
    const std::shared_ptr<Content> shallow_copy() const override;
    void check_for_iteration() const override;
    const std::shared_ptr<Content> getitem_nothing() const override;
    const std::shared_ptr<Content> getitem_at(int64_t at) const override;
    const std::shared_ptr<Content> getitem_at_nowrap(int64_t at) const override;
    const std::shared_ptr<Content> getitem_range(int64_t start, int64_t stop) const override;
    const std::shared_ptr<Content> getitem_range_nowrap(int64_t start, int64_t stop) const override;
    const std::shared_ptr<Content> getitem_field(const std::string& key) const override;
    const std::shared_ptr<Content> getitem_fields(const std::vector<std::string>& keys) const override;
    const std::shared_ptr<Content> getitem(const Slice& where) const override;
    const std::shared_ptr<Content> getitem_next(const std::shared_ptr<SliceItem>& head, const Slice& tail, const Index64& advanced) const override;
    const std::shared_ptr<Content> carry(const Index64& carry) const override;
    const std::pair<int64_t, int64_t> minmax_depth() const override;
    int64_t numfields() const override;
    int64_t fieldindex(const std::string& key) const override;
    const std::string key(int64_t fieldindex) const override;
    bool haskey(const std::string& key) const override;
    const std::vector<std::string> keys() const override;

    bool iscontiguous() const;
    void become_contiguous();
    const NumpyArray contiguous() const;

  protected:
    void checktype() const override;

    const std::shared_ptr<Content> getitem_next(const SliceAt& at, const Slice& tail, const Index64& advanced) const override;
    const std::shared_ptr<Content> getitem_next(const SliceRange& range, const Slice& tail, const Index64& advanced) const override;
    const std::shared_ptr<Content> getitem_next(const SliceArray64& array, const Slice& tail, const Index64& advanced) const override;
    const std::shared_ptr<Content> getitem_next(const SliceField& field, const Slice& tail, const Index64& advanced) const override;
    const std::shared_ptr<Content> getitem_next(const SliceFields& fields, const Slice& tail, const Index64& advanced) const override;

    const NumpyArray contiguous_next(const Index64& bytepos) const;
    const NumpyArray getitem_bystrides(const std::shared_ptr<SliceItem>& head, const Slice& tail, int64_t length) const;
    const NumpyArray getitem_bystrides(const SliceAt& at, const Slice& tail, int64_t length) const;
    const NumpyArray getitem_bystrides(const SliceRange& range, const Slice& tail, int64_t length) const;
    const NumpyArray getitem_bystrides(const SliceEllipsis& ellipsis, const Slice& tail, int64_t length) const;
    const NumpyArray getitem_bystrides(const SliceNewAxis& newaxis, const Slice& tail, int64_t length) const;
    const NumpyArray getitem_next(const std::shared_ptr<SliceItem>& head, const Slice& tail, const Index64& carry, const Index64& advanced, int64_t length, int64_t stride, bool first) const;
    const NumpyArray getitem_next(const SliceAt& at, const Slice& tail, const Index64& carry, const Index64& advanced, int64_t length, int64_t stride, bool first) const;
    const NumpyArray getitem_next(const SliceRange& range, const Slice& tail, const Index64& carry, const Index64& advanced, int64_t length, int64_t stride, bool first) const;
    const NumpyArray getitem_next(const SliceEllipsis& ellipsis, const Slice& tail, const Index64& carry, const Index64& advanced, int64_t length, int64_t stride, bool first) const;
    const NumpyArray getitem_next(const SliceNewAxis& newaxis, const Slice& tail, const Index64& carry, const Index64& advanced, int64_t length, int64_t stride, bool first) const;
    const NumpyArray getitem_next(const SliceArray64& array, const Slice& tail, const Index64& carry, const Index64& advanced, int64_t length, int64_t stride, bool first) const;

  void tojson_boolean(ToJson& builder) const;
  template <typename T>
  void tojson_integer(ToJson& builder) const;
  template <typename T>
  void tojson_real(ToJson& builder) const;
  void tojson_string(ToJson& builder) const;

  private:
    std::shared_ptr<void> ptr_;
    std::vector<ssize_t> shape_;
    std::vector<ssize_t> strides_;
    ssize_t byteoffset_;
    const ssize_t itemsize_;
    const std::string format_;
  };
}

#endif // AWKWARD_NUMPYARRAY_H_
