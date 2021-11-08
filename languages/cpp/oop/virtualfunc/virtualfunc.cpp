#include<iostream>
using namespace std;
 



class Base{
public:
    virtual void print() { cout << "In Base class" << endl;}
};


class Derived: public Base
{
public:
    void print() { cout << "In Derived class" << endl;}
};


class pureVirtual{ // This is a abstract class beacuse , this has a pure virtual function
public:
    virtual void print() {}
};

 
int main() {
    Base *b = new Derived;
    b->print();

    Base b1;
    b1.print();

    return 0;
}