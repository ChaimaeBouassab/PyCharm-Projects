t=[5,10,8,9,44,23,98]
b=True
for i in range(len(t)-1):
    if t[i] > t[i+1]:
       b=False
       break
if(b==True):
    print("it is sorted")
else:
    print("it is nooot  sorted")