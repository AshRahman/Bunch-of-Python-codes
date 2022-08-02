num= 15
arr=[5,7,9,10,15,17,20,25,30]

def bin(arr,low,high,x):

    if high>=low:

        mid=(high+low)//2


        if(arr[mid]==x):
            print("found at: {0}".format(mid))
        elif(arr[mid]>x):
            bin(arr,low,mid-1,x)
        else:
            bin(arr,mid+1,high,x)
    else:
        return -1
bin(arr,0,len(arr)-1,num)