# logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be true
# and = both the conditions must be true
# not = inverts the condition (not False, not True)



#temp = -5
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
#    print("The outdoor event is cancelled")
#else:
#    print("The outdoor event is still scheduled")




temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot outside!")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif temp < 28 and temp >0 and is_sunny: # this is chained comparision
    print("It is Warm outside")
    print("It is Sunny")



temp = 20
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It is Hot outside!")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif temp < 28 and temp > 0 and not is_sunny: # this is chained comparision
    print("It is Warm outside")
    print("It is cloudy")


