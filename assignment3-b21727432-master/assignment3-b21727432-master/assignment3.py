import sys
hurap_file = open(sys.argv[1], "r")
schuckscii_file = open(sys.argv[2], "r")

def binhexZ(invalue):
    wmap = {"0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "A",
            "1011": "B",
            "1100": "C",
            "1101": "D",
            "1110": "E",
            "1111": "F"
            }
    i = 0
    output = ""

    while (len(invalue) % 4 != 0):
        invalue = "0" + invalue

    while (i < len(invalue)):
        output = output + wmap[invalue[i:i + 4]]
        i = i + 4

    output = output.lstrip("0")
    output = "0" if len(output) == 0 else output

    return output


def hex2binZ():
    e=raw_input("enter hexadecimal no.:")
    e1=("a","b","c","d","e","f")
    e2=(10,11,12,13,14,15)
    e3=1
    e4=len(e)
    e5=()
    while e3<=e4:
        e5=e5+(e[e3-1],)
        e3=e3+1

    e6=1
    e8=()
    while e6<=e4:
        e7=e5[e6-1]
        if e7=="A":
            e7=10
        if e7=="B":
            e7=11
        if e7=="C":
            e7=12
        if e7=="D":
            e7=13
        if e7=="E":
            e7=14
        if e7=="F":
            e7=15
        else:
            e7=int(e7)
        e8=e8+(e7,)
        e6=e6+1


    e9=1
    e10=len(e8)
    e11=()
    while e9<=e10:
        e12=e8[e9-1]
        a1=e12
        a2=()
        a3=1
        while a3<=1:
            a4=a1%2
            a2=a2+(a4,)
            a1=a1/2
            if a1<2:
                if a1==1:
                    a2=a2+(1,)
                if a1==0:
                    a2=a2+(0,)
                a3=a3+1
        a5=len(a2)
        a6=1
        a7=""
        a56=a5
        while a6<=a5:
            a7=a7+str(a2[a56-1])
            a6=a6+1
            a56=a56-1
        if a5<=3:
            if a5==1:
                a8="000"
                a7=a8+a7
            if a5==2:
                a8="00"
                a7=a8+a7
            if a5==3:
                a8="0"
                a7=a8+a7
        else:
            a7=a7

        e9=e9+1

hexofcode=[]
list1=[]
sayac=0
for lines in schuckscii_file.readlines():
    lines=lines.strip("\n")
    newlist=lines.split("\t")
    list1.append(newlist)
    sayac +=1
list4=[]
secondlist4=[]
for i in list1:
    list4.append(i[0])
for i in list1:
    secondlist4.append(i[1])

list3=[]



sayac2=0
for lines in hurap_file.readlines():
    if lines[0]=="0":
        a=int(lines,2)
        b='{:X}'.format(a)
        sayac2 +=1
        n=2
        d = [b[i:i + n] for i in range(0, len(b), n)]

        for n, i in enumerate(d):
            for j in list1:
                if i == j[1]:
                    d[n] = j[0]
                    list2=''.join(d)
        #print(list2)
        list3.append(list2)

    else:

        a=lines[1:-1]
        lena=len(a)
        if a[0]=="1":
            a=int(a,2)
            num_bits = lena
            shiftamount= a - (1 << num_bits)

        else:
            shiftamount=int(a,2)

sayı=shiftamount

list5=[]
#encrypted=(original+shift) mod n
original=int()
#original =en - shit mod n
for alines in list3:

    for i in alines:

        n=(list4.index(i))
        original=(n-shiftamount)%sayac
        list5 +=list4[original]
    list5 +="\n"
list6=''.join(list5) #import annihilation


dict1={}
virus_codes_file = open(sys.argv[3], "r")
for lines in virus_codes_file.readlines():
    lines=lines.strip("\n")
    lines=lines.split(":")
    dict1.update({lines[0]:lines[1]})



sahtestr=()
sahtestr=list6
for e in dict1:
    if e in list6:
        list6=list6.replace(e,dict1[e])


list8=[]
encrpt=int()
for i in list6:
    if i != "\n":
        k=list4.index(i)
        encrpt=(k+shiftamount)%sayac
        list8 +=list4[encrpt]
    elif i=="\n":
        list8 +="\n"
#print(list8)
encrptlist="".join(list8)

hexofenc=[]

for n, i in enumerate(list8): #n sayı i eleman
    for j in list1:
        if i == j[0]:
            list8[n] = j[1]
            hexofenc = ''.join(list8)









print("""*********************
     Mission 00 
*********************""", end="\n\n")

print("""--- hex of encrypted code ---
-----------------------------""", end="\n\n")
print(hexofenc)
print("""\n--- encrypted code ----
-----------------------""", end="\n\n")
print(encrptlist)
print("""\n--- decrypted code ---
----------------------""", end="\n\n")
print(sahtestr)
print("""\n*********************
     Mission 01 
*********************""", end="\n\n")
print(list6)
print("""\n*********************
     Mission 10 
*********************""", end="\n\n")

print("""--- encrypted code ---
----------------------""", end="\n\n")
print(encrptlist)
print("""\n--- hex of encrypted code ---
-----------------------------""", end="\n\n")
print(hexofenc)
print("""\n--- bin of encrypted code ---
-----------------------------""", end="\n\n")
yeniliste=hexofenc.split("\n")
sonliste=[]
for i in yeniliste:
    if i != "\n":
        for index, value in enumerate(i):
            sonliste +=(bin(int(value, 16) + 16)[3:])


        string = ''.join([bin(int(x, 16) + 16)[3:] for y, x in enumerate(i)])
        print(string)

hurap_file.close()
schuckscii_file.close()
virus_codes_file.close()