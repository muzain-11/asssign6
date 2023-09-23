
count = 0
total_sum = 0


print("Input some integers to calculate their sum and average. Input 0 to exit.")


while True:
    number = int(input())
    
    if number == 0:
        break
 
    count += 1
    total_sum += number

average = total_sum / count

print("Average and Sum of the above numbers are:", average, total_sum)
