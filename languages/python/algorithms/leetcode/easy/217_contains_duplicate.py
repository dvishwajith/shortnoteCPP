def containsDuplicate(nums: list[int]) -> bool:
    table = set()
    for val in nums:
        if val in table:
            return True
        else:
            table.add(val)
    return False

print(containsDuplicate([1,2,3,1]))