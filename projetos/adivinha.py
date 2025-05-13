import random

numero_sorteado = random.randint(1,10)

numero = int(input("Adivinhe o numero entre 1 e 10: "))

while numero != numero_sorteado:
    if numero < numero_sorteado:
        print("Numero baixo")
    elif numero > numero_sorteado:
        print("Numero  Alto")
        
    print("Errado, tente outra vez! ")
    numero = int(input("Adivinhe o numero entre 1 e 10:"))

print("Parabens ,voce acertou!")
