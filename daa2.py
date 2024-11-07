class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Calculate value-to-weight ratio

def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value collected in the knapsack
    for item in items:
        if capacity >= item.weight:
            # Take the entire item if possible
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the item that fits
            total_value += item.ratio * capacity
            break  # Knapsack is full

    return total_value

# Example usage
items = [
    Item(60, 10),  # Value = 60, Weight = 10
    Item(100, 20), # Value = 100, Weight = 20
    Item(120, 30)  # Value = 120, Weight = 30
]
capacity = 50
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in the knapsack: {max_value}")
