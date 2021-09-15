a = int(input("enter number a:"))
b = int(input("enter number b:"))
c = int(input("enter number c:"))
if a > b and a > c:
    if b > c:
        print("b is the second greatest number")
    else:
        print("c is the second greatest number")
elif b > c and b > a:
    if c > a:
        print("c is the second greatest number")
    else:
        print("a is the second greatest number")
elif c > a and c > b:
    if a > b:
        print("a is the second greatest number")
    else:
        print("b is the second greatest number")    