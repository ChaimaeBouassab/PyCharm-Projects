def liste_entiers(l):
    n = int(input("entrer la taille : "))
    l = []
    for i in range(n):
        print("l[", i, "]=", end='')
        l.append(int(input()))
    return l



def ensembles(ll):
    E = []
    ll = []

    ll = liste_entiers(ll)
    for i in ll:
        if i not in E:
            E.append(i)
    ll = E
    return ll

def intersection(A,B):
    c=[]
    for i in A:
        if (i in B) and (i not in c):
            c.append(i)
    return c

def union(A,B):
    c=[]
    for i in A:
        c.append(i)
        for i in B:
            if i in  B and (i not in c):
                c.append(i)
    return c


def difference(A,B):
    c=[]
    for i in A:
        c.append(i)
        for i in B:
            if i not in B:
                c.append(i)
    return c



A=[3,5,4]
B=[4,9,8]
'''k = []
k = ensembles(k)
print('ensemble est', k)'''
ff=difference(A,B)
print(ff)