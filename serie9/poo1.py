import pickle
import os

T = []
class Utilisateur:
    def __init__(self, nom, prenom, compte, pwd):
        self.nom = nom
        self.prenom = prenom
        self.compte = compte
        self.pwd = pwd

    ########################################################
    ########### FONCTION POUR CHERCHER LE DOUBLANT##########
    ########################################################
    def recherche(user):
        for i in range(len(T)):
            if T[i].compte == user:
                return i
        return -1

    ########################################################
    # FONCTION créer et retouner un objet UN UTILISATEUR
    ########################################################
    def nouveaucompte():
        user = input('Donnez le compte :')
        while Utilisateur.recherche(user) != -1:
            user = input("Le compte est déjà utilisé, Entrez un autre compte :")

        n = input('Donnez votre nom :')
        p = input('Donnez votre prenom :')
        pwd = input('Donnez votre mot de passe :')
        S = Utilisateur(n, p, user, pwd)
        return S

    def creercompte():
        S2 = Utilisateur.nouveaucompte()
        T.append(S2)
        print('Le compte est ajouté avec success')
        Utilisateur.majTableauToFichier()

    ########################################################
    # FONCTION POUR SUPPRIMER UN UTILISATEUR DU TABLEAU T#
    ########################################################
    def supprimerCompte():
        compte = input("Entrez le copmte")
        if Utilisateur.recherche(compte) != -1:
            del T[Utilisateur.recherche(compte)]
            print('Le compte est supprimé avec success')
        else:
            print('Le compte est introuvable')

        Utilisateur.majTableauToFichier()

    ########################################################
    # FONCTION POUR MODIFIER UN UTILISATEUR DU TABLEAU T#
    ########################################################
    def modification():
        user1 = input('Donner le compte à modifier :')
        while Utilisateur.recherche(user1) == -1:
            user1 = input("Le comte saisie n'existe pas donner un compte existant")

        user2 = input("Donner le nouveau compte :")
        while Utilisateur.recherche(user2) != -1:
            user2 = input("Le compte saisi est dejà utilisé par un autre utilisateur, Donner un autre  compte :")

        nom = input('Donner le nouveau nom :')
        prenom = input('Donner le nouveau prenom :')
        mdp = input('Donner le nouveau mot de passe :')
        x = Utilisateur(nom, prenom, user2, mdp)
        T[Utilisateur.recherche(user1)] = x
        Utilisateur.majTableauToFichier()
        print('Le compte est modifié avec success')

    ########################################################
    # FONCTION REMPLIR UN TABLEAU A PARTIR D'UN FICHIER#####
    ########################################################
    def FichierToTableau():
        T.clear()
        try:
            f = open('Users.dat', 'rb')
            u = pickle.load(f)
            for i in range(len(u)):
                T.append(u[i])
            f.close()
        except EOFError:
            print('Fichier vide')
        except FileNotFoundError:
            print('Fichier introuvable')
            f = open('Users.dat', 'wb')
        except IOError:
            print("Erreur d'entree et de sortie")

    ########################################################
    # FONCTION REMPLI LE FICHIER AVEC LES DONNEES DU TABLEAU#
    ########################################################

    def majTableauToFichier():
        f = open('Users.dat', 'wb')
        pickle.dump(T, f)
        f.close()

    ########################################################
    # FONCTION TOUS LES ELEMENT DU TABLEAU##################
    ########################################################
    def printT():
        Utilisateur.FichierToTableau()

