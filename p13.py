
total_sum = 0

print("Enter 10 integers:")

for _ in range(10):
    number = int(input())
    total_sum += number

average = total_sum / 10

print("The average of these numbers is:", average)
