class Consumivel:
    def __init__(self, nome, danoMinimo, danoMaximo, preco):
        self.__nome = nome
        self.__danoMinimo = danoMinimo if danoMinimo >= 0 else 0
        self.__danoMaximo = danoMaximo if danoMaximo >= self.__danoMinimo else self.__danoMinimo
        self.__preco = preco

    def getNome(self):
        return self.__nome

    def getDanoMinimo(self):
        return self.__danoMinimo

    def getDanoMaximo(self):
        return self.__danoMaximo

    def getPreco(self):
        return self.__preco

    def setNome(self, nome):
        self.__nome = nome

    def setDanoMinimo(self, danoMinimo):
        self.__danoMinimo = danoMinimo if danoMinimo >= 0 else 0
        if self.__danoMaximo < self.__danoMinimo:
            self.__danoMaximo = self.__danoMinimo

    def setDanoMaximo(self, danoMaximo):
        self.__danoMaximo = danoMaximo if danoMaximo >= self.__danoMinimo else self.__danoMinimo

    def setPreco(self, preco):
        self.__preco = preco

    def mostrarDados(self):
        print("Consumivel:", self.__nome)
        print("Dano minimo:", self.__danoMinimo)
        print("Dano maximo:", self.__danoMaximo)
        print("Preco:", self.__preco, "creditos")
