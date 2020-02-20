#collection that is unordered changeable and indexed
#code begings here
#For nested use nested_dict = { 'dictA': {'key_1': 'value_1'},'dictB': {'key_2': 'value_2'}}
president={
    "Name":"Hillary Clinton",
    "Age":30,
    "Residence":"Washington DC",
    "Position":"President",
    "Email":"hillary@statehouse.go.ke",
    "Phone no":+130657019935,

}
print (president)
#code ends here:for integers dont add quotes
#Accesing the dictionary
x=president["Email"]
print(x)
#Also it can be
print(president["Name"])
#Also it can be accessed using get()
y=president.get("Phone no")
print(y)
w=president.get("Residence")
print(w)
a=president.get("Position")
print(a)

#changing values eg Position
president["Position"]="Opposition Leader"
print(president)


#print(president["Julius Kirimi"])
#looping in a dictionary
for presidents in president:
    print(president)
for value in president.values():
    print(value)
#items
for m,n in president.items():
    print (m,n)

#cheking if a value exist
if "Age"in president:
    print('Age is an available field in your dictionary' )
if "Phone no" in president:
    print('Phone is an available field in your dictionary' )

if "position" in president:
    print('Position is an available field in your dictionary' )
if "salary amount" not in president:
    print ('Salary field not found')
else:
    print('Salary is found')
#adding an item to dictionary eg ambassador
president['ambassador']="Texas USA and California"
print(president)
president['Popularity']="77 percent"
print(president)

#remove item using pop()
president.pop("Age")
print (president)

#5 more methods

#copying dictionary
g=president.copy()  
print(g)
#length of dictionary
print("len() method :", len(president))
# Finding a null item
h=president.get("Last election number")
print(h)
# setting a default value
r = president.setdefault("Kirimi")
print(r)
#getting a value
print(president.get("Position")) 
#clearing a dictionary
president.clear()
print(president)
#end