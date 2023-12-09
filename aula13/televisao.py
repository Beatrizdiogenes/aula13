class Televisao:
    def __init__(self,nome=str, genero=str):
        self.nome = nome
        self.genero = genero

    def assistir(self):
        return f"Você está assistindo {self.nome}"    
    
class Filmes (Televisao):
    def __init__(self, nome=str, genero=str,horas_duracao= int):
        super().__init__(nome, genero)
        self.horas_duracao = horas_duracao

    def em_cartaz (self):
        return f"O filme {self.nome} está em cartaz"    

class Series (Televisao):
    def __init__(self, nome=str, genero=str,num_temporadas=int):
        super().__init__(nome, genero)    
        self.num_temporadas=num_temporadas

    def maratonar (self):
        return f"A série {self.nome} está sendo maratonada" 

nome_filme =str(input("Digite o nome do filme: "))
genero_filme= str (input("Digite o gênero do filme:"))
duracao_filme = float (input("Qual o tempo duração do filme?: "))

filme1=Filmes (nome=nome_filme, genero=genero_filme,horas_duracao=duracao_filme)

print(filme1.em_cartaz())

nome_serie =str(input("Digite o nome do série: "))
genero_serie= str (input("Digite o gênero do série:"))
num_temporadas = int (input ("Digite a quantidade de temporadas existentes: "))

serie1 = Series (nome= nome_serie, genero= genero_serie, num_temporadas=duracao_filme)

print (serie1.maratonar())