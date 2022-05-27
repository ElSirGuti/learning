# Calculating Area of Triangle using Arithmetic Operators

def area(s1,s2,s3):
    s = (s1+s2+s3)/2
    a = (s*(s-s1)*s*(s-s2)*s*(s-s3))**0.5
    return a

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

answer = area(a,b,c)
print("The area of the triangle is " + str(answer))