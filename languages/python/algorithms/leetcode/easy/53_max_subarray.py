def maxSubArray(nums: list[int]) -> int:
    max_sum = -10000
    moving_sum = 0
    for i in range(len(nums)):
        moving_sum = max(0, moving_sum)
        moving_sum += nums[i]
        max_sum = max(max_sum, moving_sum)
    return max_sum

    # max_sum = -10000
    # moving_sum = 0
    # for i in range(len(nums)):
    #     if moving_sum + nums[i] >= 0 :
    #         moving_sum += nums[i]
    #     else:
    #         moving_sum = 0
    #     max_sum = max(max_sum, moving_sum)
    # return max_sum

print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

