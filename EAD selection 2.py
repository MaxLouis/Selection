#Max Louis
#EAD selection Q2
#09/10/2014

firstName = input("Please enter your first name.")
secondName = input("Please enter your second name.")
gender = input("Please enter your gender.")

if gender == "Male" or gender == "male" or gender == "M" or gender == "m":
    print("Mr {0} {1}".format(firstName,secondName))

elif gender == "Female" or gender == "female" or gender == "F" or gender == "f":
    print("Ms {0} {1}".format(firstName,secondName))

else:
    print("Please enter an appropriate gender")
