# Define a class to represent items with profit and weight
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Main function to solve the fractional knapsack problem


def fractionalKnapsack(W, arr):
    # Sort the list of items based on the profit-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    # Initialize the final value to 0
    finalvalue = 0.0

    # Loop through all the items in the sorted list
    for item in arr:
        # If adding the entire item won't exceed the knapsack capacity (W),
        # add the entire item and update the capacity and final value
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        # If adding the entire item would exceed the capacity, add a fraction of it
        else:
            finalvalue += item.profit * W / item.weight
            break  # Stop adding items since the knapsack is full

    # Return the final value in the knapsack
    return finalvalue


# Driver code
if __name__ == "__main__":
    W = 50  # Knapsack capacity
    # List of items with their profits and weights
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

    # Call the fractionalKnapsack function to find the maximum value
    max_val = fractionalKnapsack(W, arr)
    print(max_val)  # Print the maximum value that can be achieved in the knapsack
