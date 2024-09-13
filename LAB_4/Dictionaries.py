#Dictionaries
emp = {"name" : "A",
       "age" : "40",
       "type" : {"devoloper" : ["ios", "android"]},
       "permanent" : True,
       "salary" : 30000.0,
       100 : (1, 2, 3),
       4.5 : {5, 6, True, 7,1},
       True : 1
       }
print(len(emp))  #length
print(type(emp))  #type

#Access Dictionary Items
x = emp["type"]
print(x)
x = emp["type"]["devoloper"]
print(x)
x = emp["type"]["devoloper"][1]
print(x)
x = emp[4.5]
print(x)
x = emp["age"]
print(x)

#Change Dictionary Items
x = emp["permanent"] = False
print(x)

#Add Dictionary Items
emp["gendar"] = "male"
print(emp)

#emove Dictionary Items
emp.pop("age")
print(emp)

#return dictionary's keys
x = emp.keys()
print(x)

#return dictionary's items
x = emp.items()
print(x)

#return dictionary's values
x = emp.values()
print(x)

#using loop return values 
for x in emp.values():
    print(x)

#using loop return keys
for x in emp.keys():
    print(x)   
    
 #Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Apra",
    "year" : 2004
  },
  "child2" : {
    "name" : "Aka",
    "year" : 2006
  },
  "child3" : {
    "name" : "Durjoy",
    "year" : 2011
  }
} 
print(myfamily)  

x = myfamily["child1"]["year"] = 2003
print(x) 
myfamily["child1"]["CGPA"] = 3.72
print(myfamily)

