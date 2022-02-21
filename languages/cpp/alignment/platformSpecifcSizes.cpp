
#include <stdio.h>

int main()
{
    printf("sizeof(unsigned long) = %lu\n",sizeof(unsigned long));
    printf("sizeof(unsigned long long) = %lu\n",sizeof(unsigned long long));

    return 0;
}

//(long is guranteed to be at least 32bit)
//(long long is guaranteeed to be at least 64 bit)
// ( avoid using long, since it is indeterminate for multiple platforms.)
// (using long long is fine because it is 64 bit guranteed)

/* In 32bit prcessors  
sizeof(unsigned long) = 4           
sizeof(unsigned long long) = 8
*/

/* In 64bit prcessors  
sizeof(unsigned long) = 8
sizeof(unsigned long long) = 8
*/



