def my_dec(func):
    def dec():
        print("--------------")
        func()
        print("--------------")
    return dec
def print_raw():
    print("Word Sandwich")

decorated_func = my_dec(print_raw)
decorated_func()

@my_dec
def print_text():
    print("hello")
print_text()