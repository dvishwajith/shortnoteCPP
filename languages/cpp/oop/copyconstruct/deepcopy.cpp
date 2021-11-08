#include <iostream>
#include <cstring>

using  namespace std;

class DeepCopyString
{
private:
    char *s;
    int size;

public:
    DeepCopyString(const char *str=NULL);
    ~DeepCopyString();
    DeepCopyString(const DeepCopyString& str);
    void print();    
    void change(const char *);

};

DeepCopyString::DeepCopyString(const char *str){
    size = strlen(str);
    s = new char [size+1];
    strcpy(s,str);
}

DeepCopyString::~DeepCopyString(){
    delete(s);
}

DeepCopyString::DeepCopyString(const DeepCopyString& str){
    size = str.size;
    s = new char [size+1];
    strcpy(s,str.s);
}

void DeepCopyString::change(const char *str){
    delete [] s;
    size = strlen(str);
    s = new char [size+1];
    strcpy(s,str);
}

void DeepCopyString::print(){
    cout << "\""<< s<< "\""  << endl ;
}






int main(){
    DeepCopyString str1("string1Content");
    cout << "str1 print" << endl;
    str1.print(); // what is printed ?

    DeepCopyString str2 = str1;
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