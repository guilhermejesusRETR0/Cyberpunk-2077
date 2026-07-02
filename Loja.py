from Arma import Arma
from Armadura import Armadura
from Pocao import Pocao


class Loja:
    def __init__(self):
        self.__armaDisponivel = None
        self.__armaduraDisponivel = None
        self.__pocaoDisponivel = None

    def getArmaDisponivel(self):
        return self.__armaDisponivel

    def getArmaduraDisponivel(self):
        return self.__armaduraDisponivel

    def getPocaoDisponivel(self):
        return self.__pocaoDisponivel

    def setArmaDisponivel(self, arma):
        self.__armaDisponivel = arma

    def setArmaduraDisponivel(self, armadura):
        self.__armaduraDisponivel = armadura

    def setPocaoDisponivel(self, pocao):
        self.__pocaoDisponivel = pocao

    def gerarProdutos(self, numeroMasmorra):
        if numeroMasmorra == 1:
            self.__armaDisponivel = Arma("Espada de Ferro", 3, 20)
            self.__armaduraDisponivel = Armadura("Cota de Couro", 2, 18)
            self.__pocaoDisponivel = Pocao("Poção Pequena", 20, 10)

        elif numeroMasmorra == 2:
            self.__armaDisponivel = Arma("Machado Viking", 6, 45)
            self.__armaduraDisponivel = Armadura("Armadura de Malha", 4, 40)
            self.__pocaoDisponivel = Pocao("Poção Média", 35, 25)

        elif numeroMasmorra == 3:
            self.__armaDisponivel = Arma("Espada Flamejante", 9, 75)
            self.__armaduraDisponivel = Armadura("Armadura de Ferro", 7, 70)
            self.__pocaoDisponivel = Pocao("Poção Grande", 50, 40)

        elif numeroMasmorra == 4:
            self.__armaDisponivel = Arma("Lâmina do Eclipse", 13, 110)
            self.__armaduraDisponivel = Armadura("Armadura Real", 10, 100)
            self.__pocaoDisponivel = Pocao("Poção Real", 70, 60)

        else:
            self.__armaDisponivel = Arma("Espada do Núcleo", 18, 160)
            self.__armaduraDisponivel = Armadura("Armadura do Destino", 15, 150)
            self.__pocaoDisponivel = Pocao("Poção do Tempo", 100, 90)

    def mostrarProdutos(self):
        print("\n===== LOJA DO FERREIRO =====")
        print("O ferreiro olha para ti e diz:")
        print('"Não sei o que é um carregador USB-C, mas tenho espadas e outras coisas."')

        print("\n1 - Arma disponível")
        if self.__armaDisponivel is not None:
            self.__armaDisponivel.mostrarDados()
        else:
            print("Nenhuma arma disponível.")

        print("\n2 - Armadura disponível")
        if self.__armaduraDisponivel is not None:
            self.__armaduraDisponivel.mostrarDados()
        else:
            print("Nenhuma armadura disponível.")

        print("\n3 - Poção disponível")
        if self.__pocaoDisponivel is not None:
            self.__pocaoDisponivel.mostrarDados()
        else:
            print("Nenhuma poção disponível.")

    def comprarArma(self, jogador):
        if self.__armaDisponivel is None:
            print("Não há armas disponíveis neste momento.")
            return

        if jogador.gastarMoedas(self.__armaDisponivel.getPreco()):
            jogador.equiparArma(self.__armaDisponivel)
            print(f"Compraste {self.__armaDisponivel.getNome()}!")
        else:
            print("Não tens moedas suficientes para comprar esta arma.")

    def comprarArmadura(self, jogador):
        if self.__armaduraDisponivel is None:
            print("Não há armaduras disponíveis neste momento.")
            return

        if jogador.gastarMoedas(self.__armaduraDisponivel.getPreco()):
            jogador.equiparArmadura(self.__armaduraDisponivel)
            print(f"Compraste {self.__armaduraDisponivel.getNome()}!")
        else:
            print("Não tens moedas suficientes para comprar esta armadura.")

    def comprarPocao(self, jogador):
        if self.__pocaoDisponivel is None:
            print("Não há poções disponíveis neste momento.")
            return

        if jogador.gastarMoedas(self.__pocaoDisponivel.getPreco()):
            jogador.guardarPocao(self.__pocaoDisponivel)
            print(f"Compraste {self.__pocaoDisponivel.getNome()}!")
        else:
            print("Não tens moedas suficientes para comprar esta poção.")

