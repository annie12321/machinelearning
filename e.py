import math

n = 100000
apr = 1.0/n
yr = range(1, n+1)
i = 1.0

for y in yr :
    i += apr * i
    print("After year %d, you have %f dollars." % (y, i))

print("math.e = %f" % math.e)