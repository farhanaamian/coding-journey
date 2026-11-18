# 1. Ask the user for the employee's hourly wage (convert to a float)
hourly_wage = float(input("Hourly Wage is: $"))
total_hours = float(input("Total hours worked: "))

# 2. Check if they worked overtime (more than 40 hours)

if total_hours <= 40:
    regular_pay = total_hours * hourly_wage
    overtime_pay = 0

else:
    regular_pay = 40 * hourly_wage
    overtime_hours = total_hours-40
    overtime_pay = overtime_hours * hourly_wage * 1.5

# 3. Calculate total gross pay
total_gross = regular_pay + overtime_pay

#4. Print the clean summary
print (f"Regual Pay: ${regular_pay:.2f}")
print (f"Overtime Pay: ${overtime_pay:.2f}")
print (f"Total Gross Pay: ${total_gross:.2f}")