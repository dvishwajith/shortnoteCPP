#include <stdio.h>
#include <pthread.h>

int i = 0;
pthread_mutex_t lock;

void * justForLoopAndPrint(){
    pthread_mutex_lock(&lock);
    i++;
    printf("starting justForLoopAndPrint thread %d\n",i);
    for(int j = 0;j< 0xFFFF ; j++);
    printf("stoppping justForLoopAndPrint thread %d\n",i);
    pthread_mutex_unlock(&lock);
    return NULL;
}

int main(){

    if(pthread_mutex_init(&lock,NULL)){
        fprintf(stderr,"Mutex init failed\n");
    }

    pthread_t th_1 ;
    if(pthread_create(&th_1,NULL,(void* (*)(void*))justForLoopAndPrint,NULL)){
        fprintf(stderr,"Error creating thread\n");
        return -1;
    }
    pthread_t th_2 ;
    if(pthread_create(&th_2,NULL,(void* (*)(void*))justForLoopAndPrint,NULL)){
        fprintf(stderr,"Error creating thread\n");
        return -1;
    }

    if(pthread_join(th_1,NULL)){
        fprintf(stderr,"Error joining thread\n");
        return -1;       
    }
    if(pthread_join(th_2,NULL)){
        fprintf(stderr,"Error joining thread\n");
        return -1;       
    }

    pthread_mutex_destroy(&lock);
    return 0;
}