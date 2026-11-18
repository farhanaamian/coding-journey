print("Hello, World!")

#Initial balance
account_balance = 1500.00
print (f"Starting Balance: ${account_balance:.2f}")

# Add a client deposit
account_balance = account_balance + 450.50
print (f"After Depost: ${account_balance: .2f}")

#Subsract an office supply expense
account_balance = account_balance-89.99
print (f"Ending Balance: ${account_balance:.2f}")

# combining strings
first_name = "Maria"
last_name = "Gomez"
role = "Tax Preparer"

# Using an f-string (prefer modern method)
badge_label = f"{first_name}{last_name} - {role}"
print (badge_label)

# Spotting Data Type Mistakes
text_number = "100"      #String (wrapped in quotes)
real_number = 100        #Integer (no quotes)
decimal_number = 100.0   #Float (has a decimal)

print (type(text_number))    #Outputs: <class 'str'>
print (type(real_number))    #Outputs: <class 'int'>
print (type(decimal_number)) #Outputs: <class 'float'>