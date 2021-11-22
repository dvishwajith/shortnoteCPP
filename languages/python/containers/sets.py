#!/usr/bin/env python3

set = {1, "apple", 5.5, True, False, False, "1", "apple"}
print(set)

set.add("orange")
set.add("apple")
print(set)
set.remove("orange")
print(set)

set_2 = {True, "blue", "red" , 4.5}

# union create new set with two sets
set3_union = set.union(set_2)
print(set3_union)

#update can insert new element to the ecisting set
set_4 = {"yellow", "green", True, 4.5}
set.update(set_4)
print(set)

print("""
Set functions

def difference(self, *s: Iterable[Any]) -> Set[_T]: ...                        reuturns CURRENT_SET - COMPAIRING_SET  ( Removes intersetions between CURRENT and COMPAIRING)
def difference_update(self, *s: Iterable[Any]) -> None: ...                    updates  CURRENT_SET to CURRENT_SET - COMPAIRING_SET  ( Removes intersetions between CURRENT and COMPAIRING)
def discard(self, __element: _T) -> None: ...
def intersection(self, *s: Iterable[Any]) -> Set[_T]: ...
def intersection_update(self, *s: Iterable[Any]) -> None: ...
def isdisjoint(self, __s: Iterable[Any]) -> bool: ...                           #if no common elements disjoint tru
def issubset(self, __s: Iterable[Any]) -> bool: ...
def issuperset(self, __s: Iterable[Any]) -> bool: ...
def pop(self) -> _T: ...
def remove(self, __element: _T) -> None: ...
def symmetric_difference(self, __s: Iterable[_T]) -> Set[_T]: ...
def symmetric_difference_update(self, __s: Iterable[_T]) -> None: ...
def union(self, *s: Iterable[_S]) -> Set[_T | _S]: ...
def update(self, *s: Iterable[_T]) -> None: ...

""")

set_diff_set_2_4 =  set_2.difference(set_4)  # This gives    SET_2 - SET4  ( Removes intersetions between SET_2 and SET_4)
print(set_diff_set_2_4)
