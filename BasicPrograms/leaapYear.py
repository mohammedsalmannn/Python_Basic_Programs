import re
userInputYear = input("Enter A Year: ")
if not re.match("^[0-9]{4}$", userInputYear):
    print("Year Should Be Of 4 Digit Number")
if int(userInputYear)%4 == 0:
    if (int(userInputYear)%100) != 0 | (int(userInputYear)%400 == 0):
        print(userInputYear,":Leap Year")
    else:
        print(userInputYear, ":Not A Leap Year")
else:
    print(userInputYear, ":Not A Leap Year")