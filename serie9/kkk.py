def Moyenne(Notes):
    M = 0
    S = 0
    for i in range(len(Notes)):
        S = Notes[i] + S
    return S / len(Notes)


def remplir(nbre):
    nom = ''
    NOTES = []
    dico = {}

    for j in range(nbre):
        nom = input("Veuillez entrer le nom de l etudiant :  ")
        for i in range(3):
            v = float(input("NOTES[" + str(i) + "]= "))
            NOTES.append(v)
        m = Moyenne(NOTES)
        dico[nom] = [NOTES, m]
        NOTES = []


D = {}
D = remplir(2)
print(D)