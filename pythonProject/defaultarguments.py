# default arguments = a default value for certain parameters
# default is used when that argument is omitted
# make your fn more flexible, reduces # of arguments
# 1. positional, 2.DEFAULT, 3.Keyword, 4. Arbitrary


def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1-discount) * (1+tax)

#print(net_price(500,))
#print(net_price(500,0.1))
# we will use whatever is passed in
#print(net_price(500,0.1,0))

import time

def count(end, start = 0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE")

count(30,15)
# default arguments should be after any positional arguments