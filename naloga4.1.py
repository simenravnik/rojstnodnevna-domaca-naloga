niz = input("Napisite stavek: ")
niz2 = ""
niz = niz.lower()
niz = niz.replace(" ","")

niz2 = niz[::-1]

if niz == niz2:
    print ("Stavek je palindrom.")
else:
    print ("Stavek ni palindrom.")
