from datetime import date

today=date.today()
this_year=int(today.year)

birthdate=input("Whats your birthyear: ")

age=this_year-int(birthdate)
print(age)