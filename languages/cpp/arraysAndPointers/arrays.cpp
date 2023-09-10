#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
    for(int i = 1; i < 10; i++)
    {
        int arr[i];   // variable length arrays are C99 feature. This was not possible before that.
        cout << "address of arr " << arr << " sizeof(arr) " << sizeof(arr) << endl;
    }    
/*
Result 
address of arr 0x7ffcc47f0cb0 sizeof(arr) 4
address of arr 0x7ffcc47f0cb0 sizeof(arr) 8
address of arr 0x7ffcc47f0cb0 sizeof(arr) 12
address of arr 0x7ffcc47f0ca0 sizeof(arr) 16
address of arr 0x7ffcc47f0ca0 sizeof(arr) 20
address of arr 0x7ffcc47f0ca0 sizeof(arr) 24
address of arr 0x7ffcc47f0ca0 sizeof(arr) 28
address of arr 0x7ffcc47f0c90 sizeof(arr) 32
address of arr 0x7ffcc47f0c90 sizeof(arr) 36
*/


    return 0;
}

