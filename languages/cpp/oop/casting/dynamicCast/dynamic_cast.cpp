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
    auto ptr = dynamic_cast<D*>(pb);
    if(ptr)
    {
        ptr->D_print();
        ptr->print();
    }
    else
    {
        cout << "wrong cast in " << __FUNCTION__ << ":" << __LINE__ << endl;
    }
    

}

void DownCastingException(B& b)
{
    try
    {
        auto d = dynamic_cast<D&>(b);
        d.D_print();
        d.print();      
    }
    catch(const std::bad_cast & e)
    {
        std::cerr << e.what() << '\n';
    }
}

void UpCasting(B* pd)
{
    auto ptr = dynamic_cast<B*>(pd);
    if(ptr)
    {
        ptr->B_print();
        //ptr->D_print(); cannot call D_print since this is upcasted to class B
        ptr->print();
    }
    else
    {
        cout << "wrong cast in " << __FUNCTION__ << ":" << __LINE__ << endl;
    }

}

int main() 
{
    B * pb = new B();
    D * pd = new D();

    cout << "***DownCasting test with DownCasting(pd);" << endl;
    DownCasting(pd);

    cout << "***DownCasting test with DownCasting(pb);" << endl;
    DownCasting(pb);

    cout << "***UpCasting test with UpCasting(pd);" << endl;
    UpCasting(pd);

    cout << "***UpCasting test with UpCasting(pb);" << endl;
    UpCasting(pb);

    cout << "***DownCasting test with DownCastingException(*pd);" << endl;
    DownCastingException(*pd); 

    cout << "***DownCasting test with DownCastingException(*pb);" << endl;
    DownCastingException(*pb);

    return 0;
}