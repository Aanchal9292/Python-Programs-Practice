Year=int(input("enter the year : "))
if(Year%4==0|Year%100==0):
    print("given Year is leap year")
else:
    print("given year is not leap year")