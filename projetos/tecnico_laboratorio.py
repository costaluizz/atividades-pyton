temperatura = int(input("Informe a temperatura da incubadora:  "))
ph = float(input("Informe  o ph da solução da incubadora:  "))
tempo =float(input("Informe o tempo de incubação em horas:  "))

if temperatura >= 36 and temperatura <= 38 and ph >= 6.5 and ph <= 7.5 and tempo >= 18 and tempo <= 24:
    print("As condiçãoes estão ideais, todos os requisitos foram atendidos")
elif  temperatura >= 36 and temperatura <= 38 or ph >= 6.5 and ph <= 7.5 or  tempo >= 18 and tempo <= 24:
    print("Apenas um ou duas condições foram atendidas")
else:
    print("Todas as condições estão fora do ideal")