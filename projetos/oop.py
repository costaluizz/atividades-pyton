
class Usuario:
    def __init__(self,user_name,id,email):
        self.user_name=user_name
        self.id = id
        self.email=email
        self.status = False

    def cumprimentar(self):
       return f"Olá,meu usuario é {self.user_name} e tenho ID{self.id} "
    
    def ativarUsuario(self):
        if not self.status:
          self.status = True
          return f"{self.user_name}agora seu usuario está Ativo."
        return "O usuário já está ativo"
    
#Criando um objeto da classe 'Pessoa'
user1 = Usuario("maria12376",4,"maria123@gmail.com")

#Usando os métodos da classe
print(user1.cumprimentar())
print(user1.ativarUsuario())
print(user1.ativarUsuario())


    
