a = int(input("enter number a:"))
if a%3 == 0 and a%5 == 0:
    print("Fizz-Buzz")
elif a%3 == 0:
    print("Fizz")
elif a%5 == 0:
    print("Fuzz")         
else:
    print("this number is not divisible by 3 and 5") 