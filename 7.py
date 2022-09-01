x=int(input("enter a number:"))
match x:
    case x if x>0:
        print("positive number")
    case x if x<0:
        print("negative number")
    case x if x==0:
        print("zero")
