# # Create a new file called day3_bonus.py (or add to your existing file)
# # and build a program that splits a restaurant bill evenly amount a group of frinds

# # Ask the user for the marl price (convert this to a float)
# meal_price = float(input("Enter the Meal Price: "))

# #Ask the user for their desired tip percentage as a whole number (for example, 18 or 20)
# tip_rate = 0.20
# tip_amount = meal_price * tip_rate
# total_bill = meal_price + tip_amount

# # Ask the user how many people are splitting the bill 
# # (convert this to an int, since you cannot have half a person)
# people_count = int(input("How many people are splitting the bill: "))

# tip_whole = round (tip_amount,2)
# total_whole = round (total_bill, 2)
# per_person = round (total_whole / people_count, 2)


# # Calculate the total bill 
# # (meal price + tip) and the amount each person owes
# print (f"20% Tip ${tip_whole}")
# print (f"Total Bill: ${total_whole}")
# print (f"Each person pays: ${per_person: .2f}")

# 1. Get inputs from the user
meal_price = float(input("Enter the meal price: $"))
tip_percent = float(input("Enter tip percentage (e.g., 18, 20): "))
people_count = int(input("How many people are splitting the bill: "))

# 2. Perform calculations
tip_rate = tip_percent / 100
tip_amount = meal_price * tip_rate
total_bill = meal_price + tip_amount
per_person = total_bill / people_count

# 3. Display clean currency results
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total Bill: ${total_bill:.2f}")
print(f"Each person pays: ${per_person:.2f}")




