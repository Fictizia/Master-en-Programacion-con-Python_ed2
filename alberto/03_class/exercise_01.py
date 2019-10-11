comprobar = True
while comprobar:
    n = int(input('Introduce un número'))
    if n > 0:
        comprobar = False
        i = 2 
        while i < n:
            c = 2
            primo = True
            while primo and c < i:
                if i % c == 0:
                    primo = False
                else:
                    c += 1
        if True:
            print(i, "Es primo")
        i += 1
    else:
        print ("No es correcto, vuelve a intentarlo.")