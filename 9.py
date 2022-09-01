year=int(input("enter a year:"))
match year:
    case year if year%100!=0 and year%4==0:
        print("non century leap year")
    case year if year%400==0:
        print("century leap year")
    case year  if year%100!=0 and year%4!=0:
        print("non century non leap year")
    case year if year%400!=0:
        print("century non leap year")