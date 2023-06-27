my_list=[5,2,3,5,6,6,7]

newlist=[]
duplilist=[]
for i in my_list:
    if i not in newlist:
        newlist.append(i)
    else:
        duplilist.append(i)
        
print("Duplicates: ", duplilist)
print("unique: ", newlist)

