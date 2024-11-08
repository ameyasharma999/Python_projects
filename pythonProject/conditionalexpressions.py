# a one line shortcut for the if else statement (ternary operator)
# Print or assign one of the two values based on a condition
# X if condition else Y



num = 5
a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"



print("Positive" if num > 0 else "NEGATIVE")
RESULT = "even" if num % 2 == 0 else "odd"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "hot" if temperature > 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "limited access"
print(min_num)


print(RESULT)
print(status)
print(weather)
print(access_level)
