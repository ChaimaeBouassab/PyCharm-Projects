def remplir(nbre):
    dico={}
    for j in range(nbre):
        name = input("Veuillez entrer le nom :  ")
        pr = input("Veuillez entrer le prenom :  ")
        annee_naissance = int(input("Veuillez entrer annee de naissance:  "))
        email = input("Veuillez entrer le email :  ")
        addresse = input("Veuillez entrer adresse :  ")
        ville = input("Veuillez entrer la ville:  ")
        pays = input("quel est votre pays :  ")
        if name not in dico.values():
            dico['n'] = [name]
            dico['p'] = [pr]
            dico['a'] = [annee_naissance]
            dico['e'] = [email]
            dico['add'] = [addresse]
            dico['v'] = [ville]
            dico['p'] = [pays]
        else:
            print(" a partir du nom que vous avez entrer il apparait que ce contacte existe deja")
    return dico
def rechercher(name,dico):
    d={}
    for i in range(len(dico)):
        if dico[i]['n']==name:
            d=d+[i]
    return d

def afficheeer(dico):
    for C, V in dico.items():
        print("la valeur de la clé ", C, " est égle ", V)

def supprimer_elm(dico,elmsupp):
    remove= dico.pop(elmsupp, None)
    print(remove)
    return remove

def afficherMenu():
    print("-----------------------------------------------------")
    print("Ajouter un contact ....................... A")
    print("Rechercher un contact..................R")
    print("Terminer le programme .............................T")
    print("-----------------------------------------------------")
    choix=input("Veuillez saisir votre choix : ")
    return choix


def main_exo():
    rep = {}
    choix=afficherMenu()
    print("\n")
    while(not(choix=='T' or choix=='t')):
        if(choix=='A' or choix =='a'):
            rep=remplir(2)
        elif(choix=='R' or choix =='r'):
            name=str(input("Veuillez saisir un nom"))
            rechercher(name,rep)
            afficheeer(rep)
        else:
            print("SVP entrer un choix correct")
        choix=afficherMenu()


D={'n': ['bouassab'], 'p': ['espagne'], 'a': [2345], 'e': ['shjdgfjnfd@ewgrdthffn.com'], 'add': ['dthsr'], 'v': ['kenitra']}
D=remplir(1)
print(D)
D=rechercher(['n'],D)
