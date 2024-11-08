# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Builtin

# fn can't see inside of other fn
def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()



# enclosed = fn within fn



def func1():
    x = 1
    print(x)

    def func2():
        x = 2 # if this is not available, py will use the enclosed version
        print(x)
    func2()


func1()


x = 3 # global scope



from math import e

def func1():
    print(e)

e = 3

func1()



print(e)
# variables can share the same name as long as they are in different scopes