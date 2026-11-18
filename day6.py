# • Python Lists. Store multiple values inside square brackets separated by commas, like invoices = [1200, 450, 3100].
# • for Loops. Step through every item in a list automatically using for invoice in invoices:, remembering to indent the code inside the loop by 4 spaces.
# • Accumulator Pattern. Create a counter variable set to 0 before the loop starts (such as total_sales = 0), then add each item to it inside the loop using total_sales += invoice.

# Step-by-Step Day 6 Action Plan

# • Create Your File. Inside your coding-journey folder in VS Code, create a new file named day6.py.
# • Write the Invoice Loop Script. Create a list of invoice amounts, loop through them to calculate the combined pre-tax sales and total NYC sales tax (8.875%), and print a clean summary.
# • Push to GitHub. When your script runs cleanly, practice your 3-command Git workflow (git add ., git commit -m "Complete Day 6", git push) to back it up online.

# day6.py -Batch Invoice & Sales Tax Calculator

invoices = [1200, 3100, 875.50, 2400]
tax_rate = 0.08875

total_sales = 0
total_tax = 0

# Loop through each invoice in the list
for invoice in invoices:
    tax = invoice * tax_rate
    total_sales += invoice
    total_tax += tax
    print(f"Invoice: ${invoice:,.2f} | Tax: ${tax:,.2f}")

# Print final batch totals after the loop finishes
print("\n---Batch Summary---")
print(f"Invoices processed: {len(invoices)}")
print(f"Total Pre-tax Sales: ${total_sales: ,.2f}")
print(f"Total Tax Collected: ${total_tax:,.2f}")
print(f"Grand Total: ${total_sales + total_tax:,.2f}")