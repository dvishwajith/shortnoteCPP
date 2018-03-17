#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
/*
semaphores have a synchronized counter and mutex's are just binary (true / false).

A semaphore is often used as a definitive mechanism for answering how many elements 
of a resource are in use -- e.g., an object that represents n worker threads might 
use a semaphore to count how many worker threads are available.
*/


int i = 0;
sem_t sem_lock;

void * justForLoopAndPrint(){
    sem_wait(&sem_lock);
    i++;
    printf("starting justForLoopAndPrint thread %d\n",i);
    for(int j = 0;j< 0xFFFF ; j++);
    printf("stoppping justForLoopAndPrint thread %d\n",i);
    sem_post(&sem_lock);
    return NULL;
}

int main(){

    if( sem_init(&sem_lock,0,1) ){
        fprintf(stderr,"Semaphore init failed\n");
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

    sem_destroy(&sem_lock);
    return 0;
}