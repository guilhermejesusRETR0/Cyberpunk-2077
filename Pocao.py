
class Pocao:
    def __init__(self, nome, valorCura, preco):
        self.__nome = nome
        self.__valorCura = valorCura
        self.__preco = preco

    def getNome(self):
        return self.__nome

    def getValorCura(self):
        return self.__valorCura

    def getPreco(self):
        return self.__preco

    def setNome(self, nome):
        self.__nome = nome

    def setValorCura(self, valorCura):
        self.__valorCura = valorCura

    def setPreco(self, preco):
        self.__preco = preco

    def mostrarDados(self):
        print("Poção:", self.__nome)
        print("Valor de cura:", self.__valorCura)
        print("Preço:", self.__preco, "moedas")
