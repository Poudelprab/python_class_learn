# WAP that asks the user to enter their first and last names, separated by a single space. 
# The user may enter their names in any case (uppercase, lowercase, or mixed case). 
#your program should 1. use find() to locate the space between the names, 
# 2. use string slicing to extract the first and last names, 
# 3. use capitalize() on each name
#  print Hi followed by the two names

full_name = input("Enter your first and last name (separate it with a single space):")
space_index = full_name.find(" ")
#using string slicing to extract first and last names
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

#Use capitalize() on each name to ensure the first letter is uppercase and the rest are lowercase
first_name = first_name.capitalize()
last_name = last_name.capitalize()

print(f"Hi {first_name} {last_name}")
