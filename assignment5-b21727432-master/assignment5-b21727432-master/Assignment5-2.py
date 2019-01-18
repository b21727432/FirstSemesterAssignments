import sys
try:

    input1=open(sys.argv[1],"r")
    inputlist = []
    for i in input1.readlines():
        i = i.strip("\n")
        i = i.strip(";")
        i = i.split(",")
        inputlist.append(i)
except IOError:
    print("file not found... Opening a new file...")
    input1=open(sys.argv[1],"r")

input1.close()

output1=open(sys.argv[1],"w")

#print(inputlist) [['123', '25', 'Terminator', 'Action', 'James Cameron', 'Hired;'],


outputlist=[]

while True:
        print("""
        ----HUBM DVD-----
        A: ADD NEW
        R:REMOVE
        S:SEARCH
        L:LİST
        E:EDİT
        H:HİRE
        Q:QUİT

        """)
        command=input("enter your command without any extra whitelines ")
        command=command.split(",")

        if command[0] == "Q":
            sayac1 = 0
            for i in inputlist:
                output1.write(";".join(inputlist[sayac1]))
                output1.write("\n")
                sayac1 += 1
            break
        elif command[0]=="A":
            list=[]
            for j in inputlist:
                list.append(j[0])
            if command[1] not in list:
                x=[]

                for i in command[1:]:
                    x.append(i.strip('"'))
                inputlist.append(x)
                print("dvd stored")

            elif command[1] in list:
                print("serial number already exist")
                continue
        elif command[0]=="R":

            for x in inputlist:
                if command[1]==x[0]:
                    if x[5]!="Hired":
                        print("Serial   Price   Name    Genre   Director    State")
                        print("      ".join(x))
                        kesin=input("are you sure about deleting it?type Yes or No")
                        if kesin=="Yes":
                            print("Deleting...")
                            inputlist.remove(x)
                        elif kesin=="No":
                            print("Not deleting...")
                            break
                        else:
                            print("you think you are the only smart guy here?")
                            break
                    else:
                        print("You can not remove a hired dvd")
                else:
                    print("that dvd does not exist")
                    break
        elif command[0]=="S":
            command[1]=command[1][1:-1]
            haha=0
            for y in inputlist:
                if command[1]==y[2][:3]:
                    print("Serial   Price   Name    Genre   Director    State")
                    print("      ".join(y))
                    haha +=1
            if haha==0:
                print("i could not find what you asked for")
        elif command[0]=="L":


            sayac=0
            while True:
                aaa=input("hit enter to list dvd's 1 by 1 hit anything else to quit")
                if aaa=="":
                    print("Serial   Price   Name    Genre   Director    State")
                    print("    ".join(inputlist[sayac]))

                    sayac +=1
                    if sayac==len(inputlist):
                        break
                else:
                    break

        elif command[0]=="E":
            for i in command[2:]:
                i=i[1:-1]
                i=i.split("=")

                if i[0]=="Name":
                    for j in inputlist:
                        if j[0]==command[1]:
                            j[2]=i[1]
                            j[2]=j[2][1:-1]
                if i[0]=="Price":
                    for j in inputlist:
                        if j[0]==command[1]:
                            j[1]=i[1]
                if i[0]=="Genre":
                    for j in inputlist:
                        if j[0]==command[1]:
                            j[3]=i[1]
                            j[3]=j[3][1:-1]
                if i[0]=="Director":
                    for j in inputlist:
                        if j[0]==command[1]:
                            j[4]=[1]
                            j[4]=j[4][1:-1]
        elif command[0]=="H":
            for x in inputlist:
                if x[0]==command[1]:
                    if x[5]=="Inv":
                        x[5]="Hired"
                    if x[5]=="Hired":
                        print("dvd is already hired")



        else:
            print("Are you blind? Enter valid command")
            
            
            
            
            
            
output1.close()


