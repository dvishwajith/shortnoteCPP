#include "WrapperClass.h"


Napi::FunctionReference WrapperClass::constructor;

WrapperClass::WrapperClass(const Napi::CallbackInfo& info) : Napi::ObjectWrap<WrapperClass>(info)  {
  Napi::Env env = info.Env();
  Napi::HandleScope scope(env);

  int length = info.Length();
  if (length != 1 || !info[0].IsNumber()) {
    Napi::TypeError::New(env, "Number expected").ThrowAsJavaScriptException();
  }

  Napi::Number value = info[0].As<Napi::Number>();
  this->actualClass_ = new ActualClass(value.DoubleValue());
}

Napi::Value WrapperClass::GetValue(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();
  Napi::HandleScope scope(env);

  double num = this->actualClass_->getValue();
  return Napi::Number::New(env, num);
}


Napi::Value WrapperClass::Add(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();
  Napi::HandleScope scope(env);

  if (  info.Length() != 1 || !info[0].IsNumber()) {
    Napi::TypeError::New(env, "Number expected").ThrowAsJavaScriptException();
  }

  Napi::Number toAdd = info[0].As<Napi::Number>();
  double answer = this->actualClass_->add(toAdd.DoubleValue());

  return Napi::Number::New(info.Env(), answer);
}




Napi::Object WrapperClass::Init(Napi::Env env, Napi::Object exports) {
  Napi::HandleScope scope(env);

  Napi::Function func = DefineClass(env, "WrapperClass", {
    InstanceMethod("add", &WrapperClass::Add),
    InstanceMethod("getValue", &WrapperClass::GetValue),
  });

  constructor = Napi::Persistent(func);
  constructor.SuppressDestruct();

  exports.Set("WrapperClass", func);
  return exports;
}

