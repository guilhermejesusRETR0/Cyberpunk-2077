# ============================================================
# CLASSE ARMADURA
# Representa uma blindagem que o jogador pode comprar e equipar.
# Uma armadura dá um bónus fixo de defesa enquanto estiver equipada.
# Funciona em espelho com a classe Arma (mesma lógica, mas para defesa).
# ============================================================

class Armadura:

    def __init__(self, nome, bonusDefesa, preco):
        # Construtor: cria uma nova armadura.
        # Exemplo de uso: Armadura("Colete Mk3", 8, 47)
        self.__nome = nome                # Nome da armadura (texto)
        self.__bonusDefesa = bonusDefesa  # Quanta defesa extra esta armadura dá
        self.__preco = preco              # Quanto custa em créditos

    # ---------- GETTERS ----------

    def getNome(self):
        return self.__nome

    def getBonusDefesa(self):
        return self.__bonusDefesa

    def getPreco(self):
        return self.__preco

    # ---------- SETTERS ----------

    def setNome(self, nome):
        self.__nome = nome

    def setBonusDefesa(self, bonusDefesa):
        self.__bonusDefesa = bonusDefesa

    def setPreco(self, preco):
        self.__preco = preco

    # ---------- OUTROS MÉTODOS ----------

    def mostrarDados(self):
        # Imprime na consola as informações desta armadura.
        print("Blindagem:", self.__nome)
        print("Bónus de defesa:", self.__bonusDefesa)
        print("Preço:", self.__preco, "créditos")
