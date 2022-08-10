import numbers


def is_even(x):
    if x!=0:
        return x%2==0

number_pool=[3,4,5,6,8,0]
result=filter(is_even,number_pool)
print(list(result))


res = list(filter(lambda x:x%2 == 0,number_pool))
print(res)