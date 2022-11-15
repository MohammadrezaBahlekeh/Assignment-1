print("Enter the size of the triangle sides")
X = float(input("X = "))
Y = float(input("Y = "))
Z = float(input("Z = "))

if Z<X+Y and X<Z+Y and Y<X+Z:
    print("it's possible")
else:
    print("it's not possible")