def test_arguments_int(a):
    print("Before increment, id(a) = %d" % id(a))
    a += 1
    print("After increment, id(a) = %d" % id(a))


num = 9

print("id(num) = %d" % id(num))
print("Before call function, num = %d" % num)
test_arguments_int(num)
print("id(num) = %d" % id(num))
print("After call function, num = %d" % num)


def test_arguments_list(b):
    print("Before increment, id(b) = %d" % id(b))
    b.append("Good Morning")
    print("After increment, id(b) = %d" % id(b))


mylist = ["apple", 67]

print("id(mylist) = %d" % id(mylist))
print("Before call function, my list = ", mylist)
test_arguments_list(mylist)
print("id(mylist) = %d" % id(mylist))
print("After call function, my list = ", mylist)
