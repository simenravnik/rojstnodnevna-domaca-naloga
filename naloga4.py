#preveri ali je palindrom
niz = input("Napisite stavek: ")
niz2 = ""
niz = niz.lower()
niz = niz.replace(" ","")

for i in range (len(niz),0,-1):
    niz2 = niz2 + niz[i-1]

if niz == niz2:
    print ("Stavek je palindrom.")
else:
    print ("Stavek ni palindrom.")
