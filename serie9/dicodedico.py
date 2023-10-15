def remplir_expres(l):
    Langue = ''
    trad=''
    dico_in={}
    for j in range(len(l)):
        for i in range(3):
            Langue = input("Veuillez entrer la langue pour afficher traduction de lexpression :  ")
            trad = input("Veuillez entrer  sa traduction en cette langue : ")
        for trad in dico_in.values():
            print("Elle existe deja")
        else:
            dico_in[Langue] = trad
        l.append(dico_in)
        print(l)
    return l



def chercher(dico):
    Nouveau=input("Entrez lexpression que vous cherchez  : ")
    ca=dico.copy()
    if Nouveau in  dico.keys():
        print(dico)

'''def rechercher(dico,expression):
    b= -1
    for k in dico.keys():
        if cne==k:
            b=1
            break
    if b==-1:
        print(" cet esxpression  n'existe pas ")'''

D=[{'English':'Kind','French':'Gentil'},{'English':'good','French':'bien'}]
D=remplir_expres(D)
filename = "dict.txt"
with open(filename, mode='w') as f:
    f.write(str(D))
filename = open("dict.txt", "r+")

print("le contenu est : ")
print(filename.read())
print()