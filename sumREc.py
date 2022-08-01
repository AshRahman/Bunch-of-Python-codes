arr=[2,4,6,7]

def sum(arr,N):
    if N<=0:
        return 0
    else:
       return sum(arr,N-1)+arr[N-1] # arr[2,4,6,7],3 + arr[2,4,6,7],2 + arr[2,4,6,7],1 + arr[2,4,6,7],0
    
N=len(arr)
print(sum(arr,N))
    