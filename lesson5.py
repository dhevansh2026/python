side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))

if side1==side2==side3:
    print("Equilateral Triangle")
else:
    if side1==side2 or side3==side1 or side2==side3:
        print("Isosceles Triangle")
    else:print("scalene Triangle")


number=int(input("Enter number: "))

if number % 2==0:
    print("it's an even number")
else:
    print("it's a odd number")
