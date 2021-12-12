#!/usr/bin/env python3


def solveKnapsack(weights, prices, capacity, index, memo):
  # base case of when we have run out of capacity or objects
  if capacity <= 0 or index >= len(weights): 
    return 0
  # check for solution in memo table
  if (capacity, index) in memo: 
    return memo[(capacity, index)]
  # if weight at index-th position is greater than capacity, skip this object
  if weights[index] > capacity: 
    # store result in memo table
    memo[(capacity, index)] = solveKnapsack(weights, prices, capacity, index + 1, memo) 
    return memo[(capacity, index)] 
  # recursive call, either we can include the index-th object or we cannot, we check both possibilities and return the most optimal one using max
  memo[(capacity, index)] = max(prices[index]+solveKnapsack(weights, prices, capacity - weights[index], index+1, memo),
        solveKnapsack(weights, prices, capacity, index + 1, memo)) 
  return memo[(capacity, index)]

def knapsack(weights, prices, capacity):
  # create a memo dictionary
  memo = {} 
  return solveKnapsack(weights, prices, capacity, 0, memo)

print(knapsack([2,1,1,3], [2,8,1,10], 4))