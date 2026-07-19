# ============================================================
# CLASSE CONSUMIVELCOMBATE
# Representa um item ofensivo descartável (ex: granadas, dispositivos).
# Ao contrário da Arma (que fica equipada), o ConsumivelCombate é usado
# uma única vez em combate, causa dano ao inimigo e depois desaparece
# do inventário.
# ============================================================

import random


class ConsumivelCombate:

    def __init__(self, nome, danoMinimo, danoMaximo, preco):
        # Construtor: cria um novo consumível de combate.
        # Exemplo de uso: ConsumivelCombate("Granada Mk2", 10, 18, 46)
        self.__nome = nome
        # Nota de segurança: garantimos que o dano minimo nunca é negativo,
        # e que o dano maximo nunca é menor do que o dano minimo.
        self.__danoMinimo = danoMinimo if danoMinimo >= 0 else 0
        self.__danoMaximo = danoMaximo if danoMaximo >= self.__danoMinimo else self.__danoMinimo
        self.__preco = preco

    # ---------- GETTERS ----------

    def getNome(self):
        return self.__nome

    def getDanoMinimo(self):
        return self.__danoMinimo

    def getDanoMaximo(self):
        return self.__danoMaximo

    def getPreco(self):
        return self.__preco

    # ---------- SETTERS ----------

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

    # ---------- OUTROS MÉTODOS ----------

    def gerarDano(self):
        # Sorteia um valor de dano entre o minimo e o maximo deste item.
        # É este método que é chamado quando o jogador usa o consumível
        # em combate (ver Jogador.usarConsumivelCombate).
        return random.randint(self.__danoMinimo, self.__danoMaximo)

    def mostrarDados(self):
        print("Consumivel:", self.__nome)
        print("Dano minimo:", self.__danoMinimo)
        print("Dano maximo:", self.__danoMaximo)
        print("Preco:", self.__preco, "creditos")
