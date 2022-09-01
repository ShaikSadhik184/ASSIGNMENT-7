print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("enter your choice:")
choice=int(input())
match choice:
    case 1:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a+b
        print("sum is:",c)
    case 2:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a-b
        print("difference is:",c)
    case 3:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a*b
        print(" product is:",c)
    case 4:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a/b
        print("division is:",c)
    case _:
        print("invalid choice")
print()