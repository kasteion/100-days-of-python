# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

# print("You have %d days, %d weeks, and %d months left." % (days_left, weeks_left, months_left))
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
