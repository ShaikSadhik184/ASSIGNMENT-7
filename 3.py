print("1.isosceles triangle")
print("2.right angled triangle")
print("3.equilateral triangle")
print("4.exit")
choice=int(input())
match choice:
    case 1:
        print("enter three numbers")
        a,b,c=int(input()),int(input()),int(input())
        if a==b or b==c or c==a:
    
            print("isosceles triangle")
        else:
            print("false")
    case 2:
        print("enter three numbers")
        a,b,c=int(input()),int(input()),int(input())
        if c**2==a+b:
            print("right angled triangle")
        else:
            print("false")
    case 3:
        print("enter three numbers")
        a,b,c=int(input()),int(input()),int(input())
        if a==b and b==c:

            print("eqquilateral triangle")
        else:
            print("false")
    case 4:
        print("exit")





      
