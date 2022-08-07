try:
    file_to_work= open("testFile.txt","r")
    content =file_to_work.read()
    print(content)
finally:
    file_to_work.close()
    
with open("testFile.txt") as content:
    print(content.read())