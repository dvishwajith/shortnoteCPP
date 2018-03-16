#include <stdio.h>
#include <pthread.h>


#define THREAD_NUMBER 100

void * inputPrintThread(void *in){
    printf("Print inside thread %d\n",*(int *)in);
    for(int j = 0;j< 0xFFFF ; j++);
    return NULL;
}

int main(){

    pthread_t th[THREAD_NUMBER] ;

    for(int i=0; i <THREAD_NUMBER ; i++){
        if(pthread_create(&th[i],NULL,inputPrintThread,(void *)&i)){
            fprintf(stderr,"Error creating thread %d\n",i);
            return -1;
        }
    }

    for(int i=0; i <THREAD_NUMBER ; i++){
        if(pthread_join(th[i],NULL)){
            fprintf(stderr,"Error joining thread %d\n",i);
            return -1;
        }
    }

    return 0;
}