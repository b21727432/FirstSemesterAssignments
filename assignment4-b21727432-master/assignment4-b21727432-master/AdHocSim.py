import sys

commands=open("commands","r")
lineofcommands=[]
for line in commands:
    line=line.strip("\n")
    line=line.split("\t")
    lineofcommands.append(line)
print(lineofcommands)
genellist=[]
isimlist=[]
path=[]

for elements in lineofcommands:
    #print(elements) ['0', 'SEND', 'x1', 'x9', '547']
    if elements[1]=="CRNODE":
        isimlist.append(elements[2])
        elements[2]=[]
        coor=elements[3].split(";")
        coor2=elements[4].split(";")
        finalx1=int(coor[0])+int(coor2[0])
        finalx2=int(coor[0])-int(coor2[1])
        finaly1=int(coor[1])+int(coor2[2])
        finaly2=int(coor[1])-int(coor2[3])
        elements[2].append(finalx1)
        elements[2].append(finalx2)
        elements[2].append(finaly1)
        elements[2].append(finaly2)
        elements[2].append(int(elements[5]))
        genellist.append(elements) #[['0', 'CRNODE', [220, 120, 100, 0, 65], '120;40', '100;0;60;40', '65']
    if elements[1]=="SEND":
        path.append(elements[2])
        path.append(elements[3])

copylist=[]
for i in genellist:

    copylist.append(i)
coorlist=[]
for i in copylist:
    i[3]=i[3].split(";")
    for j in i[3]:
        j=int(j)
for i in copylist:
    coorlist.append(i[3])
#print(coorlist)#[['120', '40'],['200', '50'], ['150', '15'], ['240', '60'], ['260', '45'], ['225', '15'], ['273', '20'], ['221', '5'], ['345', '20']]
dict={}
for i,x in zip(genellist,isimlist):
    k=x
    x=[]
    for j,y in zip(genellist,isimlist):

        if (i[2][1]<=int(j[3][0])<=i[2][0]) and (i[2][3]<=int(j[3][1])<=i[2][2]):
            if k!=y:
                x.append(y)
    dict[k]=x
#print(dict)#{'x9': [], 'x5': ['x7'], 'x2': ['x4', 'x5'], 'x7': ['x9'], 'x6': ['x7', 'x8'], 'x4': ['x5', 'x7'], 'x1': ['x2', 'x3'], 'x8': [], 'x3': ['x6', 'x8']}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
dict2={}
for i,j in zip(coorlist,isimlist):
    dict2[j]=i
#print(dict2) #{'x2': ['200', '50'], 'x1': ['120', '40'], 'x6': ['225', '15'], 'x8': ['221', '5'], 'x3': ['150', '15'], 'x9': ['345', '20'], 'x5': ['260', '45'], 'x7': ['273', '20'], 'x4': ['240', '60
#print(find_all_paths(dict,"x1","x9")) [['x1', 'x2', 'x4', 'x5', 'x7', 'x9'], ['x1', 'x2', 'x4', 'x7', 'x9'], ['x1', 'x2', 'x5', 'x7', 'x9'], ['x1', 'x3', 'x6', 'x7', 'x9']]
listofpaths=find_all_paths(dict,path[0],path[1])
 # [['x1', 'x2', 'x4', 'x5', 'x7', 'x9'], ['x1', 'x2', 'x4', 'x7', 'x9'], ['x1', 'x2', 'x5', 'x7', 'x9'], ['x1', 'x3', 'x6', 'x7', 'x9']]

print('********************************')
print('AD-HOC NETWORK SIMULATOR - BEGIN')
print('********************************')
print('\tNODES & THEIR NEIGHBORS:', end= " ")
print(dict)
# prints number of possible routes found
print( ' ROUTE(S) FOUND:')
print(listofpaths)
