
frequencia=int(input("Digite a frequencia"))

if frequencia <= 6:
    print("Reprovado")
else:

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))



    media = (n1+n2+n3+n4) /4


    if media < 5 or frequencia <=6:
        print("Reprovado!")    

    if media >= 7 and frequencia >= 7:
        print("Aprovado!")

    if media < 7 and  media >= 5 and frequencia >= 7:
        print("Recuperação!")