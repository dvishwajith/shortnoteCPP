#include<iostream>
using namespace std;

/**
 * This example works even without forwarding.
 * Because function  new T() is going to use different function
 * according to the type always. It is not overloaded. So compiler can identify which 
 * function to actually call. 
 *
 */

template <typename T, typename A1, typename A2>
T * factory(A1 &&a1, A2 &&a2)
{
    return new T(a1, a2);
} 

template <typename T, typename ... Args>
T * factory2(Args&& ... args)
{
    return new T((args)...);
} 

struct W
{
    W(int& a, int& b)
    {
        a=0; b=0;
        cout << "called by " << __FUNCTION__ << endl;
        //cout << "a type" << typeid(a).name() << "b type" << typeid(b).name() << endl;
    }
};

struct X
{
    X(const int& a, int& b)
    {
        b=1;
        cout << "called by " << __FUNCTION__ << endl;
        //cout << "a type" << typeid(a).name() << "b type" << typeid(b).name() << endl;
    }
};

struct Y
{
    Y(int& a, const int& b)
    {
        a=2; 
        cout << "called by " << __FUNCTION__ << endl;
        //cout << "a type" << typeid(a).name() << "b type" << typeid(b).name() << endl;
    }
};

struct Z
{
    Z(const int& a, const int& b)
    {
        cout << "called by " << __FUNCTION__ << endl;
        //cout << "a type" << typeid(a).name() << "b type" << typeid(b).name() << endl;
    }
};

int main() 
{

    int a,b;
    a =__LINE__; b=__LINE__;
    auto obj1 = factory<W>(a, b);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj2 = factory<X>(7, b);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj3 = factory<Y>(a, 8);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj4 = factory<Z>(5, 6);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj5 = factory<X>(a, b);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj6 = factory<Y>(a, b);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj7 = factory<Z>(a, b);
    cout << "a " << a << " b " << b << endl;

    // factory pattter with variadic template

    a =__LINE__; b=__LINE__;
    auto obj8 = factory2<W>(a, b);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj9 = factory2<X>(a, b);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj10 = factory2<Y>(a, b);
    cout << "a " << a << " b " << b << endl;

    a =__LINE__; b=__LINE__;
    auto obj11 = factory2<Z>(a, b);
    cout << "a " << a << " b " << b << endl;
        
    
    return 0;
}