contador = 0

while contador != 6:
    
    if contador == 6:
        break
    
    contador += 1
    
    entrada = str(input())
    
    a, b = entrada.split(" ")
    
    a = int(a)
    b = int(b)

    resultat = 1
    
    for _ in range(b):
        resultat *= a

    print(resultat)