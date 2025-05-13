valor_hora=float(input("Informe o valor da hora:  "))

horas_semanas=[]

for i in range(5):
    horas_inserida=float(input("Quantidade de horas  trabalhadas  na dia:  "))

    horas_semanas.append(horas_inserida)

def calcular_total(horas_semanas):

        return sum(horas_semanas)
    
def calcular_pagamento (horas_semanas,valor_hora):
     total = calcular_total(horas_semanas) * valor_hora
     
     print(f"A quantidade de horas trabalhadas foi {calcular_total(horas_semanas)} horas e o valor do pagamento a receber é de R${total:.2f}")

calcular_pagamento (horas_semanas,valor_hora)