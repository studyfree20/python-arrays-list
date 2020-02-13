#the python lists
#list of presidents
globalpresidents=["Barack Obama","Jeff Kennedy","Hillary Clinton","Nelson","Kim li yong","Julius Kirimi"]
print(globalpresidents)
print(globalpresidents[2:5])
print(globalpresidents[-5:-1])
globalpresidents[3]="Donald Trump"                      #changing item in list:Nelson to Donald Trump
globalpresidents[3:4]="Donald Trump","Nelson Mandela"   #changing multiple items in list:Nelson to Donald Trump
print(globalpresidents)
for globalpresident in globalpresidents:
    print(globalpresident)
if "Jeff Kennedy"in globalpresidents:                   #checking if item is in list
    print("\033[0;30;47m]Jeff Kennedy is found")        #changed terminal color and printed query
    print (len(globalpresidents))
    globalpresidents.append("Prince Williams")          #added a president
    print(globalpresidents)
    globalpresidents.insert(3,"Prince III")
    print(globalpresidents)                             #adding in a specific location
    globalpresidents.pop(3)                             #removes an item specified
    print(globalpresidents) 
    globalpresidents.reverse()                          #reverses order of list
    print(globalpresidents) 
    globalpresidents.remove("Barack Obama")             #removes an entry
    print(globalpresidents) 
    globalpresidents.sort()                             #sorts the list
    print(globalpresidents) 
    x=globalpresidents.count("Julius Kirimi")           #counts instances of query
    print(x) 
#end of presidents list

#list of students

students =["Julius Kirimi","Barack Obama","Hilary Clinton"]
print (students)
print (students[1])
students.append("Hilary")   #adding to list
print (students)
#student list ends here
#empty list starts here

Presidents=[]
print(Presidents)
#empty list ends here

