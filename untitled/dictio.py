def dictionary(l):
    d = dict()

    for a in l:
        if a % 2 == 0:
           d[a] = 'Pair'
        else:
            d[a] = 'Impair'
    return d

l=[5,2]

print(dictionary(l))