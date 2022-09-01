age=int(input("enter a number:"))
match age:
    case age if age <10:
        print("kid")
    case age if 10<age<20:
        print("teen")
    case age if 20<age<40:
        print("young")
    case age if 40<age<60:
        print("experienced")
    case age if age>=60:
        print("senior citizen")
  
    
    