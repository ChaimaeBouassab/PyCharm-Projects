def tri_selection(l):
    for i in range(len(l)):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j
        l[i],l[min]=l[min],l[i]
    return l


def tri_bull(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def comparer(c1,c2):
    if c1<c2:
        return -1
    elif c1>c2:
        return 1
    else:
        return 0

def saisir(n):
    l=[]
    for j in range(n):
        chaine = input("Veuillez entrer une chaine  :  ")
        l.append(chaine)
    return l

def trier_chaine(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if comparer(liste[j],liste[j+1])>0 :
                liste[j], liste[j + 1] = liste[j+1],liste[j]
    return liste



y=["work","travail","rouge","vert"]
y=trier_chaine(y)
print(y)


