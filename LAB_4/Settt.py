#My practice
thisset = {"Apra", "CSE", "DIU"}
print(thisset)
print(len(thisset))
print(type(thisset))
a = set(("Hi", "Namaskar", "annyeong"))  #set constructor
print(a)

for x in thisset:
    print(x)

thisset.add(1823)   #Add Method (item)
print(thisset)    

thisset.update(a)  #add set using update method
print(thisset)
#//

#set
a = {1, 3, 5, 8, 3, 7}
print(len(a))  #length of the set
print(type(a))  #type of the set

#add method
a.add(10)
print(a)

#remove method
a.remove(8)
print(a)

#join sets
b = {0, False, 1, 5}
c = a | b   #union/|
print(c)

c = a.intersection(b)  #&/intersection
print(c)

c = a - b  #difference/ -
print(c)

# #update method
# a.update(b)
# print(a)

#loop 
print(a)
for x in a:
    if x == 5:
        break       
    print(x)

d = {2, 3, 4}
print(a.union(d))

#subset method
d = a.issubset(b)
print(d)

#superset method
d = a.issuperset(b)
print(d)

