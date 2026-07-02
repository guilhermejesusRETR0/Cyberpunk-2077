
class Masmorra:
    def __init__(self, numero, nome, descricao):
        self.__numero = numero
        self.__nome = nome
        self.__descricao = descricao

    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    def getDescricao(self):
        return self.__descricao

    def setNumero(self, numero):
        self.__numero = numero

    def setNome(self, nome):
        self.__nome = nome

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def mostrarInfo(self):
        print("\n===== ZONA ATUAL =====")
        print("Número:", self.__numero)
        print("Nome:", self.__nome)
        print("Descrição:", self.__descricao)
