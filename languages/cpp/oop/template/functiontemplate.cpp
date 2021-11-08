#include<iostream>
using namespace std;
 



class Base1 {
public:
    Base1(){
        cout<< "Base1 constructor" << endl;
    }


    ~Base1(){
        cout<< "Base1 distructor" << endl;
    }

    template <class T>
    T add(T a, T b)
    {
        return a+b;
    }
    
};

 
int main() {
    Base1 base;
    auto ret_int = base.add<int>( 1, 5);
    cout << "ret_int " << ret_int << endl;

    auto ret_float = base.add<float>( 1.3f, 5.5f);
    cout << "ret_float " << ret_float << endl;

    auto ret_double = base.add<double>( 1.56d, 5.73d);
    cout << "ret_double " << ret_double << endl;

    /**
     * template type need not to be defined, if it can be decided by parameters
     * 
     */
    auto ret_auto = base.add( 1.56, 5.73);
    cout << "ret_auto (auto type is " << typeid(ret_auto).name() <<") " << ret_auto << endl;

    auto ret_auto2 = base.add( 1.56f, 5.73f);
    cout << "ret_auto2 (auto type is " << typeid(ret_auto2).name() <<") " << ret_auto2 << endl;

    auto ret_auto3 = base.add( 1, 5);
    cout << "ret_auto3 (auto type is " << typeid(ret_auto3).name() <<") " << ret_auto3 << endl;
    
    /**
     * This works as well
     * 
     */
    int a = 1, b = 3;

    auto ret_auto4 = base.add( a, b);
    cout << "ret_auto4 (auto type is " << typeid(ret_auto4).name() <<") " << ret_auto4 << endl;

    return 0;
}