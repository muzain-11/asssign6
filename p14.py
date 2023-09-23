
numbers = [24, 50, 29]


for number in numbers:
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    print()
