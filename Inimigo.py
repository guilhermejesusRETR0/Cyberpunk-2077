
class Inimigo:
    def __init__(self, nome, vida, ataque, defesa, experiencia, moedas):
        self.__nome = nome
        self.__vida = vida
        self.__ataque = ataque
        self.__defesa = defesa
        self.__experiencia = experiencia
        self.__moedas = moedas

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
        return self.__experiencia

    def getRecompensaMoedas(self):
        return self.__moedas

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        self.__vida = max(0, vida)

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def setMoedas(self, moedas):
        self.__moedas = moedas

    def receberDano(self, dano):
        danoReal = dano - self.__defesa
        if danoReal < 1:
            danoReal = 1

        self.__vida -= danoReal
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, jogador):
        dano = max(1, self.__ataque - jogador.getDefesaTotal())
        jogador.receberDano(dano)
        print(f"{self.__nome} atingiu {jogador.getNome()} e causou {dano} de dano.")

    def estaVivo(self):
        return self.__vida > 0

    def mostrarEstado(self):
        print("\n===== ESTADO DO INIMIGO =====")
        print("Nome:", self.__nome)
        print("Integridade:", self.__vida)
        print("Ataque:", self.__ataque)
        print("Defesa:", self.__defesa)
        print("Recompensa de experiencia:", self.__experiencia)
        print("Recompensa de moedas:", self.__moedas)
