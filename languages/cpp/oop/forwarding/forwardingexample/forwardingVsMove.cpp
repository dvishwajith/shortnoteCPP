#include<iostream>
using namespace std;

typedef struct 
{
    int data;
} ADT;


/**
 * @brief You don’t want to use std::move or std::forward because the client should expect their object to be modified – but not expired – after the call.
 *
 */
void func(ADT& param)
{
  ADT temp = param;  // Copy object
  cout << "func(ADT& param) called with .data val " << temp.data << endl;
}


/**
 * @brief  Overloading with an r-value reference parameter is an explicit declaration that you intend to move from the parameter.
 * 
 */
void func(ADT&& param)
{
  ADT temp = std::move(param);  //  See rules below
  cout << "func(ADT&& param) called with .data val " << temp.data << endl;
}


template<typename T>
void wrapper_func(T&& t)
{
    cout << __FUNCTION__ << " called ";
    func(std::forward<T>(t));
}


/*
Collapsing rules for forward function

*/

int main() 
{
    //calling with lvalue
    ADT a = {1};
    wrapper_func(a);

    //calling with rvalue
    wrapper_func(
        ADT{
            .data = 5
            }
        );
}

