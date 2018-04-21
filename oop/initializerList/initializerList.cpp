#include<iostream>
using namespace std;
 


class A {
    const int t;
public:
    A(int value):t(value){

    }

    int getT(){
        return t;
    }
};
 
int main() {
    cout << " To assign a contant data member value to a object , we have to use initializer List. " << endl;
    cout << " There are other reasons too . Search them" << endl;
    A a(10);
    cout<<a.getT() << endl;
    return 0;
}