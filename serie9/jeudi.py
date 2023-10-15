def sasir(dico):
    notes=[]
    m=int(input("Veuillez entrer le nombre des etudiants que vous souhaitez d'ajouter:  "))
    for j in range(m):
        nom_prenom=input("Veuillez saisir le nom et le prenom  s["+str(j)+ "] de l'etudiant : \n ")
        classement=int(input("saisir son classement:  "))
        for i in range(3):
            print("notes[",i,"]=",end='')
            notes.append(float(input()))
        dico[nom_prenom] = [notes,classement]
        notes = []
    return dico

def initialiser_Dico():
    D = {}
    return D

def ajouter_element_Dico_1(c, v, D):
    D[c] = v
    return (D)

def reinitialiser_Dico(D):
    D.clear()
    return D


def chercher_Element_Dico_2(v, D):
    for key, value in D.items():
        if v == value:
            return key
        else:
            return None


def chercher_Element_Dico_1(c, D):
    if c in D.keys():
        return D[c]
    else:
        return (None)


def supprimer_element_Dico_1(c, D):
    return (D.pop(c))


def supprimer_element_Dico_2(c, D):
    del D[c]


def supprimer_Dernier_element_Dico(D):
    return (D.popitem())


def supprimer_tous_Les_elements_Dico(D):
    del D

def afficher_Element_Dico(c, v, D):
    print(c, " : ", v)

def Dico_to_Fichier(D, nomFichier):
    f = open(nomFichier, "w")
    f.write(str(D))
    f.close()


def changer_element_Dico_2(c, v, D):
    return (D.update({c: v}))

def saisir_element():
    c = input("Veuillez saisir la clé de votre élément : ")
    v = input("Veuillez saisir la valeur de votre élément : ")
    return c, v



def Menu_Dico():
    return (["0. Créer un dictionnaire",
             "1. Réinitialiser le dictionnaire",
             "2. Ajouter un élément dans un dictionnaire",
             "3. Chercher un élément dans un dictionnaire par sa clé",
             "4. Chercher un élément dans un dictionnaire par sa valeur",
             "5. Supprimer un élément dans un dictionnaire",
             "6. Supprimer le dernier élément d'un dictionnaire",
             "7. Modifier un élément dans un dictionnaire",
             "9. Quitter le programme",
             "8. put the dictionary in a file"
             ])


def Menu(M):
    for i in range(len(M)):
        print(M[i], '\n')
    return (input("Veuillez choisir un nombre entre 0 et " + str(len(M) - 1) + " : "))


def principal():
    while True:
        print('\n', '\n')
        choix = Menu(Menu_Dico())
        if choix == '0':
            Dico={}
            Dico = sasir(Dico)
            print(Dico)
        elif choix == '1':
            Dico = reinitialiser_Dico(Dico)
        elif choix == '2':
            k,v = saisir_element()
            Dico = ajouter_element_Dico_1(k,v, Dico)
            print(Dico)
        elif choix == '3':
            Dico = chercher_Element_Dico_1("girac",Dico)
            print(Dico)
            print("vous avez choisi : ", choix)
        elif choix == '4':
            val = input('Entrez la valeur à chercher pour connaitre sa clé')
            rep = chercher_Element_Dico_2(val, Dico)
            print("la clé de la valeur : ", val, " est : ", rep)
        elif choix == '5':
            print("vous avez choisi : ", choix)
            Dico = supprimer_element_Dico_2('sara', Dico)

        elif choix == '6':
            print("vous avez choisi : ", choix)
            Dico = supprimer_Dernier_element_Dico(Dico)
            print(Dico)

        elif choix == '7':
            print("vous avez choisi : ", choix)
            Dico = changer_element_Dico_2('ouiam', [[5.0, 6.0, 7.0], 4], Dico)
            print(Dico)
        elif choix == '8':
            Dico_to_Fichier(Dico, "hello.txt")
        elif choix == '9':
            print("AU REVOIR")
            break
        else:
            print("Erreur : ", '\n', " recommencez svp et veuillez saisir un nombre entre 0 et 13 : ", '\n')


if __name__ == '__main__':
    # cette partie s'exécute en premier lors de l'execution du programme
    principal()


