markOne = int(input("Enter marks for first subject"))

markTwo = int(input("Enter marks for second subject"))

markThree = int(input("Enter marks for third subject"))


tot = markOne + markTwo + markThree
avg = tot/3

if avg>=91 and avg<=100:

    print("Your grade is a+")
elif avg>=81 and avg<91:

    print("Your grade is a")

elif avg>=71 and avg<81:

    print("Your grade is b+")

elif avg>=61 and avg<71:

    print("Your grade is b")

elif avg>=51 and avg<61:

    print("Your grade is c")

else:
    print(" Your grade is f")


