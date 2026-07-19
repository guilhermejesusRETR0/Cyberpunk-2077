# ============================================================
# CLASSE INIMIGO
# Representa um inimigo que o jogador enfrenta ao explorar uma zona.
# Cada zona do jogo tem o seu próprio inimigo, com estatísticas
# diferentes (ver Jogo.criarInimigoAtual).
# ============================================================

class Inimigo:

    def __init__(self, nome, vida, ataque, defesa, experiencia, moedas):
        # Construtor: cria um novo inimigo.
        # Exemplo de uso: Inimigo("Ganger de neon", 30, 7, 2, 20, 15)
        self.__nome = nome
        self.__vida = vida                    # Vida atual do inimigo
        self.__ataque = ataque                # Quanto dano este inimigo causa ao atacar
        self.__defesa = defesa                # Quanto este inimigo reduz o dano que recebe
        self.__experiencia = experiencia      # Experiência que o jogador ganha ao derrotá-lo
        self.__moedas = moedas                # Créditos que o jogador ganha ao derrotá-lo

    # ---------- GETTERS ----------

    def getNome(self):
        return self.__nome

    def getVida(self):
        return self.__vida

    def getAtaque(self):
        return self.__ataque

    def getDefesa(self):
        return self.__defesa

    def getExperiencia(self):
        return self.__experiencia

    def getMoedas(self):
        return self.__moedas

    def getRecompensaExperiencia(self):
        # Nome alternativo para getExperiencia(), usado quando se fala
        # especificamente da "recompensa" dada ao jogador após a vitória.
        return self.__experiencia

    def getRecompensaMoedas(self):
        # Nome alternativo para getMoedas(), usado quando se fala
        # especificamente da "recompensa" dada ao jogador após a vitória.
        return self.__moedas

    # ---------- SETTERS ----------

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        # Nunca deixamos a vida ficar negativa.
        self.__vida = max(0, vida)

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def setMoedas(self, moedas):
        self.__moedas = moedas

    # ---------- OUTROS MÉTODOS ----------

    def receberDano(self, dano):
        # Chamado quando o jogador ataca este inimigo.
        # "dano" é o valor de ataque BRUTO do jogador (sem descontar
        # a defesa do inimigo) - essa subtração é feita aqui dentro.
        danoReal = dano - self.__defesa

        # Regra do jogo: o dano mínimo é sempre 1, mesmo que a defesa
        # seja muito alta (para que o combate nunca fique "impossível").
        if danoReal < 1:
            danoReal = 1

        self.__vida -= danoReal

        # Garantimos que a vida nunca fica negativa.
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, jogador):
        # Chamado quando é a vez do inimigo atacar o jogador.
        # Passamos o ataque BRUTO deste inimigo; é o método
        # Jogador.receberDano() que faz o desconto da defesa do jogador.
        # (Isto evita descontar a defesa duas vezes.)
        jogador.receberDano(self.__ataque)
        print(f"{self.__nome} atacou {jogador.getNome()} com {self.__ataque} de dano.")

    def estaVivo(self):
        # Devolve True enquanto o inimigo tiver vida > 0.
        return self.__vida > 0

    def mostrarEstado(self):
        # Imprime na consola o estado atual deste inimigo (usado em combate).
        print("\n===== ESTADO DO INIMIGO =====")
        print("Nome:", self.__nome)
        print("Integridade:", self.__vida)
        print("Ataque:", self.__ataque)
        print("Defesa:", self.__defesa)
        print("Recompensa de experiencia:", self.__experiencia)
        print("Recompensa de moedas:", self.__moedas)
