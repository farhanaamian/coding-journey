# 1. Get inputs from the user
client_name = input("Enter Client's Name: ")
invoice_amount = float (input ("Enter Invoice Amount: $"))
days_ovedue = int(input("Enter days overdue: "))

# 2. Check aging status and calculate late fees
if days_ovedue <= 0:
    status = "On Time"
    late_fee = 0

elif days_ovedue <= 30:
    status = "1-30 Days late (5% penalty)"
    late_fee = invoice_amount * 0.05

else:
    status = "30+ Days Severly Overdue (10% Penalty +$25 Admin Fee)"
    late_fee = (invoice_amount * 0.10) + 25

# 3. Calculate total and print clean summary
total_due = invoice_amount + late_fee

print (f"Client Name: {client_name}")
print (f"STATUS: {status}")
print (f"ORIGINAL Amount: ${invoice_amount: .2f}")
print (f"LATE Fee: ${late_fee:.2f}")
print (f"TOTAL Due: ${total_due:.2f}")