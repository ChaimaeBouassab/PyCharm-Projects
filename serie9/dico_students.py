def remplissage(dico):
    dict={}
    notes=[]
    s=0
    for j in range(2):
        nom_prenom=input("Veuillez saisir le nom et le prenom de s["+str(j)+ "]stagiaire : \n ")
        classement=int(input("saisir son classement"))
        for i in range(3):
            print("notes[",i,"]=",end='')
            notes.append(float(input()))
        for i in range(len(notes)):
            s=s+notes[i]
            z=s/len(notes)
        dico[nom_prenom]=[notes,z,classement]
        notes=[]
    return  dico
def affichage(d):
    for k,v in d.items():
        print("la valeur de cle",k,"est",v)

def saisir_Nom():
  return input("Entrer le nom dun stagiaire : ")

def consulter(dic,N):
    print("le stagiaire ",N," a un classement de ", dic[N][2])



D={}
D=remplissage(D)
print(D)
consulter(D,saisir_Nom())
affichage(D)



