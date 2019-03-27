#izpise vsa prastevila od 1 - 100

i = 1

for n in range (1,101):
    for i in range (2,n):
        if n % i == 0:
            #print("Stevilo " + str(n) + " ni prastevilo.")
            break

    if i == n-1:
        print(n)
