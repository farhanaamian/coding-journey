# # Ask the user for a number and convert it to a decimal (float)
# meal_price = float (input("Enter the price of the meal: $"))
# print("You entered: ", meal_price)

# # 1. Get the meal price from the user
# meal_price = float(input("Enter the meal price: $"))


# # 2. Calculate the 20% tip and total bill
# tip_rate = 0.20
# tip_amount = meal_price * tip_rate
# total_bill = meal_price + tip_amount

# # 3. Round the numbers to 2 decimal places
# tip_rounded = round(tip_amount, 2)
# total_rounded = round (total_bill, 2)

# # 4. Display the results cleanly using f-string
# print (f"20% Tip: ${tip_rounded}")
# print (f"Total Bill: ${total_rounded}")

# 1. Get the meal price from the user
meal_price = float(input("Enter the meal price: $"))

# 2. Calculate the 20% tip, people count and total bill
tip_rate = 0.20
tip_amount = meal_price * tip_rate
total_bill = meal_price + tip_amount
people_count = int(input("How many people are splitting the bill: $"))

# 3. Round the numbers to 2 decimal places
tip_rounded = round(tip_amount, 2)
total_rounded = round (total_bill, 2)
per_person = round (total_rounded /people_count, 2)

# 4. Display the results cleanly using f-string
print (f"20% Tip: ${tip_rounded}")
print (f"Total Bill: ${total_rounded}")
print(f"Each person Pays: ${per_person: .2f}")

