list=[2,4,6,7,8,1]

def count(arr):
    if len(arr)<=0:
        return 0
    else:
        return 1+count(arr[1:]) #1+count([4,6,7,8,1]) -> 2+count([6,7,8,1])
print(count(list))