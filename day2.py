#1. Store text in Strings
client_name = "JH Coffee Shop"
filling_period = "November 2026"

#2. Store whole numbers in Integers
receipt_count = 1420   

#3. Store decimal numbers in Floats
gross_sales = 99075.09
tax_rate = 0.08875

#4. Calculate new variables using math
collected_tax = gross_sales * tax_rate
total_proceeds = gross_sales + collected_tax

#5. Print a clean summary using an f-string
print (f"Client: {client_name} {filling_period}")
print (f"total Receipts Processed: {receipt_count}")
print(f"Gross Sales: ${gross_sales:,.2f}")
print (f"NYC Sales Tax Due: ${collected_tax:,.2f}")
print (f"Total Proceeds: ${total_proceeds:,.2f}")