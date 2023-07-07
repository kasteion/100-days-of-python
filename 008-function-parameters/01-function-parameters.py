# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#   for i in range(3):
#     print("Hello")

# greet()

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How are you doing {name}")
#   print("Isn't the weather nice today?")

# greet_with_name("Fredy")
# greet_with_name("Jack Bauer")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Fredy", "Guatemala")
greet_with(location="London", name="Angela")