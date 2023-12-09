class Veiculos:
    def __init__(self,modelo:str,cor:str, ano:int):
        self.__modelo= modelo
        self.__cor= cor
        self.__ano= ano

    def getModelo (self):
        return self.__modelo 
    
    def setModelo (self,novo_valor):
        self.__modelo =novo_valor
        return self.__modelo

    def getCor (self):
        return self.__cor
    
    def setCor (self, novo_valor):
        self.__cor=novo_valor
        return self.__cor
    
    def getAno(self):
        return self.__ano
    
    def setAno(self,novo_valor):
        self.__ano = novo_valor
        return self.__ano
    

    def buzinar (self): 
        return f"Som indefinido"   
    
class Carro (Veiculos):
    def __init__(self, modelo=str, cor=str, ano=int):
        super().__init__(modelo, cor, ano)   
    
    def buzinar(self):
        return "Bi bi"

class Navio (Veiculos):
    def __init__(self, modelo: str, cor: str, ano: int):
        super().__init__(modelo, cor, ano)

    def buzinar (self):
        return "Fommm"

class Aviao (Veiculos):
    def __init__(self, modelo: str, cor: str, ano: int):
        super().__init__(modelo, cor, ano)     


carro1= Carro (modelo= "HB20", cor= "Branco", ano=2022)           
navio1 = Navio (modelo= "Titanic", cor= "Branco Gelo", ano= 1920)
aviao1=Aviao (modelo= "Boing", cor="Branco", ano=2019)

# print (carro1.buzinar())
# print (navio1.buzinar())
# print (aviao1.buzinar())

carro1.setModelo("Uno")

print (carro1.getModelo())
print (carro1.getAno())
print (carro1.getCor())
