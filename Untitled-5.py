def desc(m):
    winter = "White snow fell outside the window"
    spring = "Birds sang beautiful songs"
    summer = "The sun shone brighter than ever"
    autumn = "The harvest was incredible "
    if m == "January" or m == "February" or m == "December":
        print("Your were born in ", m,".", winter)
    elif m == "March" or m == "April" or m == "May":
        print("Your were born in ", m,".", spring)
    elif m == "June" or m == "July" or m == "August":
        print("Your were born in ", m,".", summer)
    elif m == "September" or m == "October" or m == "November":
        print("Your were born in ", m,".", autumn)
    else:
        print("That's not a month!")
month = input("Enter the month you were born in: ")
desc(month)
