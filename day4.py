# 1. Ask the user for the business's quarterly taxable sales
quarterly_sales = float(input("Enter quarterly taxable sales: $"))

# 2. Check the sales threshold using if/elif/else
if quarterly_sales >= 300000:
    print ("Status: Monthly Filer (Part-Quarterly)")
    print ("Action: Must file returns every month")

elif quarterly_sales > 0:
    print ("Status: Quarterly Filer")
    print ("Action: Standard quarterly filling applies")

else: 
    print ("Status: Zero Return/Inactive")
    print ("Action: Verify if business had any taxable activity") 