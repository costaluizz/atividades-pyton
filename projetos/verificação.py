idade =int(input("Digite sua idade"))

if idade >= 16 and idade <= 18:
    print("Você ja pode votar")
if idade > 18 and idade <= 70:
    print("Você é obrigado a votar")
if idade < 16 or idade > 70:
    print("Você não é obrigado a votar")     