
consumo_total_litros=float(input("Informe a quantidade de água consumida pela sua residencia:   "))
numero_moradores=int(input("Informe a quantidade de pessoas que moram com você na mesma residencia:   "))


def avaliar_consumo_familiar(consumo_total_litros,numero_moradores):
    
    if consumo_total_litros / 30 /numero_moradores < 110 :
        print("Consumo Consciente")
    elif consumo_total_litros / 30 /numero_moradores > 110 and consumo_total_litros / 30 /numero_moradores  < 200 :
        print("Consumo Moderado")
    elif consumo_total_litros / 30 /numero_moradores > 200:
        print("Alto Consumo - Atenção Necessario")
    print(f"Consumo medio diario por pessoa:  {consumo_total_litros / 30 /numero_moradores:.2f} litros")
        
if numero_moradores <= 0:
    print("Erro:número de moradores deve ser maior que zero")
else:
    avaliar_consumo_familiar(consumo_total_litros,numero_moradores)