#Max Louis
#EAD selection Q1
#09/10/2014

attend = float(input("Please input students attendance."))

if attend <= 85:
    danger = True
elif attend >= 85:
    danger = False

if danger == True:
    print("Your attendance is only {0}%. You must improve your attendance.".format(attend))
else:
    print("Your attendance is {0}%. Keep up the good attendance.".format(attend))
