programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}
print("---")
print(programming_dictionary["Bug"])
print("---")
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
print("---")
for k, v in programming_dictionary.items():
  print(f"{k}: {v}")
print("---")
travel_log = {
  "France": { "cities_visited": ["Paris", "Lille", "Dijon"]},
  "Germany": ["Berlin", "Hamburg", "Stuttgard"],
}
print(travel_log)