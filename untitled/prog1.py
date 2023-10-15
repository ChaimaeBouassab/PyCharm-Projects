l1=[]
l2=[]
for i in range(3):
    x=float(input('donner des valeurs'))
    l1.append(x)
for j in range(3):
    x=float(input('donner des valeurs'))
    l2.append(x)
b = False
for i in range(3):
  for j in range(3):
          if(l1[i]==l2[j]):
              b = True
              break
if (b == True):
    print("il y a un element commun ")
else:
   print("il y a pas ")