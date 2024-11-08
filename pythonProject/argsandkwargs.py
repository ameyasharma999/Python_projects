# *args = allows you to pass multiple non-key arguments (tuple)
# **kwargs = allows you to pass multiple keyword arguments (dictionary)
# * unpacking operator


#def add(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total

#print(add(1,2,3,4,5))



#def display_name(*args):
#    for arg in args:
#        print(arg,end=" ")

#display_name("Dr","Spongebob","Harold","Squarepants","III")




#def print_address(**kwargs):
#    for key,value in kwargs.items():
#        print(f"{key}:{value}")


#print_address(street="123 Fake Street",city="Detroit",state="MI",zip="54321")



def shipping_label(*args,**kwargs): # it won't run the other way around

    for arg in args:
        print(arg,end=" ")
    print()

    #for value in kwargs.values():
    #    print(value,end=" ")

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")



shipping_label("Dr","Spongebob","Squarepants","III", street = "123 Fake Street", apt ="100", city="Detroit", state = "MI", zip = "54321")


# you can use if else statements when printing

