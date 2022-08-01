def beautify(text):
    return text + "!!!"

def make_line(func, words):
    return "Hello"+func(words) #calls the second function taking the arguement

print(make_line(beautify," World"))
print(make_line.__doc__)