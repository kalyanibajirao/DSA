import re


s = input("Enter your txt here:")

while True:
    choice = int(input(" 1.search \n 2.findall \n 3.split \n 4.sub \n 5.match a word character \n 6.match digit character \n 7.match whitespace character (space, tab, newline, etc.)\n 8.match a zerolength character \n 9.Begining of string \n 10.Ending of string \n 11.Match any charcter \n 12.Exit \n Please enter your choice:"))
    expression =input("Enter your expression here:")
    if choice == 1:
        x = re.search(r'__expression__',s)
        print(x)
    elif choice == 2:
        x = re.findall(r'__expression__',s)
        print(x)
    elif choice == 3:
        x = re.split(r"\s",s)
        print(x)
    elif choice == 4:
        x = re.sub(r"\s",'_expression__',s)
        print(x)
    elif choice == 5:
        x = re.search(r'\w____expression____\w',s)
        print(x)
    elif choice == 6:
        x = re.search(r'\d___expression____\d',s)
        print(x)
    elif choice == 7:
        x = re.search(r'\s___expression___\s',s)
        print(x)
    elif choice == 8:
        x = re.search(r'\b___expression___\b',s)
        print(x)
    elif choice == 9:
        x = re.search(r'^__expression___',s)
        print(x)
    elif choice == 10:
        x = re.search(r'__expression__$',s)
        print(x)
    elif choice == 11:
        x =re.search(r'.__expression__',s)
        print(x)
    elif choice == 12:
        break
    else:
        print("Invalid choice Please choose option from below:")          

    