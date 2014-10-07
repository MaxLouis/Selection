#Max Louis
#Boolean Exercise
#24/09/14

age = int(input("What age are you?"))

if age < 18:
    print("You cannot vote")

else:
    print("You can vote")

retire = 65 - age

if age >= 65:
    print("You can retire!")

if age < 65:
    print("You can retire in {0} year(s).".format(retire))
