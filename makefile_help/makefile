all: main

main: main.o
	g++ -o  test -pthread main.o

main.o:main.cpp
	g++ -c  main.cpp

clean:
	rm -rf *.o
	rm -rf test