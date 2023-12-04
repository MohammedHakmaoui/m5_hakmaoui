contador = 0

while contador != 6:
    entrada = input("Introdueix dos números: ")
    
    a, b = map(int, entrada.split(" "))
    
    if not (isinstance(a, int) and isinstance(b, int)):
        print("Error")
        continue

    resultat = 1
    for _ in range(b):
        resultat *= a

    print(f"El resultat de {a}^{b} es: {resultat}")
    
    contador += 1
