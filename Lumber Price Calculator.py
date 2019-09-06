check = bool(False)
checkFeet = bool(False)
cont = bool(False)
error = bool(False)

while not cont:
    total = 0.0
    print("You will be asked the number of board feet for the purchase and the type of lumber (common or select)")
    feet = (input("Enter number of board feet: "))

    if feet.isdigit():
        checkFeet = True
        feet = int(feet)
        if feet < 1:
            checkFeet = False

    while not checkFeet:
        print("Invalid, try again")
        feet = (input("Enter number of board feet: "))
        if feet.isdigit():
            checkFeet = True
            feet = int(feet)
            if feet <= 0:
                checkFeet = False
        else:
            checkFeet = False

    lumber = (input("Enter a 1 for select lumber or a 2 for common lumber "))

    if lumber.isdigit():
        check = True
        lumber = int(lumber)

    if lumber == 1 or lumber == 2:
        check = True
    else:
        check = False

    while not check:
        print("Invalid, try again")
        lumber = (input("Enter a 1 for select lumber or a 2 for common lumber "))
        if lumber.isdigit():
            check = True
            lumber = int(lumber)
        else:
            check = False

        if check is True:
            if lumber < 1 or lumber > 2:
                check = False

    if lumber == 1:
        if feet < 10000:
            total = total + feet * 2
        elif 10000 <= feet <= 50000:
            feet = feet * 2
            discount = feet * .1
            total = feet - discount

        elif feet > 50000:
            feet = feet * 2
            discount = feet * .2
            total = feet - discount

    elif lumber == 2:
        if feet < 10000:
            total = feet * 1

        elif 10000 <= feet <= 50000:
            discount = feet * .1
            total = feet - discount

        elif feet > 50000:
            discount = feet * .2
            total = feet - discount

    print("Total price for the lumber is "f"{total:,.2f}")

    print()
    while not error:
        answer = (input("Continue (y/n)?: "))
        if answer == 'y':
            cont = False
            check = False
            checkFeet = False
            break
        elif answer == 'n':
            cont = True
            error = True
            break
        else:
            print("Invalid, try again")
            error = False
