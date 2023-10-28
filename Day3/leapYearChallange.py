year = int(input("Enter Year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("It's not a leap year")
    else:
        print("It's a leap year")
else:
    print("It's not a leap year")
