# Tip Calculator
# Ask the users for numbers (wrapped in float for decimals)
bill_amount = float(input("Enter the restaurant bill subtotal: "))
tip_percent = float (input("Enter the percentage (e.g. 18 or 20): "))

# Ask for a whole number (wrapped in int)
people_count = int(input("How many people are splitting the bill? "))

# Do the math using / or * and round ()
tip_rate = tip_percent/100
tip_amount = round(bill_amount * tip_rate, 2)
total_bill = round(bill_amount + tip_amount, 2)
per_person = round(total_bill/people_count, 2)

# Display results
print("n---Bill Breakdown---")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total with Tip: ${total_bill:.2f}")
print(f"Each Person Pays: ${per_person:.2f}")