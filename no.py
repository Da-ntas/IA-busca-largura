from future.types import no


class No:
    def __init__(self, nome: str):
        # variaveis privadas
        self.nome: str = nome
        self.cor: str = "Branco"
        self.custo: float = 0
        self.anterior: no = None
        self.adjacentes = None

    # Métodos 'get' para cada atributo

    def get_cor(self):
        return self.cor

    def get_custo(self):
        return self.custo

    def get_anterior(self):
        return self.anterior

    def get_adjacentes(self):
        return self.adjacentes

    def get_nome(self):
        return self.nome

    # Métodos 'set' para cada atributo

    def set_cor(self, cor: str):
        self.cor = cor

    def set_custo(self, custo: float):
        self.custo = custo

    def set_anterior(self, anterior: no):
        self.anterior = anterior

    def set_nome(self, nome: str):
        self.nome = nome

    def set_adjacentes(self, adjacentes: list):
        self.adjacentes = adjacentes
