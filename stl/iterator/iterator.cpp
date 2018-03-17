#include <iostream>
#include <vector>

using namespace std;

int main(){

    vector <int> vect ;
    vect.push_back(0);
    vect.push_back(1);
    vect.push_back(2);
    vect.push_back(3);
    vect.push_back(4);

    for(auto i=vect.begin(); i != vect.end() ; i++ ){
        cout << "vect out " << *i << endl ;
    }


    // not that in here not hte pointer is printed
    for(auto i : vect ){
        cout << "Even smaller vect out " << i << endl ;
    }
}