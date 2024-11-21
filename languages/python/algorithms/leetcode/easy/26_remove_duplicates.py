
# use two pointers
def removeDuplicates(nums: list[int]) -> int:
    uniq_index = 0
    current_val = -101
    for i in range(len(nums)):
        if nums[i] > current_val:
            current_val = nums[i]
            nums[uniq_index] = nums[i]
            uniq_index += 1
    return uniq_index

      
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))