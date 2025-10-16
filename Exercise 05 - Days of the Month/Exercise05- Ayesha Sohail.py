months_days= {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31, 
}

#Ask the user for the month number
month= int (input("Enter the month number (1-12): "))

#Check if the input is valid and display the number of days 
if month in months_days:
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        if leap == "yes": #Check if it is a leap year in case of February
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {months_days[month]} days.")
else:
    print("Invalid month number! The number should be between 1 and 12.")
