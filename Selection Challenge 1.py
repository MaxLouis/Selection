#Max Louis
#Selection: Challenge 1
#30/09/14

date = input("What is the date? DD MM YY.")

days = date[0:2]
months = date[3:5]
years = date[6:8]

if date[1:8:2] == "1":
    print(days,"st")
    
