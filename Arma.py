class Arma:
    def __init__(self, nome, bonusAtaque, preco):
        self.__nome = nome
        self.__bonusAtaque = bonusAtaque
        self.__preco = preco

    def getNome(self):
        return self.__nome

    def getBonusAtaque(self):
        return self.__bonusAtaque

    def getPreco(self):
        return self.__preco

    def setNome(self, nome):
        self.__nome = nome

    def setBonusAtaque(self, bonusAtaque):
        self.__bonusAtaque = bonusAtaque

    def setPreco(self, preco):
        self.__preco = preco

    def mostrarDados(self):
        print("Arma:", self.__nome)
        print("Bónus de ataque:", self.__bonusAtaque)
        print("Preço:", self.__preco, "moedas")

