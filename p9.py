
quantity = int(input("Enter the quantity: "))

cost_per_unit = 100
total_cost = quantity * cost_per_unit

if total_cost > 1000:
    discount = 0.1 * total_cost
    total_cost -= discount

print("The total cost is:", total_cost)
