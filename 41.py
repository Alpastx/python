import calendar 
def display(y,m):
    print(calendar.month(y,m))
y = int(input("Enter year: "))
m = int(input("Enter month: "))
display(y,m)