def mot_a_evoluer():
    n=int(input("veuillez entrer le nombre des mots que vous voulez faire entrer:  "))
    for i in range(n):
        mots = input("Mot M["+str(i)+ "]: ")
        myFile= open('mots.txt','a')
        myFile.write(mots + '\n')
        myFile.close()



'''def nbre_occurance():
    M=input('Veuillez entrer le mot que vous voulez connaitre son  nombre doccurance   \n ' )
    nbre=0
    with open('mots.txt', 'r') as myFile:
        l=myFile.readline()
        print(l)
        for i in l:
            if (M==l[i]):
                nbre=nbre+1
        return nbre'''

def occurancemot():
    M=input('Veuillez entrer le mot que vous voulez connaitre son  nombre doccurance   \n ' )
    nbr=0
    with open('mots.txt', 'r') as myFile:
        for ligne in myFile:
            liste=ligne.split()
            for i in range(len(liste)):
                if(M.upper()==liste[i].upper()):
                    nbr+=1
    print("Occurrences of the word", M, ":", nbr)


M = input('Veuillez entrer le mot que vous voulez connaitre son  nombre doccurance   \n ')
nbr = 0
with open('mots.txt', 'r') as myFile:
    for ligne in myFile:
        liste = ligne.split()
        print(liste)
        for i in range(len(liste)):
            if (M.upper() == liste[i].upper()):
                nbr += 1
print("Occurrences of the word", M, ":", nbr)







