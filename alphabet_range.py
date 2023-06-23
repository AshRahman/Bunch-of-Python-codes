def range_char(start,stop):
    return (chr(n) for n in range(ord(start),ord(stop)+1))

for char in range_char("A", "G"):
    print(char)