import math

x = float(input())
y = math.ceil(x ** 5/3 + math.tan(math.radians(x)))
z = int(math.pi ** 2 + math.atan(math.radians(math.sin(math.radians(x)) ** 2)))
print(y)
print(z)
result = math.gcd(y, z)
print(result)









