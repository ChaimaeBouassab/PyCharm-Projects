
def palindrome(c):
    r=c[::-1]
    if (r== c):
        print("palindrome")
    else:
        print("nom ")


p='abccba'
print(p[::-1])
palindrome(p)