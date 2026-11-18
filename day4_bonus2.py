# 1. Ask the user for the expense description (keep this as text using plain input(), no float() needed).
expense_description = (input("Expense Description: "))
expense_amount = float (input("Enter Expense Amount: $"))

# 2. Route the expense and set the audit fee
if expense_amount <= 100:
    staus = "Auto-Approved"
    audit_fee = 0

elif expense_amount <=1000:
    status = "Manager Approval Required"
    audit_fee = 0

else: 
    status = "Executive Review Required"
    audit_fee = expense_amount * 0.02

# 3. Calculate total cost and display clean summary
total_cost = expense_amount + audit_fee

print ("---Expense Report---")
print (f"Item: {expense_description}")
print (f"Status: {status}")
print (f"Audit Fee: ${audit_fee: .2f}")
print (f"Total Cost: ${total_cost: .2f}")
