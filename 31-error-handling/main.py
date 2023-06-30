# Catch Exceptions
# try:
#    Something that might cause an exception
# except:
#    If there was an exception
# else:
#    If there were no exceptions
# finally:
#    No matter what happened we execute this code

# FileNotFoundError
# with open("no_file.txt") as file:
#     file.read()

# KeyError
# a_dict = { "key": "value"}
# value = a_dict["non_existent_key"]

# IndexError
# a_list = [1, 2, 3]
# value = a_list[3]

# TypeError
# a_text = "abc"
# value = a_text + 1

try:
    file = open("no_file.txt")
    a_dict = {"key": "value"}
    # value = a_dict["non_existent_key"]
    value = a_dict["key"]
except FileNotFoundError:
    file = open("no_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")

# raise TypeError("This is an error that i made up.")
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

# JSON built in
# import json
# Write: json.dump()
# Read: json.load()
# Update: json.update()

