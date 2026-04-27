print("choose y for yes and n for no")
dog_for_a_walk=(input("did you take the dog for a walk?: "))
drink_milk=(input("did you drink your milk?: "))
homework=(input("did you do your homework?: "))
veggie=(input("did you eat your veggie?: "))
help_mom=input("did you help mom with chores: ")

if dog_for_a_walk=="y" and drink_milk=="y" or homework=="y" and veggie=="y":
    print("I will take you to the PARK!")

elif help_mom=="y":
    print("I am still taking you to the PARK")

else:
    print("I am not taking you to the park")