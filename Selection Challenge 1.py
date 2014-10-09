#Max Louis
#Selection: Challenge 1
#30/09/14

date = input("What is the date? DD MM YY.")

days = date[0:2]
months = date[3:5]
years = date[6:8]

years = int(years)

if days[0] == "0":
    days = days[1]

if date[1] == "1":
    days = ("{0}st".format(days))
    
elif date[1] == "2":
    days = ("{0}nd".format(days))

elif date[1] == "3":
    days = ("{0}rd".format(days))

else:
    days = ("{0}th".format(days))
    

if months == "01":
          months = "January"
if months == "02":
          months = "February"
if months == "03":
          months = "March"
if months == "04":
          months = "April"
if months == "05":
          months = "May"
if months == "06":
          months = "June"
if months == "07":
          months = "July"
if months == "08":
          months = "August"
if months == "09":
          months = "September"
if months == "10":
          months = "October"
if months == "11":
          months = "November"
if months == "12":
          months = "December"

if years > 31:
    century = "19"
else:
    century = "20"

print(days,months,"{0}{1}".format(century,years))

