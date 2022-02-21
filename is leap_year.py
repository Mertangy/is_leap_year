def is_leap_year(year):
    """Given year as an integer the functions prints if its a leap year or not.A leap year is exactly divisible by 4
    except for century years (years ending with 00). The century year is a leap year only if it is perfectly
    divisible by 400 """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a leap year")


# driver code
while True:
    user_input = input("Enter a year to check,Q to quit: ")
    try:
        year = int(user_input)
        is_leap_year(year)
    except ValueError:
        if user_input.lower() == 'q':
            print("Good bye!")
            break
        print("Please enter a valid integer year.")
