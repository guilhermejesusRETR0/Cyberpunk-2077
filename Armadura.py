class Armadura:
    def __init__(self, nome, bonusDefesa, preco):
        self.__nome = nome
        self.__bonusDefesa = bonusDefesa
        self.__preco = preco

    def getNome(self):
        return self.__nome

    def getBonusDefesa(self):
        return self.__bonusDefesa

    def getPreco(self):
        return self.__preco

    def setNome(self, nome):
        self.__nome = nome

    def setBonusDefesa(self, bonusDefesa):
        self.__bonusDefesa = bonusDefesa

    def setPreco(self, preco):
        self.__preco = preco

    def mostrarDados(self):
        print("Blindagem:", self.__nome)
        print("Bónus de defesa:", self.__bonusDefesa)
        print("Preço:", self.__preco, "créditos")

