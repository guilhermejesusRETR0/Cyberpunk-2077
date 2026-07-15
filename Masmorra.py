
class Masmorra:
    def __init__(self, numero, nome, descricao, caminhos=None):
        self.__numero = numero
        self.__nome = nome
        self.__descricao = descricao
        self.__caminhos = list(caminhos) if caminhos is not None else []

    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    def getDescricao(self):
        return self.__descricao

    def getCaminhos(self):
        return list(self.__caminhos)

    def setNumero(self, numero):
        self.__numero = numero

    def setNome(self, nome):
        self.__nome = nome

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setCaminhos(self, caminhos):
        self.__caminhos = list(caminhos) if caminhos is not None else []

    def mostrarInfo(self):
        print("\n===== ZONA ATUAL =====")
        print("Número:", self.__numero)
        print("Nome:", self.__nome)
        print("Descrição:", self.__descricao)
        if self.__caminhos:
            print("Caminhos possiveis:", ", ".join(str(caminho) for caminho in self.__caminhos))
        else:
            print("Caminhos possiveis: nenhum")
