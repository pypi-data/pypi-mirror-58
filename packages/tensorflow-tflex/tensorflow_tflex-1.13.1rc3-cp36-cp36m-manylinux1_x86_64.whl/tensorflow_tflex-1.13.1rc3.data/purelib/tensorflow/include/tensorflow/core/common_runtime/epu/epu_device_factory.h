#ifndef TENSORFLOW_COMMON_RUNTIME_EPU_EPU_DEVICE_FACTORY_H_
#define TENSORFLOW_COMMON_RUNTIME_EPU_EPU_DEVICE_FACTORY_H_

// Register a factory that provides EPU devices.
#include "tensorflow/core/common_runtime/epu/epu_device.h"

#include <vector>
#include "tensorflow/core/common_runtime/device_factory.h"
#include "tensorflow/core/framework/allocator.h"
#include "tensorflow/core/public/session_options.h"

namespace tensorflow {

class EPUDeviceFactory : public DeviceFactory {
 public:
  Status CreateDevices(const SessionOptions& options, const string& name_prefix,
                       std::vector<std::unique_ptr<Device>>* devices) override;
  ~EPUDeviceFactory();

 private:
  bool inited = false;
  int devid[MAX_EPU_DEV_NUM];
  Allocator* calloc;
  EPU* epu[MAX_EPU_DEV_NUM];
  EPUAllocator* ealloc[MAX_EPU_DEV_NUM];
  EPUDeviceContextCoreX* ctx[MAX_EPU_DEV_NUM];
  EPUDNN* dnn[MAX_EPU_DEV_NUM];
  string name[MAX_EPU_DEV_NUM];
};

}  // namespace tensorflow
#endif
