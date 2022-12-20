check_year = input("Which Year would you like to check? ")

check_year_as_int = int(check_year)

if int(check_year) % 4 == 0:
    print("Leap year.")
    exit()
    if int(check_year) % 100 == 0:
        print("Leap year.")
        exit()
    if int(check_year) % 400 == 0:
        print("Leap year.")
        exit()

if int(check_year) % 4 != 0:
    print("Not leap year.")
    exit()
    if int(check_year) % 100 != 0:
        print("Not leap year.")
        exit()
    if int(check_year) % 400 != 0:
        print("Not leap year.")
        exit()
