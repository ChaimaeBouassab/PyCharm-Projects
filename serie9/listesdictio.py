def remplissage(dico):
    dico={}
    notes=[]
    s=0
    module=[]
    for i in range(1):
        nom_prenom=input("Veuillez saisir le nom et le prenom de s["+str(i)+ "]etudiant : \n ")
        for j in range(2):
            module = []
            print('module '+str(j))
            for k in range(2):
                module.append((float(input("donner une note : "))))
            notes.append(module)
        dico[nom_prenom]=notes
        notes=[]

    return  dico





def Moyenne(Notes):
    S=0
    q=len(Notes)
    for i in range(q):
        S=Notes[i]+S
    return S/q


d={}
d=remplissage(d)
print(d)
d2={}
d3={}
for k,v in d.items():
    print("l'etudiante ",k,"a pour moyenne generale", (Moyenne(d[k][1])+Moyenne(d[k][0])/2))
    if( (Moyenne(d[k][1])+Moyenne(d[k][0])/2) >= 10):
        d2[k]=v
        print("le dictionnaire des etudiants qui  ont  valide",d2)
    elif((Moyenne(d[k][1])+Moyenne(d[k][0])/2) <=7):
        d3[k]=v
        print("le dictionnaire des etudiants qui n ont pas valide",d3)

