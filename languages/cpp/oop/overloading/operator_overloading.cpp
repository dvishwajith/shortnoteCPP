#include<iostream>
using namespace std;
 

class complex 
{
protected:
    double real;
    double imag;

public:
    complex (double real=0, double imag=0);
    complex operator+(const complex &) const;
    std::string to_string();

    //unary operator (takes only one argumen) This is a incrementor  (and this is prefix operator). for example ++a;
    void operator++();

    // This is for postfix operations. No need  for example for    a++;
    void operator++(int);
};

complex::complex (double real, double imag)
{
    this->real = real;
    this->imag = imag;
}

/**
 * @brief Example for operator overloading using plus operations
 * 
 * @param arg       this_object is added with arg
 * @return complex addition
 */
complex complex::operator+(const complex &arg) const
{
    complex output;
    output.real = this->real + arg.real;
    output.imag = this->imag + arg.imag;
    return output;

}

std::string complex::to_string()
{
    return std::to_string(real) + "+" + std::to_string(imag) + "i"; 
}

/**
 * @brief Unary operator  ++a  prefix operator
 * 
 */
void complex::operator++()
{
    this->real = this->real + 1.0;
    this->imag = this->imag + 1.0;
}

/**
 * @brief Unary operator a++ postfix operator
 * 
 * @param arg 
 */
void complex::operator++(int arg)
{
    this->real = this->real + 1.0;
    this->imag = this->imag + 1.0;
}


int main() {
    complex a(1,3);
    complex b(4,5);

    auto c = a + b;

    // just checking assignment for fun
    complex d = c;
    complex &e = d;
    cout << e.to_string() << endl;

    // prefix increment operator test  ( ++a)
    complex inc_check(20,30);
    ++inc_check;  // prefix operator test
    std::cout << inc_check.to_string() << endl; 
    return 0;
}