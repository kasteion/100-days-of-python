# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lucky_one = random.randint(0, len(names)-1)
print(len(names))
print(f"{names[lucky_one]} is going to buy the meal today!")
