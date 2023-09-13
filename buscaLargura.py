from no import *


class BuscaLargura:

    def executar(self, no_inicial: No):
        no_inicial.set_cor("Azul")
        fila: list = [no_inicial]
        while len(fila) > 0:
            no_atual = fila.pop(0)
            for no_filho in no_atual.get_adjacentes():
                if no_filho.get_cor() == 'Branco':
                    no_filho.set_cor("Azul")
                    no_filho.set_custo(no_atual.get_custo() + 1)
                    no_filho.set_anterior(no_atual)
                    fila.append(no_filho)

            no_atual.set_cor("Vermelho")

    def percorrer_caminho(self, alvo: No):
        caminho = ']'
        while not (alvo is None):
            caminho = ', ' + alvo.get_nome() + caminho
            alvo = alvo.get_anterior()
        caminho = '[' + caminho
        return caminho
