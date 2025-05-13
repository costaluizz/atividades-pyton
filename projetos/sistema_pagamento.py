from abc import ABC, abstractmethod

class Pagamento (ABC):
    def __init__(self,valor):
        self.valor= valor 

    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self,valor, numero_cartao,cvv):
        super().__init__(valor)
        self.numero_cartao = numero_cartao
        self.cvv = cvv

    def processar_pagamento(self):
        if len(self.numero_cartao) == 16 and len(self.cvv) == 3:
            print("Pagamento Processado com cartão")
        else:
            print("Erro:Pagamento não processado com cartão")

class BoletoBancario(Pagamento):
    def __init__ (self,valor,cpf_cliente):
        super().__init__(valor)
        self.cpf_cliente = cpf_cliente
    
    def processar_pagamento(self):
        print(f"Boleto com vencimento de tres dias,gerado no cpf:  {self.cpf_cliente}")

class Pix(Pagamento):
    def __init__(self, valor,chave_pix):
        super().__init__(valor)
        self.chave_pix = chave_pix
    
    def processar_pagamento(self):
        print(f"Pagamento instantaneo confirmado na chave pix: {self.chave_pix}")


pagamentos =[CartaoCredito(100,"1234567891234567","123"),  
            BoletoBancario(500,"800.450.340-80"),
            Pix(100,"6399801000")]

for pagamento in pagamentos:
    pagamento.processar_pagamento()

        

    

    
        
