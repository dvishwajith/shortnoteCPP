
# This uses Moors Majority vote algorithm
def majorityElement(nums: list[int]) -> int:
    majority_element = 0
    count = 0
    for val in nums:
        if count == 0:
            majority_element = val
            count = 1
        else:
            if majority_element == val:
                count += 1
            else:
                count -= 1
    
    # This part is not needed if majority element is present for sure.
    majority_count = 0
    for val in nums:
        if val == majority_element:
            majority_count += 1
    if majority_count <= len(nums)//2:
        print(f"Error majority_count({majority_count}) and len_nums({len(nums)}), Majority vote does not exist for {nums}")

    return majority_element

print(majorityElement([3,2,3]))

print(majorityElement([4,3,4,4,2,3,4]))

print(majorityElement([1,5,4,4,4,3,2,4,3,4]))