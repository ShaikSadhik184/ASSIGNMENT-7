x=input("enter a string:")
x.strip()
match x:
    case x if ' ' in x:
        print("multiword string")
    case x if ' ' not in x:
        print("single word string")
print()
