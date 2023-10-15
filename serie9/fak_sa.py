def Dico_to_Fichier(D, nomFichier):
    f = open(nomFichier, "w")
    f.write(str(D))
    f.close()

details = {'Name': "Alice",
           'Age': 21,
           'Degree': "Bachelor Cse",
           'University': "Northeastern Univ"}

Dico_to_Fichier(details, "hello.txt")