


def Dico_to_Fichier(D, nomFichier):
    f = open(nomFichier, "w")
    f.write(str(D))
    f.close()


def Fichier_to_Liste(nomFichier):
    with open(nomFichier, 'r') as f:
        return f.readlines()


def Liste_to_Dico(Liste_Dico):
    if verifie_Si_Dico((Liste_Dico[0].strip())):
        return (Liste_Dico())
    else:
        return (None)


def verifie_Si_Dico(S):
    return S[0] == '{'





def afficher_Element_Dico(c, v, D):
    print(c, " : ", v)


# ________________________________________________________________________________________________________________________
import ast


def Str_to_Dict(String_dico):
    return (ast.literal_eval(String_dico))


def Menu_Dico():
    return (["0. Créer un dictionnaire",
             "1. Réinitialiser le dictionnaire",
             "2. Ajouter un élément dans un dictionnaire",
             "3. Chercher un élément dans un dictionnaire par sa clé",
             "4. Chercher un élément dans un dictionnaire par sa valeur",
             "5. Supprimer un élément dans un dictionnaire",
             "6. Supprimer le dernier élément d'un dictionnaire",
             "7. Modifier un élément dans un dictionnaire",
             "8. Quitter le programme",
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
            Dico = initialiser_Dico()
        elif choix == '1':
            Dico = reinitialiser_Dico(Dico)
        elif choix == '2':
            K, V = saisir_element()
            Dico = ajouter_element_Dico_1(K, V, Dico)
        elif choix == '3':
            Dico = chercher_Element_Dico_2(12, Dico)
            print(Dico)
            print("vous avez choisi : ", choix)
        elif choix == '4':
            val = input('Entrez la valeur à chercher pour connaitre sa clé')
            rep = chercher_Element_Dico_2(val, Dico)
            if rep == None:
                print("Cette valeur n'existe pas")
            else:
                print("la clé de la valeur : ", val, " est : ", rep)
        elif choix == '5':
            print("vous avez choisi : ", choix)
            Dico = supprimer_element_Dico_2('sara', Dico)

        elif choix == '6':
            print("vous avez choisi : ", choix)
            Dico = supprimer_Dernier_element_Dico(Dico)
            print('Dico')

        elif choix == '7':
            print("vous avez choisi : ", choix)
            Dico = changer_element_Dico_2('ouiam', 1889, Dico)

        elif choix == '8':
            print("AU REVOIR")
            break
        else:
            print("Erreur : ", '\n', " recommencez svp et veuillez saisir un nombre entre 0 et 13 : ", '\n')


if __name__ == '__main__':
    # cette partie s'exécute en premier lors de l'execution du programme
    principal()