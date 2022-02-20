#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
    char str1[] = "start stop";
    char str2[] = "start stop";

    memmove(str1, str1+6, sizeof(char)*4);
    memcpy(str2, str2+6, sizeof(char)*4);
    
    printf("memmoved str1  '%s'\n", str1);
    printf("memcpyied str2  '%s'\n", str2);


    char str3[] = "start stop";
    char str4[] = "start stop";

    memmove(str3, str3+2, sizeof(char)*5);
    memcpy(str4, str4+2, sizeof(char)*5);
    
    printf("memmoved str3  '%s'\n", str3);
    printf("memcpyied str4  '%s'\n", str4);

    char str5[] = "start stop";
    char str6[] = "start stop";

    memmove(str5+2, str5, sizeof(char)*5);
    memcpy(str6+2, str6, sizeof(char)*5);
    
    printf("memmoved str5  '%s'\n", str5);
    printf("memcpyied str6  '%s'\n", str6);

    return 0;
}

/*
Result with O3 optimisation 

memmoved str1  'stopt stop'
memcpyied str2  'stopt stop'
memmoved str3  'art s stop'
memcpyied str4  'art s stop'
memmoved str5  'ststarttop'     // memmove and memcopy will be different with 03 optimsation
memcpyied str6  'ststaratop'    // memcpy messed up with O3 optimisation when there are overlaps

*/


/*
Result without O3 optimisation give same results

memmoved str1  'stopt stop'
memcpyied str2  'stopt stop'
memmoved str3  'art s stop'
memcpyied str4  'art s stop'
memmoved str5  'ststarttop'     
memcpyied str6  'ststarttop'    

*/