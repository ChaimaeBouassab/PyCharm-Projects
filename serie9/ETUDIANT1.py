def Moyenne(Notes):
    S=0
    q=len(Notes)
    for i in range(q):
        S=Notes[i]+S
    return S/q


def remplir(nbre):
    CNE = ''
    NOTES = []
    dico1={}
    dico={}
    for j in range(nbre):
        CNE = input("Veuillez entrer le cne de l etudiant :  ")
        for i in range(3):
            v = float(input("NOTES[" + str(i) + "]= "))
            NOTES.append(v)
        n = Moyenne(NOTES)
        dico[CNE] = NOTES,Moyenne(NOTES)
        NOTES=[]
    return dico
'''
def trier_note(dico):
    dico={}
    s={k : v for k , v in sorted(dico.items())}
    print(dico)
    return dico
'''
'''def rechercher_parCNE(dico,cne):
    b= -1
    for k in dico.keys():
        if cne==k:
            b=1
            break
    if b==-1:
        print(" ce cne n'existe pas ")'''

def rechercherparCNE(dico,cne):
    if cne in dico.keys():
        return  1
    else:
        return  -1



D={}
D=remplir(2)
print(D)






