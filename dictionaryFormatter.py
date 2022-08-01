### using * arguement for making dictionary
def make_dict(**kwargs):
    print(kwargs) #makes the dictionary format
    for args in kwargs:
        print("{0} : {1}".format(args,kwargs[args]))

make_dict( a = 1, b =2, c = 3)