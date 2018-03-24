#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char const *argv[]) {
  int fd ;
  char * myfifo = "~/myfifo";
  char buf[1000] ;

  mkfifo(myfifo,0666);
  fd = open(myfifo, O_RDONLY);
  read(fd,buf , sizeof(buf));
  printf("REcieved :%s\n",buf );
  close(fd);

  unlink(myfifo);
  return 0;
}
