
list1 = [2, 4, 6, 8, 10]
list2 = [3, 5, 7, 9]


divisors = [4, 6, 8, 10, 3, 5, 7, 9]
divisible_lists = [[] for _ in range(len(divisors))]

for number in list1 + list2:
    for i, divisor in enumerate(divisors):
        if number % divisor == 0:
            divisible_lists[i].append(number)

# Print the new lists
for i, divisor in enumerate(divisors):
    print(f"Numbers divisible by {divisor}: {divisible_lists[i]}")
