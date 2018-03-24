#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char const *argv[]) {
  int fd ;
  char * myfifo = "~/myfifo";

  mkfifo(myfifo,0666);
  fd = open(myfifo, O_WRONLY);
  write(fd,"hi,write",sizeof("hi,write"));
  close(fd);

  unlink(myfifo);
  return 0;
}
