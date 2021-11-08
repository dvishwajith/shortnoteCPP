#include <stdio.h>
#include <pthread.h>



class aClass {
public:
    void add(int a,int b, int *c){
        *c = a+b;
    }
};

void * aclassInstancevoid(void *){
    aClass obj;
    int a,b,c;
    a=1,b=10,c=5;
    obj.add(a,b,&c);
    printf ("test aclassInstancevoid %d\n",c);
    
}

int main (){

    /* this variable is our reference to the second thread */
    pthread_t thread;

    /* create a second thread which executes inc_x(&x) */
    if(pthread_create(&thread, NULL, aclassInstancevoid, NULL)) {

    fprintf(stderr, "Error creating thread\n");
    return 1;

    }
   
    /* wait for the second thread to finish */
    if(pthread_join(thread, NULL)) {

    fprintf(stderr, "Error joining thread\n");
    return 2;

    }

    /* this variable is our reference to the second thread */
    pthread_t thread2;

    /* create a second thread which executes inc_x(&x) */
    if(pthread_create(&thread2, NULL, aclassInstancevoid, NULL)) {

    fprintf(stderr, "Error creating thread\n");
    return 1;

    }
    
    /* wait for the second thread to finish */
    if(pthread_join(thread2, NULL)) {

    fprintf(stderr, "Error joining thread\n");
    return 2;

    }

    
    return 0;
}