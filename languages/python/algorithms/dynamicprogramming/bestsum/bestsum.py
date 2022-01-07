#!/usr/bin/env python3


def bestsum(sum, values=[]):
    if sum is 0:
        return []
    elif sum < 0:
        return None
    else:
        min_sum_len = sum
        min_sum_list = None
        for val in values:
            sum_list = bestsum(sum-val, values)
            if sum_list is not None:
                if len(sum_list) <= min_sum_len:
                    min_sum_len = len(sum_list)
                    min_sum_list = sum_list
                    min_sum_list.append(val)
        return min_sum_list


print("bestsum method 1")
print(bestsum(7, [5,3,4,7]))
print(bestsum(7, [2,4]))
print(bestsum(7, [2,4,1]))
print(bestsum(8, [2,3,5]))




def bestsumMemoised(sum, values=[], mem=None):
    if mem is None:
        mem = {}
    if sum is 0:
        return []
    elif sum < 0:
        return None
    elif sum in mem:
        return mem[sum]
    else:
        min_sum_len = sum
        min_sum_list = None
        for val in values:
            sum_list = bestsumMemoised(sum-val, values, mem)
            if sum_list is not None:
                if len(sum_list) <= min_sum_len:
                    min_sum_len = len(sum_list)
                    min_sum_list = [*sum_list, val]
        mem[sum] = min_sum_list
        return min_sum_list        


print("\nbestsum Memoized 1")
print(bestsumMemoised(7, [5,3,4,7]))
print(bestsumMemoised(7, [2,4]))
print(bestsumMemoised(7, [2,4,1]))
print(bestsumMemoised(8, [2,3,5]))
print(bestsumMemoised(300, [7,14,1]))