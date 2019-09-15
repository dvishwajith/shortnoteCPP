/* cppsrc/main.cpp */
#include <napi.h>
#include "Samples/functionexample.h"
#include "Samples/WrapperClass.h"

Napi::Object InitAll(Napi::Env env, Napi::Object exports) {
  functionexample::Init(env, exports);
  return WrapperClass::Init(env,exports);
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, InitAll)