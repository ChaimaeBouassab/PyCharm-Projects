ListeVacance=[[12,'Rabii I',1443,'Aid Al MAwlid',2], [6,'Novembre',2021,'La marche Verte',1],[6,'Fevrier',2022,'Vacance du 2eme semestre',8],
[14,'Mars',2022,'Vacance du 3eme semestre',8], [1,'Mai',2022,'Fete du travail',1],
[29,'Ramadan',1443,'Aid alfitr',3], [8,'Di alhija',1443,'Aid aladha',4]]

def save_data():
    f = open('data.txt', 'wt')
    for item in ListeVacance:
        f.write(str(item[0])+"-"+item[1]+"-"+str(item[2])+"-"+item[3]+"-"+str(item[4])+"\n")
    f.close()

def NbreJoursTotalVacances():
    f=open('data.txt','rt')
    L=f.readlines()
    print(L)
    s=0
    for v in L:
        l=v.split('-')
        s+=int(l[4])
        return s
        print("Total:",NbreJoursTotalVacances())


save_data()
d=NbreJoursTotalVacances()