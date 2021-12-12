#!/usr/bin/env python3



class MyNUmbers:
    def __init__(self) -> None:
        pass

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


ExampleNumbers = MyNUmbers()

iter = iter(ExampleNumbers)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

print(
"""
With stop iteration feature
"""
)


class MyNUmbersModified:
    def __init__(self) -> None:
        pass

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


Example2 = MyNUmbersModified()

for i in Example2:
    print(i, end=' ')

print()

#print iterate using  *operator

different_way = [*Example2]
print(different_way)
