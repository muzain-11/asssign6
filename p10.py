
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))


if years_of_service > 5:
  
    bonus_amount = 0.05 * salary
   
    print("Your net bonus amount is:", bonus_amount)
else:
    print("Sorry, you are not eligible for a bonus.")
