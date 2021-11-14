#include<iostream>
using namespace std;

/**
 * @brief Function with R value
 * 
 * @param a rvalue
 */
void foo(int &&a)
{
    cout << "rvalue function paramter input called with parameter value " << a << endl;
    a = 3;
    cout << "changed paramter value to " << a << endl;
}

/**
 * @brief Function with l value
 * 
 * @param a lvalue
 */
void foo(int &a)
{
    cout << "lvalue function paramter input called with parameter value " << a << endl;
    a = 4;
    cout << "changed paramter value to " << a << endl;
}

// /**
//  * @brief Function with pass by value. This will work. But you cant change the variable inside
//  * 
//  * @param a lvalue
//  */
// void foo(int a)
// {
//     cout << "value function paramter input called with parameter value " << a << endl;
// }


/*
If we dedeind a template type for foo, then we will not have to create two functions like  this
void foo(int &&a)
void foo(int &a)
for example
*/
template <typename T>
void modifiedfoo(T&& t)
{
    t = __LINE__;
    cout << __FUNCTION__ << endl;
}

int main() {

    int i, j, *p;
    j = 0;

    //corrct usage:  i is an lvalue, 7 is a rvalue
    i = 7;

    //incorrect usage. (error: lvalue required as left operand of assignment)
    // 7 = i;
    // 7*j = i;

    // correct usage: Conditional operator returns an lvalue
    (i < 3) ? i : j = 5;
    cout <<  "i " << i << endl;
    cout <<  "j " << j << endl;


    /*********Function paramters with lvalue and rvalue**************************/

    foo(5);     // this will call the function with rvalue paramter  because 5 is an rvalue
    foo(i);     // this will call the function with lvalue paramter  because i is an lvalue
    cout <<  "i " << i << endl;
    foo(i + 3); // this will call the function with rvalue paramter  because i+3 is an rvalue
    cout <<  "i " << i << endl;

    //int&& c = b;  //Error. An rValue reference cannot be pointed to a lValue.
    int&& d = 10;  //Compiles with no error.
    cout << "d " << d << endl;
    foo(d);
    cout << "d " << d << endl;
    d = 9;
    d = j;
    cout << "d " << d << endl;


    int m =  __LINE__;
    modifiedfoo(m);             // modifiedfoo<int&>(int& &&) -> modifiedfoo<int&>(int&)
    cout << "m " << m << endl;

    modifiedfoo(500);
    cout << "m " << m << endl;  // modifiedfoo<int&&>(int&& &&) -> modifiedfoo<int&&>(int&&)
   /**
    * No need to define two foo functions , if we use template functions
    * 
    * This is how template deduce types
      
            TR   R
      
            T&   &  -> T&  // lvalue reference to cv TR -> lvalue reference to T
            T&   && -> T&  // rvalue reference to cv TR -> TR (lvalue reference to T)
            T&&  &  -> T&  // lvalue reference to cv TR -> lvalue reference to T
            T&&  && -> T&& // rvalue reference to cv TR -> TR (rvalue reference to T)

            template <typename T>
            void modifiedfoo(T&& t)
            above will tranfor following to

            modifiedfoo(m);     modifiedfoo<int&>(int& &&) -> modifiedfoo<int&>(int&)
            modifiedfoo(500);   modifiedfoo<int&&>(int&& &&) -> modifiedfoo<int&&>(int&&)
    * 
    */



    // correcr usage: deferenced pointer is and lvalue  (althogh there is a segfault here/ but no compile errors)
    *p = i;

    return 0;
}