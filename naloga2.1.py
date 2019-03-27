#preveri ali je stevilo prastevilo

n = int(input("Vpisite pozitivno celo stevilo: "))

i = 1
for i in range (2,n):
    if n % i == 0:
        print("Stevilo " + str(n) + " ni prastevilo.")
        break

if i == n-1:
    print("Stevilo " + str(n) + " je prastevilo.")
else:
    print("Stevilo " + str(n) + " ni prastevilo.")
