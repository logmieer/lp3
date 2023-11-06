# Dynamic programming function to solve the 0-1 Knapsack problem
# W: Maximum weight capacity of the knapsack
# wt: List of weights of items
# val: List of values of items
# n: Number of items
def knapSack(W, wt, val, n):
    # Create a 2D DP table to store results of subproblems
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill the DP table using a bottom-up approach
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                # Base case: no items or no remaining capacity
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                # If the weight of the current item is less than or equal to the remaining capacity
                # Calculate the maximum value by either including or excluding the current item
                dp[i][w] = max(val[i - 1] + dp[i - 1]
                               [w - wt[i - 1]], dp[i - 1][w])
            else:
                # If the weight of the current item is greater than the remaining capacity, exclude the item
                dp[i][w] = dp[i - 1][w]

    # The result is stored in dp[n][W], representing the maximum value that can be obtained
    return dp[n][W]


if __name__ == '__main__':
    profit = [160, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)

    # Call the knapSack function to find the maximum value
    result = knapSack(W, weight, profit, n)

    # Print the maximum value that can be obtained in the knapsack
    print("Maximum value:", result)
