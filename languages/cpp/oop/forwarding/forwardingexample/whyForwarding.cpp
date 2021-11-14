#include<iostream>
using namespace std;

void overloaded(const int &x)
{
    cout << "[lvalue]";
}

void overloaded(int &&x)
{
    cout << "[rvalue]";
}

template <typename T>
void WrapperFuncForOverloaded(T&& t)
{
    //calling both function show the difference of st::forward
    overloaded(t);  
    overloaded(std::forward<T>(t));  // normally you onlu have to call this ( std::forward<T>(t) is same as ------- staitc_cast<T&&>(t)
}


template <typename T>
void WrapperOverloadedNoForward(T&& t)
{
    //calling both function show the difference of st::forward
    overloaded(t);  
    overloaded(t);  // normally you onlu have to call this ( std::forward<T>(t) is same as ------- staitc_cast<T&&>(t)
}

int main() 
{
    int a, b;
    std::cout << "callng WrapperFuncForOverloaded() with lavalue :";
    WrapperFuncForOverloaded(a);

    std::cout << std::endl;

    std::cout << "callng WrapperFuncForOverloaded() with ravalue :";
    WrapperFuncForOverloaded(5);

    std::cout << std::endl;


    std::cout << "callng WrapperOverloadedNoForward() (No forwarding used) with lavalue :";
    WrapperOverloadedNoForward(a);

    std::cout << std::endl;

    std::cout << "callng WrapperOverloadedNoForward() (No forwarding used) with ravalue :";
    WrapperOverloadedNoForward(5);

    std::cout << std::endl;


    return 0;
}

//output is
/*

callng WrapperFuncForOverloaded() with lavalue :[lvalue][lvalue]
callng WrapperFuncForOverloaded() with ravalue :[lvalue][rvalue]

As you can see, if input is an lvalue , lvalue will be forwaded to the overloaded function and
 if input is an rvalue , rvalue will be forwaded to the overloaded function and

*/