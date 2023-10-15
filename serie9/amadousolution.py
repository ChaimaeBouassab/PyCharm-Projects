def saveData():
    event = input("Évènement: ")
    number_of_days = int(input("Nombre des jours: "))
    date_of_holiday = input("Date des vacances: ")

    with open('data.txt', 'a+') as file:
        file.write(event)
        file.write(f' - {number_of_days}')
        file.write(f' - {date_of_holiday}\n')
        file.close()


def loadData():
    print("Évènement - Nombre des jours - Date des vacances")
    with open('data.txt', 'r+') as file:
        tab = file.readlines()
        print(tab)
        for i in tab:
            print(i)
        file.close()


def start():
    print("1 - Enregistrer des évènements")
    print("2 - Voir les évènements")
    print("0 - Quitter")

    options = int(input("Choisir: "))
    if options == 1:
        saveData()
        start()
    elif options == 2:
        loadData()
        print("0 - Retourner")
        options_in = int(input("Choisir: "))
        if options_in == 0:
            start()
    elif options == 0:
        return


start()
