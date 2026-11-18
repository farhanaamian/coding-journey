# Extra Practice 1
quarterly_sales1 = float(input("Enter quarterly taxable sales for 1st Practice: $"))

if quarterly_sales1 >3000000:
    print("Monthly Filers")

else:
    print("Quarterly Filers")

# Extra Practice 2
quarterly_sales2 = float(input("Enter quarterly taxable sales for 2nd Practice: $"))

if quarterly_sales2 >= 300000:
    print("Monthly Filers")

elif quarterly_sales2 >=3000:
    print ("Quarterly Filers")

else:
    print ("Annual Filers")

# Extra Practice 3
# TITLE: Sales Tax Filer Frequency Checker
# Ask for input and clean up common formatiin ($ or commas)--
# use .strip() command to remove extra space, tabs or line breaks

raw_input = input("Enter quarterly taxable sales for 3rd Practice: $")
cleaned_input = raw_input.replace("$","").replace(",","").strip()
quarterly_sales3 = float(cleaned_input)

# 2. Check filing status using if/elif/else
if quarterly_sales3 <0:
    print ("Invalid Amount. Sales cannot be negative")

elif quarterly_sales3 >= 300000:
    print("Filling Status: Monthly Filer")
    print("Reason: Quarterly taxable receipts are $300,000 or more")

elif quarterly_sales3 >3000:
    print("Filling Status: Quarterly Filer")
    print("Reason: Quarterly taxable receipts are under $300,000.")

else:
    print("Filling Status: Annual Filer (if eligible)")
    print("Reason: Total tax due is minimal ($3,000 or less in receipts)")