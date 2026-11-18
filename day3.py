# Ask the user for business details
client_name = input("Enter Client Business name: ")

# Ask for numbers and convert them to floats (decimals)
total_proceeds =float(input("Enter total sales proceeds (including tax): "))
tax_rate = 0.08875

# # Perform math and round to 2 decimal places
gross_sales = round(total_proceeds/(1+tax_rate), 2)
collected_tax = round (total_proceeds-gross_sales, 2)

# # Print the interactive receipt summary
print ("\n--- NYC Sales Tax Summary---")
print(f"Business: {client_name}")
print(f"Pre-Tax Gross Sales: ${gross_sales:,.2f}")
print(f"Collected Sales Tax: ${collected_tax:,.2f}")