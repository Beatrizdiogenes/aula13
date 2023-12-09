class Funcionarios:
    def __init__(self,nome:str, cpf:int, endereco:str, salario:float):
        self.__nome= nome
        self.__cpf = cpf
        self.__endereco=endereco
        self.__salario = salario

    def getNome(self):
        return self.__nome

    def setNome (self,novo_valor):
        self.__nome= novo_valor
        return self.__nome   
    
    def getCpf(self):
        return self.__cpf
    
    def setCpf (self,novo_valor):
        self.__cpf= novo_valor
        return self.__cpf  

    def getEndereco(self):
        return self.__endereco
    
    def setEndereco (self,novo_valor):
        self.__endereco= novo_valor
        return self.__endereco 
    
    def getSalario(self):
        return self.__salario
    
    def setSalario (self,novo_valor):
        self.__salario= novo_valor
        return self.__salario

    def bater_ponto(self):
        return f"O {self.getNome()} bateu o ponto"
    
class Caixa(Funcionarios):
    def __init__(self, nome: str, cpf: int, endereco: str, salario: float, num_do_caixa:int):
        super().__init__(nome, cpf, endereco, salario)
        self.__num_do_caixa=num_do_caixa

    def getNum_do_caixa(self):
        return self.__num_do_caixa
    
    def setNum_do_caixa (self,novo_valor):
        self.__num_do_caixa= novo_valor
        return self.__num_do_caixa
    
    def bater_ponto(self):
        return f"O caixa {self.getNome()} bateu o seu ponto"

    def fechar_caixa (self):
        return f"O {self.getNome()} fechou o caixa {self.getNum_do_caixa}"
    
    
class Vendedor (Funcionarios):
    def __init__(self, nome: str, cpf: int, endereco: str, salario: float,comissao:float):
        super().__init__(nome, cpf, endereco, salario)   
        self.__comissao=comissao

    def getComissao(self):
        return self.__comissao
    
    def setComissao(self,novo_valor):
        self.__comissao= novo_valor
        return self.__comissao

    def realizar_venda (self,valor_da_venda):
        return f"O{self.getNome} realizou uma venda e ganhou {self.getComissao() * valor_da_venda}"
    
caixa1= Caixa (nome="Maria", cpf=123, endereco="bem ali", salario=1500, num_do_caixa=5)
vendedor1= Vendedor (nome="Ana",cpf= 123, endereco= "Aculá", salario=2500, comissao=0.2)

print(caixa1.fechar_caixa())
print (caixa1.getCpf())
vendedor1.setEndereco ("Bem aqui")
print (vendedor1.realizar_venda(5000))