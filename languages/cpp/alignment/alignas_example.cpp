// alignas_alignof.cpp
// compile with: cl /EHsc alignas_alignof.cpp
#include <iostream>

struct alignas(16) Bar
{
    int i;       // 4 bytes
    int n;      // 4 bytes
    alignas(4) char arr[3];  // This wull make sure that arr will stat at a 4 byte boundary
    short s;          // 2 bytes
};

struct alignas(4) Bar_2
{
    int i;       // 4 bytes
    int n;      // 4 bytes
    alignas(4) char arr[3];
    short s;          // 2 bytes
};

struct alignas(4) Bar_3
{
    int i;       // 4 bytes
    int n;      // 4 bytes
    alignas(4) char arr[3];
    char s;          // 1 byte
};

struct alignas(16) Bar_4
{
    int i;       // 4 bytes
    int n;      // 4 bytes
    char arr[3];  // no allignment
    short s;          // 2 bytes
};

struct Bar_5
{
    int i;       // 4 bytes
    int n;      // 4 bytes
    char arr[3];  // no allignment
    short s;          // 2 bytes
};

int main()
{
   std::cout << " alignof(Bar) " <<  alignof(Bar) << " sizeof(Bar) " << sizeof(Bar) << std::endl; // output: 16  // because "struct alignas(16)" size should be a multiple of 16
   std::cout << " alignof(Bar_2) " <<  alignof(Bar_2) << " sizeof(Bar_2) " << sizeof(Bar_2) << std::endl; // output: 16  // because "struct alignas(4)" size should be a multiple of 4
   std::cout << " alignof(Bar_3) " <<  alignof(Bar_3) << " sizeof(Bar_3) " << sizeof(Bar_3) << std::endl; // output: 12  // because "struct alignas(4)" size should be a multiple of 4
   std::cout << " alignof(Bar_4) " <<  alignof(Bar_4) << " sizeof(Bar_4) " << sizeof(Bar_4) << std::endl; // output: 16  // because "struct alignas(16)" size should be a multiple of 16
   std::cout << " alignof(Bar_5) " <<  alignof(Bar_5) << " sizeof(Bar_5) " << sizeof(Bar_5) << std::endl; // output: 16  // because max variable size is 4 byte. Whole strucutre will be alignas(4)
}