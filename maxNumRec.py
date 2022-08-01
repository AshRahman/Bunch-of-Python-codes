max_arr=[2,4,5,8,9,2,5,10]

def maxA(arr):
    if len(arr)==1:
        return arr[0]
    else:
        m= maxA(arr[1:])
        return m if m>arr[0] else arr[0]

print(maxA(max_arr))
