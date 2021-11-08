#include <iostream>
#include <cstring>

using  namespace std;



class ShallowCopyString
{
private:
    char *s;
    int size;

public:
    ShallowCopyString(const char *str=NULL);
    ~ShallowCopyString();

    void print();    
    void change(const char *);

};

ShallowCopyString::ShallowCopyString(const char *str){
    size = strlen(str);
    s = new char [size+1];
    strcpy(s,str);
}

ShallowCopyString::~ShallowCopyString(){
    delete(s);
}



void ShallowCopyString::change(const char *str){
    delete [] s;
    size = strlen(str);
    s = new char [size+1];
    strcpy(s,str);
}

void ShallowCopyString::print(){
    cout << "\""<< s<< "\""  << endl ;
}




int main(){
    cout << "\n Vishwajith : Double free courruption error will be printed , because char *S is opimized out from the compiler beacause of the shallow copy" << endl;

    ShallowCopyString str1("string1Content");
    cout << "str1 print" << endl;
    str1.print(); // what is printed ?

    ShallowCopyString str2 = str1;
    cout << "\nDeep copy str1 to str2" << endl;
 
    cout << "str2 print" << endl;
    str2.print();
 
    cout << "\nchange str2 content" << endl;
    str2.change("Changedstring2Content");
 
    cout << "\nstr1 print" << endl;
    str1.print(); // what is printed now ?
    cout << "\nstr2 print" << endl;
    str2.print();


    return 0;

}