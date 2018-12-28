a = 10

if a > 5:
    print("a is greater than 5")
elif a > 3:
    print("a is less than 5, but greater than 3")
else:
    print("a is less than 3")

b = [9, 6, 4, 2]

for x in b:
    print(x)

c = True
cnt = 0
while c:
    print("Number %d" % cnt)
    cnt+=1
    if cnt==10:
        c = False