#print("lol"*50)
from dataclasses import replace


msg="What is intend to is {1}, and why is that is {0}".format("violence","fun")
print(msg)
msg2="Previous msg was by a {x},Dont believe what he {y}".format(x="madman",y="says")
print(msg2)


print(", ".join(["apple","orange","pinapple"]))

replace="ar koto kal"
print(replace.replace("kal","kola"))

print("k,o,l,a".split(","))