
count = 0
total_sum = 0
product = 1


print("Enter integers. Press 'q' to quit.")

while True:
    number = input("Enter a number: ")
    
    if number.lower() == 'q':
        break
    
    number = int(number)
  
    count += 1
    total_sum += number
    product *= number

average = total_sum / count

print("Average:", average)
print("Product:", product)
