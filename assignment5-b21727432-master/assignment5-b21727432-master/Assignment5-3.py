import sys
a=open(sys.argv[1],"r")
b=open("output.txt","w")
names=[]
cities=[]
info=[]
wanted=sys.argv[2]
for line in a.readlines():
    line=line.strip("\n").split(":")
    names.append(line[0])
    cities.append(line[1])
info1={}
for i,j in zip(names,cities):
    x=[]
    x.append(i)
    x.append(j)
    info.append(x)
    info1[i]=j
#print(info) {'Valentine': 'San Antonio', 'Fatima': 'Hopkins', 'Danica': 'Waco', 'Yuki': 'Taylor', 'Willar

sortedinfo=[]
#print(info)[['James', 'New Orleans'], ['Josephine', 'Brighton'], ['Art', 'Bridgeport'], ['Lenna', 'Anchorage'], ['Donette', 'Hamilton'], ['Simona', 'Ashland'], ['Mitsue', 'Chicago'], ['Leota', 'San Jose'], ['Sage', 'Sioux Falls'], ['Kris', 'Baltimore'], ['Minna', 'Kulpsville'], ['Abel', 'Middle Island'], ['Kiley', 'Los Angeles'], ['Graciela', 'Chagrin Falls'], ['Cammy', 'Laredo'], ['Mattie', 'Phoenix'], ['Meaghan', 'Mc Minnville'], ['Gladys', 'Milwaukee'], ['Yuki', 'Taylor'], ['Fletcher', 'Rockford'], ['Bette', 'Aston'], ['Veronika', 'San Jose'], ['Willard', 'Irving'], ['Maryann', 'Albany'], ['Alisha', 'Middlesex'], ['Allene', 'Stevens Point'], ['Chanel', 'Shawnee'], ['Ezekiel', 'Easton'], ['Willow', 'New York'], ['Bernardo', 'Conroe'], ['Ammie', 'Columbus'], ['Francine', 'Las Cruces'], ['Ernie', 'Ridgefield Park'], ['Albina', 'Dunellen'], ['Alishia', 'New York'], ['Solange', 'Metairie'], ['Jose', 'New York'], ['Rozella', 'Camarillo'], ['Valentine', 'San Antonio'], ['Kati', 'Abilene'], ['Youlanda', 'Prineville'], ['Dyan', 'Overland Park'], ['Roxane', 'Fairbanks'], ['Lavera', 'Miami'], ['Erick', 'Fairbanks'], ['Fatima', 'Hopkins'], ['Jina', 'Boston'], ['Kanisha', 'Los Angeles'], ['Emerson', 'Madison'], ['Blair', 'Philadelphia'], ['Brock', 'New York'], ['Lorrie', 'Tullahoma'], ['Sabra', 'Columbia'], ['Marjory', 'Wayne'], ['Karl', 'Flemington'], ['Tonette', 'Westbury'], ['Amber', 'Jenkintown'], ['Shenika', 'Van Nuys'], ['Delmy', 'Providence'], ['Deeanna', 'Huntingdon Valley'], ['Blondell', 'Providence'], ['Jamal', 'Monroe Township'], ['Cecily', 'Austin'], ['Carmelina', 'Littleton'], ['Maurine', 'Milwaukee'], ['Tawna', 'New York'], ['Penney', 'Anchorage'], ['Elly', 'Erie'], ['Ilene', 'Glen Burnie'], ['Vallie', 'Boise'], ['Kallie', 'San Francisco'], ['Johnetta', 'Chapel Hill'], ['Bobbye', 'San Carlos'], ['Micaela', 'Concord'], ['Tamar', 'London'], ['Moon', 'Wellsville'], ['Laurel', 'Baltimore'], ['Delisa', 'Newark'], ['Viva', 'Chicago'], ['Elza', 'Newark'], ['Devorah', 'Clovis'], ['Timothy', 'Staten Island'], ['Arlette', 'Jacksonville'], ['Dominque', 'Hayward'], ['Lettie', 'Beachwood'], ['Myra', 'Euless'], ['Stephaine', 'Gardena'], ['Lai', 'Evanston'], ['Stephen', 'Akron'], ['Tyra', 'Philadelphia'], ['Tammara', 'Burlingame'], ['Cory', 'San Gabriel'], ['Danica', 'Waco'], ['Wilda', 'Anchorage'], ['Elvera', 'San Jose'], ['Carma', 'San Leandro'], ['Malinda', 'Indianapolis'], ['Natalie', 'Rock Springs'], ['Lisha', 'Mc Lean'], ['Arlene', 'New Orleans']]

while True:
    if info != []:
        x=min(info)
        sortedinfo.append(x)
        y=info.index(x)
        del info[y]
    if info == []:
        break
#print(sortedinfo)[['Abel', 'Middle Island'], ['Albina', 'Dunellen'], ['Alisha', 'Middlesex'], ['Alishia', 'New York'
sortedname=[]
sortedcity=[]
for i in sortedinfo:
    sortedname.append(i[0])
    sortedcity.append(i[1])

#print(sortedname) works correctly



def binarysearch(list,item):
    first=0
    last=len(list)-1
    i=(first+last)//2



    if len(list) != 1:



        if len(list)==2:
            if item > list[1]:
                b.write(" ".join(list))
                b.write("\n")
                return list[1]
            if item < list[0]:
                b.write(" ".join(list))
                b.write("\n")
                return list[0]
        if item < list[i]:
            b.write(" ".join(list))
            b.write("\n")
            return binarysearch(list[:i],item)
        if item > list[i]:
            b.write(" ".join(list))
            b.write("\n")
            return binarysearch(list[i+1:],item)
        if item == list[i] :
            b.write(" ".join(list))
            b.write("\n")
            return list[i]

    else:
        return list[i]



try:

    dsa=info1[wanted]
    b.write("Searching value is :")
    b.write(wanted)
    b.write("\n\n")


    b.write(" ".join(names))

    b.write("\n")
    b.write(binarysearch(sortedname, wanted))
    b.write("\n\n")
    b.write("The search string is ")
    b.write(wanted)
    b.write(" and the city is ")
    b.write(dsa)


except KeyError:
    b.write("Searching value is :")
    b.write(wanted)
    b.write("\n\n")
    b.write(" ".join(names))
    b.write("\n")
    b.write(binarysearch(sortedname, wanted))
    b.write("\n\n")
    b.write("The search string was not found in file")

a.close()
b.close()
