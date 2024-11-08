# module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program into reusable separate files



#print(help('modules'))
#print(help('math'))




#import math
#import math as m
#from math import pi # this can create conflicts # we always use the latest version
# prefix the module name
#print(m.pi)
#print(pi)

import modulemain

result = modulemain.pi
result = modulemain.square(3)
result = modulemain.cube(3)
result = modulemain.circumference(3)
result = modulemain.area(3)


print(result)