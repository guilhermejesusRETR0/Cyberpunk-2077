# ============================================================
# CLASSE POCAO (MaxDoc)
# Representa um item de cura. No jogo, aparece com o nome "MaxDoc".
# Quando usada em combate, recupera vida ao jogador e é gasta
# (removida do inventário) logo a seguir.
# ============================================================

class Pocao:

    def __init__(self, nome, valorCura, preco):
        # Construtor: cria uma nova poção/MaxDoc.
        # Exemplo de uso: Pocao("MaxDoc Mk2", 39, 24)
        self.__nome = nome            # Nome do item (texto)
        self.__valorCura = valorCura  # Quantos pontos de vida recupera
        self.__preco = preco          # Quanto custa em créditos

    # ---------- GETTERS ----------

    def getNome(self):
        return self.__nome

    def getValorCura(self):
        return self.__valorCura

    def getPreco(self):
        return self.__preco

    # ---------- SETTERS ----------

    def setNome(self, nome):
        self.__nome = nome

    def setValorCura(self, valorCura):
        self.__valorCura = valorCura

    def setPreco(self, preco):
        self.__preco = preco

    # ---------- OUTROS MÉTODOS ----------

    def mostrarDados(self):
        # Imprime na consola as informações desta poção.
        print("Nano kit:", self.__nome)
        print("Valor de cura:", self.__valorCura)
        print("Preço:", self.__preco, "créditos")
