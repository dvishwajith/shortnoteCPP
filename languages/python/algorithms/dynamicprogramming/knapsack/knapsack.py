#!/usr/bin/env python3


class solution():
    def solveKnapsack(self, W, weights, prices):
        return self.ks(W, weights, prices, 0)

    def ks(self, W, weights, prices, i):
        if W < 0 or i == len(weights):
            return 0
        elif W == 0:
            return prices[i]
        else:
            inc_price = self.ks(W-weights[i], weights, prices, i+1) + prices[i] #profit including weight[i]
            exc_price = self.ks(W, weights, prices, i+1)   # Total profit excluding price
            return max(inc_price, exc_price)


print(solveKnapsack(4, [2,1,1,3], [2,8,1,10]))

#you can memoise this usung W (weight limit ) and index 