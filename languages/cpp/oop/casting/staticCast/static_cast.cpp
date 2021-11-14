#include<iostream>
#include <memory>
using namespace std;

class B 
{
    public:
    void B_print()
    {
        cout << "printing inside " << __FUNCTION__ << " line " << __LINE__ << endl;
    }

    virtual void print()
    {
        cout << "printing inside " << __FUNCTION__ << " line " << __LINE__ << endl;
    }
};

class D: public B
{
    public:
    void D_print()
    {
        cout << "printing inside " << __FUNCTION__ << " line " << __LINE__ << endl;
    }

    virtual void print()
    {
        cout << "printing inside " << __FUNCTION__ << " line " << __LINE__ << endl;
    }
};

void DownCasting(B* pb)
{
    auto ptr = static_cast<D*>(pb);
    ptr->D_print();
    ptr->print();

}

void UpCasting(B* pd)
{
    auto ptr = static_cast<B*>(pd);
    ptr->B_print();
    //ptr->D_print(); cannot call D_print since this is upcasted to class B
    ptr->print();

}

int main() 
{
    B * pb = new B();
    D * pd = new D();

    cout << "***DownCasting test with DownCasting(pd);" << endl;
    DownCasting(pd);

    cout << "***UpCasting test with UpCasting(pd);" << endl;
    UpCasting(pd);

    cout << "***UpCasting test with UpCasting(pb);" << endl;
    UpCasting(pb);

    double double_number = 123.543;
    int int_number = static_cast<int>(double_number);
    cout << "double_number " << double_number << " is casted to int_number " << int_number << endl;


    return 0;
}