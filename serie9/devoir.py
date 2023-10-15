def ajouter_increm(dic):
    Produit=''
    quantite =0
    Produit=input("Veuillez sasir un produit : ")
    quantite=int(input("Entrer sa quantite : "))
    if Produit in dic.keys():
        dic[Produit]=  dic[Produit]+quantite
    else:
        dic[Produit] = quantite
    return dic



def ajouter_verifier(dic):
    Produit=''
    quantite =0
    Produit=input("Veuillez sasir un produit : ")
    quantite=int(input("Entrer sa quantite : "))
    if Produit in dic.keys():
        dic[Produit].append(quantite)
    else:
        dic[Produit] = [quantite]
    return dic

def supprimer_elm(dico,elmsupp):
    remove= dico.pop(elmsupp, None)
    print(remove)
    return remove

def supprimer_parvaleur(dico):
    elmsupp=input("Veuillez sasir element que vous voulez supprimer : ")
    qte=int(input("Entrer sa quantite : "))
    if elmsupp in dico.keys():
        if qte in dico[elmsupp]:
            dico[elmsupp].remove(qte)
        else:
            dico.pop(elmsupp,None)
    return dico


def chercher_modifier(dico):
    Nouveau=input("Entrez un nouveau Produit : ")
    produit=input("Entrez  Produit  qui sera remplacer par le Nouveau: ")
    ca=dico.copy()
    if produit in  dico.keys():
        dico[produit]=Nouveau
        print(dico)

lesproduits={"Livres":[19,7,8], "Stylos":[7], "Cartables":[18]}
lesproduits=ajouter_verifier(lesproduits)
print(lesproduits)
lesproduits=ajouter_increm(lesproduits)
print(lesproduits)
lesproduits=supprimer_parvaleur(lesproduits)
print(lesproduits)
