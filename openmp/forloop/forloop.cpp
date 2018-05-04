#include <iostream>

int main(){

    int a[1000];

    #pragma omp parallel for
    for(int i=0 ; i <1000 ; i++){
        a[i] = 2*i;
        printf("%d %d\n",i,a[i]);
    }

    // for(int i=0 ; i <1000 ; i++){
    //     printf("%d\n",a[i]);
    // }
    printf("This example is embarrassingly parallel, and depends only on the value of i. \n \
     The OpenMP parallel for flag tells the OpenMP system to split this task among its   \n \
     working threads. The threads will each receive a unique and private version of the  \n \
     variable.[15] For instance, with two worker threads, one thread might be handed a   \n \
     version of i that runs from 0 to 4999 while the second gets a version running from \n \
     5000 to 9999.\n");
    return 0 ;
}