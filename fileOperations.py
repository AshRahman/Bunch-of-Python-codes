from winreg import HKEY_LOCAL_MACHINE


#file_to_work_on = open("testFile.txt","w") #for write mode
#file_to_work_on = open("testFile.txt","r") #for read mode
#file_to_work_on = open("testFile.txt","a") #for append mode
#file_to_work_on = open("testFile.txt","wb") #for opening binary file in write mode
file_to_work = open("testFile.txt","w")
file_to_work.write("More content i guess")
file_to_work.close()
#file_to_work_on.close()
# file_create=open("file.txt","x")
# file_create.write("Test file write")
# file_create.close()

file_to_work=open("testFile.txt","r")
#content=file_to_work.read()
lines=file_to_work.readlines()



#print(content)
print(lines)
file_to_work.close()
