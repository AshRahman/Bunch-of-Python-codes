try:
    a = 1000
    b = int(input("Enter a divisor to divide 1000: "))
    print("Start of the program")
    print(a/b)
except ZeroDivisionError:
    print("You have entered 0 which is not permitted!")
    
finally:
    print("This code will run eventually")