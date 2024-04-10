import math as m 
def cal(r):
    area = m.pi * r ** 2
    circumference = 2 * m.pi * r
    print("Area:",area)
    print("Circumference:",circumference)
r = float(input("Enter the radius of the circle: "))
print(cal(r))

