import re
str = "Hello <<UserName>>, How are you?"
name = input("Enter A Name With Minimum Three Character: ")
if not re.match("^[aA-zZ]{3,}$", name):
    print("Name Should Have Minimum Three Character")
else:    
    str_new = str.replace('<<UserName>>', name)
    print(str_new) 