#soda fibonaccijeva stevila

a = 1
b = 1

while (b < 100):
    c = b
    b = a + c
    a = c

    if a % 2 == 0:
        print(a)
