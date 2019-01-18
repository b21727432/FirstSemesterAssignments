import sys
list1=sys.argv[1] #first command line argv
list2=sys.argv[2].split(',') #second command line argv
list3=[] #secret word
list4=[] #used word
for i in range(len(list1)): #putting "-"
    list3.append('-')
guessesleft=5 #if it hits 0 game over
flag=0 #in or out
list5=["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]
list6=[] #letters used in out mode
list7=[] #thrash
list8=[] #thrash
list9=[] #thrash
list10=[] #thrash
for i in range(10): #example 
    if i>5:
        list7.append(i)
    elif i==5:
        list8.append(i)
    else:
        list9.append(i)

for i in range(10):
    list10.append("-")

print("You have {} guesses left".format(guessesleft))
print(list3)
print("-------------------------------------------")
flag1=1 # letter bitti demek için
def winorlost(list): # "-" kaldıysa kaybettin
    for i in list:
        if i == "-":
            return False
    return True
def ibre(list1, char): # harfin nerde oldugunu bulma
    list5=[]
    for i, letter in enumerate(list1):
        if letter == char:
            list5.append(i)
    return list5
for i in list2:
    if i in list1 and flag==0:
        if i not in list4:
            list4.append(i)
            for j in (ibre(list1,i)):
                list3[j] = i
            print("Guessed word: {} You are in IN mode".format(i))
            print("You have {} guesses left".format(guessesleft))
            print(list3)
            print("-------------------------------------------")
            if winorlost(list3) == True:
                print("You won the game")
                flag1=0
                break
        else:
            guessesleft +=-1
            flag=1
            print("Guessed word: {} is used in IN mode. The game turned into OUT mode".format(i))
            print("You have {} guesses left".format(guessesleft))
            print(list3)
            print("-------------------------------------------")
            if guessesleft==0:
                print("You lost the game")
                flag1=0
                break
    elif i not in list1 and flag==0:
        guessesleft +=-1
        flag=1
        print("Guessed word: {} The game turned into OUT mode".format(i))
        print("You have {} guesses left".format(guessesleft))
        print(list3)
        print("-------------------------------------------")
        if guessesleft == 0:
            print("You lost the game")
            flag1 = 0
            break
    elif i in list1 and flag==1:
        guessesleft +=-1
        print("Guessed word: {} You are in OUT mode".format(i))
        print("You have {} guesses left".format(guessesleft))
        print(list3)
        print("-------------------------------------------")
        if guessesleft==0:
            print("You lost the game")
            flag1 = 0
            break

    else:
        flag = 0
        print("Guessed word: {} The game turned into IN mode".format(i))
        print("You have {} guesses left".format(guessesleft))
        print(list3)
        print("-------------------------------------------")
if flag1 == 1:
    print("You finished all letters")
    print("You lost the game")
