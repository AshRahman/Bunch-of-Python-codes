number=int(input("Enter the number to be reversed: "))
reverse=0
while (number>0):
    remainder=number%10
    reverse=(reverse*10)+remainder
    number=number//10
print(reverse)