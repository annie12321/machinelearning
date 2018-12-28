import datetime

def printmorning():
    print("Good Morning!")

today = datetime.datetime.today()
name = "Annie"
age = 14

print("My name is %s and I am %d years old." % (name, age))

print("Today is ", today)
print("Today is ", today.strftime("%A"))

printmorning()


