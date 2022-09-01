s1=input("enter first string:")
s2=input("enter second string:")
match(s1,s2):
    case (s1,s2) if s1==s2:
        print("identical strings")
    case(s1,s2) if s1>s2:
        print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} comes after {}".format(s2,s1))
print()