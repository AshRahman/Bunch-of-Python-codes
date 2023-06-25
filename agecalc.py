from datetime import date

today = date.today()
this_year = int(today.year)
while True:
    try:
        birthdate = int(input("Whats your birthyear: "))
        if birthdate >= this_year:
            raise ValueError
        age = this_year - int(birthdate)
        print(age)
        break

    except ValueError:
        print("Enter valid year")
