def function1():
    print("my python function!")
    return "hi "

newstring = function1() * 2
print(newstring)

def addfunction1(a, b):
    return a + b

def printname(score, s = "no name"):
    print("The name is %s and the score is %d" % (s, score))
    return

name = "Annie Chen"
printname(1)

c = addfunction1(5, 9)
print("The sum is %d" % c)