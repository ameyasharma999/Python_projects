import math
#friends = 10

#friends = friends + 1
#friends += 1 # augmented assignment operator
#friends = friends - 2
#friends -= 2
#friends = friends * 3
#friends *= 3
#friends = friends / 2
#friends /= 2
#friends = friends ** 2
#friends **= 2
#remainder = friends % 3 # modulus operator

#print(remainder)
#print(friends)



#x = 3.14
#y = 4
#z = 5

#result = round(x)
#result = abs(y)
#result = pow(y,3)
#result = max(x,y,z)
#result = min(x,y,z)

#print(result)


#x = 9.9

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)

#print(result)

# Exercise 1
radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)} cm")

# Exercise 2
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius,2)

print(f"The area of the circle is {round(area,2)}cm^2")

# Exercise 3
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C = {c}")