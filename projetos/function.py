def saudacao(nome):
    return f"Ola {nome}"

def dobro(valor):
    return valor * 2

usuario= "Ana"
mensagem= saudacao(usuario)
print(mensagem)
valor=10
resultado=dobro(valor)
print(f"O dobro de {valor} é {resultado}")