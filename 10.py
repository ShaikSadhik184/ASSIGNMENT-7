x=input("what is your favourite colour: ")
l1=["yellow","blue","orange","white","black","red"]
for colour in l1:
    if colour in x:
        c=colour
        break
    else:
        c="other"
match c:
    case "yellow":
        print("monday")
    case "blue":
        print("tuesday")
    case "orange":
        print("wednesday")
    case "white":
        print("thursday")
    case "black":
        print("friday")
    case "red":
        print("saturday")
    case "other":
        print("sunday")
print()

