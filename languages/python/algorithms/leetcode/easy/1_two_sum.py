def twoSum(nums: list[int], target: int) -> list[int]:
    ###### Method 2 #############

    # sorted_num = sorted(nums)
    # low_index = 0
    # high_index = len(sorted_num) - 1
    # for i in range(len(sorted_num)):
    #     low_index = i
    #     expected_val = target - sorted_num[low_index]
    #     while sorted_num[high_index] > expected_val :
    #         high_index -= 1
    #     if sorted_num[high_index] == expected_val :
    #         break
    # first_val = sorted_num[low_index]
    # second_val = target - first_val

    # result = []  
    # for i in range(len(nums)):
    #     if nums[i] == first_val or nums[i] == second_val:
    #         result.append(i)
    # return result

    ###### Method 3 #############

    check_exist = {}
    # check_exist = set(nums)
    for val in nums:
        if val in check_exist:
            check_exist[val] += 1
        else:
            check_exist[val] = 1
    # val_one = 0
    for val in nums:
        if (target - val) in check_exist:
            if target - val == val :
                if check_exist[val] <= 1:
                    continue
            val_one = val
            break
    
    result = []
    val_two = target - val_one
    for i in range(len(nums)):
        if nums[i] == val_one or nums[i] == val_two:
            result.append(i)
    return result 

print(twoSum([2,7,11,15], 9))