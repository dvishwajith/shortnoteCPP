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
    
};


class Base2 {
public:
    Base2(){
        cout<< "Base2 constructor" << endl;
    }

    ~Base2(){
        cout<< "Base2 distructor" << endl;
    }
    
};

class Derived: public Base1, public Base2 {
public:
    Derived(){
        cout<< "Derived constructor" << endl;
    }   
    ~Derived(){
        cout<< "Derived disttructor" << endl;
    } 
};





 
int main() {
    cout << "Chack the order of contructor and distructor calls" << endl;
    Derived d;
    return 0;
}