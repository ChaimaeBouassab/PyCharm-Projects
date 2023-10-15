
def remplir_expres(list):
    Langue = ''
    trad=''
    dico_in={}
    for j in range(len(list)):
        for i in range(3):
            print("Choisissez la langue : \n")
            print("English---------------1\n")
            print("Francais--------------2\n")
            print("Arabe-----------------3\n")
            nbr = input("Entrer :  ")
            switcher={
                 1:"English",
                 2:"Francais",
                 3:"Arabe",
                 }
            trad = input("Entrer le mot : ")
        for trad in dico_in.values():
            print("Elle existe deja")
        else:
            dico_in[nbr] = trad
        list.append(dico_in)
        print(list)
    return list

D=[{'English':'Kind','French':'Gentil'},{'English':'good','French':'bien'}]
D=remplir_expres(D)