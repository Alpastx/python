def ifleap(N):
    if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
         print("Leap year")
    else:
         print("Not a leap year")
         
         
N = int(input("Enter the year: "))
print(ifleap(N))