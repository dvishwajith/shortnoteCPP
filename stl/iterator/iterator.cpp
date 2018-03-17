#include <iostream>
#include <vector>

using namespace std;

int main(){

    // You can use queue for iterator as well

    vector <int> vect ;
    vect.push_back(0);
    vect.push_back(1);
    vect.push_back(2);
    vect.push_back(3);
    vect.push_back(4);

    for(auto i=vect.begin(); i != vect.end() ; i++ ){  // not that vector begin returns and iterator . Not and integer
        cout << "vect out " << *i << endl ;
    }


    // not that in here not hte pointer is printed  and the object get copied 
    for(auto i : vect ){
        cout << "Even smaller vect out " << i << endl ;
    }

    // use this if you want to change vecto veriables
    for(auto i : vect ){
        i = i + 20;
        cout << "Try adding 20 to vector vaule using 'auto i' vect out " << i << endl ;
    }

        // not that in here not hte pointer is printed  and the object get copied 
    for(auto i : vect ){
        cout << "After changing , you can see it is not changed  vect out " << i << endl ;
    }

    // use this if you want to change vecto veriables
    for(auto &i : vect ){
        i = i+50;
        cout << "Try  adding 50 to vector vaule using 'auto &i' vect out " << i << endl ;
    }

        // not that in here not hte pointer is printed  and the object get copied 
    for(auto i : vect ){
        cout << "It is changed  vect out " << i << endl ;
    }    
}