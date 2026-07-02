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
            self.__armaDisponivel = Arma("Lâmina de rua", 3, 20)
            self.__armaduraDisponivel = Armadura("Colete de fibra", 2, 18)
            self.__pocaoDisponivel = Pocao("BioGel básico", 20, 10)

        elif numeroMasmorra == 2:
            self.__armaDisponivel = Arma("Rifle eletromagnético", 6, 45)
            self.__armaduraDisponivel = Armadura("Blindagem de rede", 4, 40)
            self.__pocaoDisponivel = Pocao("Estimulante", 35, 25)

        elif numeroMasmorra == 3:
            self.__armaDisponivel = Arma("Katana mono-fio", 9, 75)
            self.__armaduraDisponivel = Armadura("Exoesqueleto leve", 7, 70)
            self.__pocaoDisponivel = Pocao("Reparador de implantes", 50, 40)

        elif numeroMasmorra == 4:
            self.__armaDisponivel = Arma("Canhão de pulso", 13, 110)
            self.__armaduraDisponivel = Armadura("Armadura de dados", 10, 100)
            self.__pocaoDisponivel = Pocao("Nano kit premium", 70, 60)

        else:
            self.__armaDisponivel = Arma("Arma do núcleo", 18, 160)
            self.__armaduraDisponivel = Armadura("Blindagem de emergência", 15, 150)
            self.__pocaoDisponivel = Pocao("Reparador de IA", 100, 90)

    def mostrarProdutos(self):
        print("\n===== MERCADO NEGRO =====")
        print("O vendedor olha para ti como quem já viu pior. Talvez até viu a tua cara em outro cadáver.")
        print('"Se és capaz de pagar, és capaz de sobreviver. O resto é propaganda."')

        print("\n1 - Arma disponível")
        if self.__armaDisponivel is not None:
            self.__armaDisponivel.mostrarDados()
        else:
            print("Nenhuma arma disponível.")

        print("\n2 - Blindagem disponível")
        if self.__armaduraDisponivel is not None:
            self.__armaduraDisponivel.mostrarDados()
        else:
            print("Nenhuma blindagem disponível.")

        print("\n3 - Nano kit disponível")
        if self.__pocaoDisponivel is not None:
            self.__pocaoDisponivel.mostrarDados()
        else:
            print("Nenhum nano kit disponível.")

    def comprarArma(self, jogador):
        if self.__armaDisponivel is None:
            print("Não há armas disponíveis neste momento. A cidade está a economizar munições, como sempre.")
            return

        if jogador.gastarMoedas(self.__armaDisponivel.getPreco()):
            jogador.equiparArma(self.__armaDisponivel)
            print(f"Compraste {self.__armaDisponivel.getNome()}!")
        else:
            print("Não tens créditos suficientes para comprar esta arma. A tua conta está mais seca do que um beco sem rede.")

    def comprarArmadura(self, jogador):
        if self.__armaduraDisponivel is None:
            print("Não há blindagens disponíveis neste momento. Até o ferro está a fazer greve.")
            return

        if jogador.gastarMoedas(self.__armaduraDisponivel.getPreco()):
            jogador.equiparArmadura(self.__armaduraDisponivel)
            print(f"Compraste {self.__armaduraDisponivel.getNome()}!")
        else:
            print("Não tens créditos suficientes para comprar esta blindagem. O teu orçamento já não faz frente ao teu medo.")

    def comprarPocao(self, jogador):
        if self.__pocaoDisponivel is None:
            print("Não há nano kits disponíveis neste momento. A medicina de rua custa mais do que a dignidade.")
            return

        if jogador.gastarMoedas(self.__pocaoDisponivel.getPreco()):
            jogador.guardarPocao(self.__pocaoDisponivel)
            print(f"Compraste {self.__pocaoDisponivel.getNome()}!")
        else:
            print("Não tens créditos suficientes para comprar este nano kit. O teu corpo vai ter de aprender a sobreviver à própria má sorte.")

