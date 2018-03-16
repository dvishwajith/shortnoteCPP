#include <stdio.h>
#include <pthread.h>
#include <unistd.h>


#define THREAD_NUMBER 100

void * inputPrintThread(void *in){
    sleep(1);
    printf("Print inside thread %d\n",*((int *)in));
    return NULL;
}

int main(){

    pthread_t th[THREAD_NUMBER] ;
    int id[THREAD_NUMBER];
    int i=0;
    for( i=0; i <THREAD_NUMBER ; i++){
        id[i] = i;
        printf("In main: creating thread %d\n", i);
        if(pthread_create(&th[i],NULL,inputPrintThread, &id[i]) ){
            fprintf(stderr,"Error creating thread %d\n",i);
            return -1;
        }

        printf("In main:Done  creating thread %d\n", i);        
        
    }

    for(int i=0; i <THREAD_NUMBER ; i++){
        if(pthread_join(th[i],NULL)){
            fprintf(stderr,"Error joining thread %d\n",i);
            return -1;
        }
    }

    return 0;
}