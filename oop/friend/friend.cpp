#include<iostream>
using namespace std;
 


class A {
private:
    int x;
public:
    A(){
        x = 5;
    }

    int getx(){
        return x;
    }

    friend void show(A&);
};

void show(A& a){
    cout << "A::x :" << a.x << endl;
    a.x = 10;
}



 
int main() {
    A a;
    show(a);
    show(a);
    return 0;
}