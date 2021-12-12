#!/usr/bin/env python3


class CounterClass:
    ' counter to demo data hiding'
    __secret_counter = 0
    
    def __init__(self):
        CounterClass.__secret_counter = CounterClass.__secret_counter + 1
        print("CounterClass.__secret_counter ", CounterClass.__secret_counter)


if __name__ == "__main__":
    CountDemo = CounterClass()
    CountDemo2 = CounterClass()