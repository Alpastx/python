import math as m 

def cal(r,h):
    print("surface Area:",2*m.pi*r*(r+h))
    print("volume:",m.pi * r ** 2 * h)
    print("Area:",2*m.pi*r*h)

r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))
cal(r,h)
