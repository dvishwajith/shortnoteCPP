#include<iostream>
#include <memory>
using namespace std;



int main() 
{
    float float_number = 123.543;
    uint32_t uint_number = reinterpret_cast<uint32_t&>(float_number);
    cout << "float_number " << float_number << " is casted to uint32_t " << to_string(uint_number) << endl;

    float casted_back = 0;
    casted_back = reinterpret_cast<float&>(uint_number);
    cout << "uint_number " << uint_number << " is casted back to to float " << to_string(casted_back) << endl;

    return 0;
}