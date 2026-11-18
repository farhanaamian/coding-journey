#1 Store text in String
client_name ="Quazi Maksud Hassan INC"
filling_period = "October 2026"

#2 Store whole numbers in Integers
receipt_number = 1014

#3 Store decimal numbers in Floats
gross_sales = 99075.09
tax_rate = 0.08875
exempt_sales = 516

#4 Calculate new variables using math
taxable_sales = gross_sales - exempt_sales
collected_tax = gross_sales * tax_rate
total_proceeds = gross_sales + collected_tax
net_sales_tax = taxable_sales * tax_rate

#5 Print a clean summary using an f-string
print (f"Client: {client_name} Sales Tax Filling Period {filling_period}")
print (f"Total Receipts Processed: {receipt_number}")
print (f"Gross Sales: ${gross_sales:,.2f}")
print (f"NYC Sales Tax Due: ${collected_tax:,.2f}")
print (f"Total Proceeds: ${total_proceeds:,.2f}")
print (f"NET SALES TAX: ${net_sales_tax}")
print (f"GROSS SALE IS: ${gross_sales} for {client_name}")

