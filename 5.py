a=int(input("enter a number"))
match a:
    case a if a%2==0:
        print("saurabh shukla")
    case a if a<0 and a%2!=0:
        print("prateek jain")
    case a if a>0 and a%2!=0:
        print("aditya choudhary")
