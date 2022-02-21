#include <stdio.h>

// sizeof(x_) will be a multiple of max variable byte boundary(by default max varialbe size).
// In here its a multiple of 4
typedef struct 
{
   char a;     // 1 byte
   int b;      // 4 bytes
   short c;    // 2 bytes
   char d;     // 1 byte
} x_;

// x_actual_memory_layout Shows x_'s  actual memory layout. This will be done by compiler automatically.
typedef struct 
{
   char a;            // 1 byte
   char _pad0[3];     // padding to put 'b' on 4-byte boundary
   int b;            // 4 bytes
   short c;          // 2 bytes
   char d;           // 1 byte
   char _pad1[1];    // padding to make sizeof(x_) multiple of 4
} x_actual_memory_layout;

// This will induce packed data structure.( AKA one byte boundaries)
// evnethough this uses small memory foot print this can make accessing variable inefficient.
// For example accessing "int b" require two memory accesses
// But this can be avoided by changing the order of variable inside the sturcutre.
#pragma pack(push, 1)
typedef struct 
{
   char a;     // 1 byte
   int b;      // 4 bytes
   short c;    // 2 bytes
   char d;     // 1 byte
} x_1;
#pragma pack(pop)

#pragma pack(push, 1)
typedef struct 
{
   int b;      // 4 bytes
   short c;    // 2 bytes
   char a;     // 1 byte
   char d;     // 1 byte
} x_1_fast;
#pragma pack(pop)

// sizeof(x_) will be a multiple of max variable byte boundary(by default max varialbe size).
// In here its a multiple of 8
typedef struct 
{
   void * b;      // 8 bytes
   char d;     // 1 byte
} y_;


// sizeof(y_16) will be a multiple of max variable byte boundary(by default max varialbe size).
// In here sizeof(y_16) is a multiple of 16 because alignas(16) changed byte boundary to 16. Now max byte boundary is 16.
typedef struct 
{
   alignas(16) void * b;      // 8 bytes
   char d;     // 1 byte
} y_16;

// sizeof(y_16) will be a multiple of max variable byte boundary(by default max varialbe size).
// In here sizeof(y_16) is a multiple of 16 because alignas(16) changed byte boundary to 16. Now max byte boundary is 16.
typedef struct 
{
    alignas(16) void * b;      // 8 bytes
    void *c;    // 8 bytes
} y_16_exemple_2;

// sizeof(y_16) will be a multiple of max variable byte boundary(by default max varialbe size).
// In here sizeof(y_16) is a multiple of 16 because alignas(16) changed byte boundary to 16. Now max byte boundary is 16.
typedef struct 
{
    alignas(16) void * b;      // 8 bytes
    void *c;    // 8 bytes
    char d;     // 1 byte
} y_16_exemple_3;

int main()
{
    printf("sizeof(unsigned long) %lu\n",sizeof(unsigned long));
    printf("sizeof(x_) %lu\n", sizeof(x_));
    printf("sizeof(x_1) %lu\n", sizeof(x_1));

    printf("sizeof(y_) %lu\n", sizeof(y_));
    printf("sizeof(y_16_exemple_2) %lu\n", sizeof(y_16_exemple_2));
    printf("sizeof(y_16_exemple_3) %lu\n", sizeof(y_16_exemple_3));

    return 0;
}



