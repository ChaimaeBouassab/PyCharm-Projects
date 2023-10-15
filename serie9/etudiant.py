def Moyenne(Notes):
    M=0
    S=0
    for i in range(len(Notes)):
        S=Notes[i]+S
    return S/len(Notes)


dico={}
CNE=''
NOTES=[]
CNE=input("Veuillez entrer le cne de l etudiant :  ")
print("entrer les notes")
for i in range(3):
        v=float(input("Saisir une Note : "))
        NOTES.append(v)
dico[CNE]=NOTES
for cle,valeur in dico.items():
    print(cle , Moyenne(valeur))






