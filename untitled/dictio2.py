def diviseur(n):
  l=[]
  for i in range(1,n+1):
      if n%i==0:
          l.append(i)
  return l


print(diviseur(4))

def dicte(l):
    d = dict()
    for a in l:
        d[a]= diviseur(a)
    return d

l=[5,2]
print( dicte(l))


