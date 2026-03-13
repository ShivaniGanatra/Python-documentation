import math


print("a value")
print(input("ask for a value"))

print("value".upper())

print(abs(-1))
print(max(10,5))
print(min(0,1))
print(len('test'))


def calculateHypotenuseLenth(a,b):
    cSquared = (a * a) + (b * b)
    return math.sqrt(cSquared)

print(calculateHypotenuseLenth(3,4))

side_a = int(input("the width of a triangle: "))
side_b = int(input("the height of a triangle: "))
hypotenuse = (side_a ** 2 + pow(side_b,2)) ** 1/2
print("The hypotenuse is: ", hypotenuse)
