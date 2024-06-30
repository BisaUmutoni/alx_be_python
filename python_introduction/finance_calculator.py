#finance calculator
income = int(input("Enter  your monthly income:"))
expenses = int (input("Enter your total monthly expenses:"))

savings = income-expenses

projected_savings = savings * 12 + (savings *12 * 0.05)

print(" Your monthly expenses:", savings)
print("Your projected savings after one year is:", projected_savings)