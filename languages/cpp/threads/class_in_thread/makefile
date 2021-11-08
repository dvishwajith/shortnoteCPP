##############################################################################
# Compiler specifications
# These match the variable names given in /usr/share/lib/make/make.rules
# so that make's generic rules work to compile our files.
# gmake prefers CXX and CXXFLAGS for c++ programs
##############################################################################
# Which compiler should be used

CXX = g++
CC = $(CXX)

all: main

main: main.o
	$(CC) -o  test -pthread main.o

main.o:main.cpp
	$(CC) -c  main.cpp

clean:
	rm -rf *.o
	rm -rf test