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

    int add(int a, int b)
    {
        return a+b;
    }
    
    // different parameters . Correct
    int add(float a, float b)
    {
        return a+b;
    }

/*
    // This conflict with  "int add(float a, float b)" . Have to choose one of those because
    // cannot overload functions distinguished by return type aloneC/C++(311)
    float add(float a, float b)
    {
        return a+b;
    }
 
*/

    // different number of paramters correct
    float add(int a, int b, int c)
    {
        return a+b;
    }
    
};

 
int main() {
    Base1 b;
    int ret_int = b.add( 1, 5);
    cout << "ret_int " << ret_int << endl;

    float ret_float = b.add( 1.0f, 5.0f);
    cout << "ret_float " << ret_float << endl;
    
    return 0;
}