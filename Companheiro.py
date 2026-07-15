class Companheiro:
    def __init__(
        self,
        nome,
        papel,
        descricao,
        preco,
        arquivo,
        bonusAtaque=0,
        bonusVidaMaxima=0,
        bonusCura=0,
        bonusCritico=0,
        bonusExperiencia=0
    ):
        self.__nome = nome
        self.__papel = papel
        self.__descricao = descricao
        self.__preco = preco
        self.__arquivo = arquivo
        self.__bonusAtaque = bonusAtaque
        self.__bonusVidaMaxima = bonusVidaMaxima
        self.__bonusCura = bonusCura
        self.__bonusCritico = bonusCritico
        self.__bonusExperiencia = bonusExperiencia

    def getNome(self):
        return self.__nome

    def getPapel(self):
        return self.__papel

    def getDescricao(self):
        return self.__descricao

    def getPreco(self):
        return self.__preco

    def getArquivo(self):
        return self.__arquivo

    def getBonusAtaque(self):
        return self.__bonusAtaque

    def getBonusVidaMaxima(self):
        return self.__bonusVidaMaxima

    def getBonusCura(self):
        return self.__bonusCura

    def getBonusCritico(self):
        return self.__bonusCritico

    def getBonusExperiencia(self):
        return self.__bonusExperiencia

    def mostrarDados(self):
        print(f"{self.__nome} - {self.__papel}")
        print(self.__descricao)
        print("Preço:", self.__preco, "créditos")
        if self.__bonusAtaque:
            print("Bónus de ataque:", self.__bonusAtaque)
        if self.__bonusVidaMaxima:
            print("Bónus de vida máxima:", self.__bonusVidaMaxima)
        if self.__bonusCura:
            print("Bónus de cura:", self.__bonusCura)
        if self.__bonusCritico:
            print("Bónus de dano crítico:", self.__bonusCritico)
        if self.__bonusExperiencia:
            print("Bónus de experiência:", self.__bonusExperiencia)
