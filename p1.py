print("hellow world".title())
list_=list()
print(list_)

#contstants
MAX=100


#LIST FUNCTION
NAME=['A','b','SDF','DFS','azmat']
# print(NAME[4].get(1).title())
# print(f"my name is {NAME[4].get(1).title()}")

for obj in enumerate(NAME):
    print(list(obj))

#difference between sort->prmanedtedly  and sorted  not permenaedly

print("1".join(NAME))


print(NAME[::-1])

print(NAME[:-1])

# refernce 
NAME2=NAME.copy()
NAME2.remove('A')
print(NAME2)

print(NAME)


for i in NAME:
    print(i.title(), i.upper())
\
#single staric typle

# double staric dixtionay*
def check(*b):
    
    return b
print(check("dfd"))