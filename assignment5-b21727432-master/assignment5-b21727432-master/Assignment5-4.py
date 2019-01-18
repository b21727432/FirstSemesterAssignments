import matplotlib.pyplot as plt
import numpy as np
import sys
datalist=[]
data=open(sys.argv[1],"r")
for i in data.readlines():
    i=i.strip("\n")
    i=i.split(";")
    datalist.append(i)
#print(datalist)[['6', '148', '72', '35', '0', '33.6', '0.627', '50', '1'], ['1', '85', '66', '29', '0', '26.6', '0.351', '31', '0']
chosen=[]
for i in datalist:
    i[0]=int(i[0])
    i[1] = int(i[1])
    i[2] = int(i[2])
    i[3] = int(i[3])
    i[4] = int(i[4])
    i[7] = int(i[7])
    i[8] = int(i[8])

    i[5]=float(i[5])
    i[6]=float(i[6])

#print(chosen)[[6, 148, 72, 35, 0, 33.6, 0.627, 50, 1], [1, 85, 66, 29, 0, 26.6, 0.351, 31, 0], [8, 183, 64, 0, 0, 23.
for i in datalist:
    if i[2]>=90:
        chosen.append(i)
#print(chosen)[8, 125, 96, 0, 0, 0.0, 0.232, 54, 1], [4, 110, 92, 0, 0, 37.6, 0.191, 30, 0], [7, 196, 90, 0, 0, 39.8, 0.451, 41, 1], [11, 143, 94, 3
ages=[]
sayac=[]
for i in range(len(chosen)):
    sayac.append(i)
for i in chosen:
    ages.append(i[7])


max=0
index=int()
for i in chosen: # 0 dogum 7 age


    if i[0]!=0 and i[7]!=0:
        lol=i[0]/i[7]
        if lol>max:
            max=lol
            index = chosen.index(i)
min=max
index2=()
for i in chosen:
    if i[0] != 0 and i[7] != 0:
        lol = i[0] / i[7]
        if lol < min:
            min=lol
            index2=chosen.index(i)
#print(max)0.30952380952380953
#print(index)10
#print(min)0.022222222222222223
#print(index2)28
# 5 İNDEX 7 AGE

max1=0
index3=int()

for i in chosen:
    if i[5] != 0 and i[7] != 0:
        wow=i[5]/i[7]
        if wow > max1:
            max1=wow
            index3=chosen.index(i)
min1=max1
index4=int()
for i in chosen:
    if i[5] != 0 and i[7] != 0:
        wow = i[5] / i[7]
        if wow < min1:
            min1 = wow
            index4 = chosen.index(i)



part1=[]
part1.append(index)
part1.append(index2)
part2=[]
part2.append(index3)
part2.append(index4)
yenilist=[]
yenilist2=[]
yenilist.append(chosen[28][7])
yenilist.append(chosen[10][7])
yenilist2.append(chosen[52][7])
yenilist2.append(chosen[39][7])

plt.annotate("max(#pregnancy/age)",xy=(part1[0],yenilist[0]),xytext=(0.32, 0.566),textcoords='axes fraction',xycoords='data',arrowprops=dict(facecolor='red', shrink=0.05),horizontalalignment='left', verticalalignment='top')
plt.annotate("min(#pregnancy/age)",xy=(part1[1],yenilist[1]),xytext=(0.35, 0.67),textcoords='axes fraction',xycoords='data',arrowprops=dict(facecolor='red', shrink=0.05),horizontalalignment='left', verticalalignment='top')
plt.annotate("max(#body mass index/age)",xy=(part2[0],yenilist2[0]),xytext=(0.5, 0.25),textcoords='axes fraction',xycoords='data',arrowprops=dict(facecolor='green', shrink=0.05),horizontalalignment='left', verticalalignment='top')
plt.annotate("min(#body mass index/age)",xy=(part2[1],yenilist2[1]),xytext=(0.156, 1),textcoords='axes fraction',xycoords='data',arrowprops=dict(facecolor='green', shrink=0.05),horizontalalignment='left', verticalalignment='top')
plt.plot(sayac,ages)
plt.xticks(np.arange(1, len(sayac), 5))
plt.xlabel("Instances")
plt.ylabel("Ages")

plt.savefig("Fig1.pdf")
