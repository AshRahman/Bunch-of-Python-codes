num=10
arr=[5,7,9,10,15,17,25,30,35]

def bs(arr,target):
    fst=0
    lst=len(arr)
    i=lst-1

    while i>0 and arr[i]==target:
        mid=(fst+lst)//2
        print(mid)
        if target<arr[i]:
            mid=arr-1
            i-=1
        else:
            mid=arr+1
            i-=1


bs(arr,15)