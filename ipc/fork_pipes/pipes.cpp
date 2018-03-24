#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

/** FORK PROCESS
 * System call fork() is used to create processes. It takes no arguments and returns 
 * a process ID. The purpose of fork() is to create a new process, which becomes the 
 * child process of the caller. After a new child process is created, both processes 
 * will execute the next instruction following the fork() system call. Therefore, we 
 * have to distinguish the parent from the child. This can be done by testing the 
 * returned value of fork()
 * 
 */

/**Pipe
 * Here a if we weite to fd[0] we can read from fd[1] vise verca
 */ 

int main(int argc, char const *argv[]) {
  int     fd[2];
  pid_t   childpid;
  char    string2[] = "Hello, world test!\n";
  char    readbuffer[80];
  pipe(fd);
  if ( (childpid = fork()) == -1 ) {
    perror("fork");
    exit(1);
  }

  //Two processes start working conccurently from here onwards

  //child process
  if (childpid == 0){ // child process because return value zero
    close(fd[0]);
    printf("Sending from process %d string: %s\n", childpid, string2 );
    write(fd[1],string2 ,strlen(string2)+1);

    exit(0);
  } 

  //parent process 
  else { // parent process
    close(fd[1]);

    read(fd[0],readbuffer,sizeof(readbuffer));

    printf("Recieved from process %d string: %s\n", childpid, readbuffer );
  }

  return 0;
}


