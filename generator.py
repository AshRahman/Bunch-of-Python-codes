def even_numbers(x):
    for i in range(x):
        if i%2==0:
            yield i #this makes it a generator function
            
even_nums_list = list(even_numbers(10))
print(even_nums_list)
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
a=my_gen()
next(a)
next(a)
next(a)

for item in my_gen():
    print(item)

