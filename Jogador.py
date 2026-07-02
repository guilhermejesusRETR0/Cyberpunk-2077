
class Jogador:
    def __init__(self, nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas):
        self.__nome = nome
        self.__vidaMaxima = vidaMaxima
        self.__vida = vidaMaxima
        self.__ataque = ataque
        self.__defesa = defesa
        self.__nivel = nivel
        self.__experiencia = experiencia
        self.__moedas = moedas
        self.__arma = None
        self.__armadura = None
        self.__pocao = None

    def getNome(self):
        return self.__nome

    def getVida(self):
        return self.__vida

    def getVidaMaxima(self):
        return self.__vidaMaxima

    def getAtaque(self):
        return self.__ataque

    def getDefesa(self):
        return self.__defesa

    def getNivel(self):
        return self.__nivel

    def getExperiencia(self):
        return self.__experiencia

    def getMoedas(self):
        return self.__moedas

    def getArma(self):
        return self.__arma

    def getArmadura(self):
        return self.__armadura

    def getPocao(self):
        return self.__pocao

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        self.__vida = max(0, min(vida, self.__vidaMaxima))

    def setVidaMaxima(self, vidaMaxima):
        self.__vidaMaxima = vidaMaxima

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa

    def setNivel(self, nivel):
        self.__nivel = nivel

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def setMoedas(self, moedas):
        self.__moedas = moedas

    def setArma(self, arma):
        self.__arma = arma

    def setArmadura(self, armadura):
        self.__armadura = armadura

    def setPocao(self, pocao):
        self.__pocao = pocao

    def getAtaqueTotal(self):
        ataqueTotal = self.__ataque
        if self.__arma is not None:
            ataqueTotal += self.__arma.getBonusAtaque()
        return ataqueTotal

    def getDefesaTotal(self):
        defesaTotal = self.__defesa
        if self.__armadura is not None:
            defesaTotal += self.__armadura.getBonusDefesa()
        return defesaTotal

    def receberDano(self, dano):
        danoReal = dano - self.getDefesaTotal()
        if danoReal < 1:
            danoReal = 1

        self.__vida -= danoReal
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, inimigo):
        dano = self.getAtaqueTotal()
        inimigo.receberDano(dano)
        print(f"{self.__nome} lançou um ataque em {inimigo.getNome()} e causou {dano} de dano. A cidade engole o som e devolve-o como mais um problema.")

    def curar(self, valor):
        self.__vida += valor
        if self.__vida > self.__vidaMaxima:
            self.__vida = self.__vidaMaxima
        print(f"{self.__nome} recuperou {valor} de integridade. O corpo ainda não desiste, o que já é um milagre com o estado em que está.")

    def ganharExperiencia(self, valor):
        self.__experiencia += valor
        while self.__experiencia >= 100:
            self.__experiencia -= 100
            self.subirNivel()

    def subirNivel(self):
        self.__nivel += 1
        self.__vidaMaxima += 20
        self.__ataque += 5
        self.__defesa += 2
        self.__vida = self.__vidaMaxima
        print(f"{self.__nome} subiu para o nível {self.__nivel}. O sistema reconheceu a tua sobrevivência. Isso, por si só, já é um insulto.")
        return True

    def ganharMoedas(self, valor):
        self.__moedas += valor

    def gastarMoedas(self, valor):
        if self.__moedas >= valor:
            self.__moedas -= valor
            return True
        return False

    def equiparArma(self, arma):
        self.__arma = arma

    def equiparArmadura(self, armadura):
        self.__armadura = armadura

    def guardarPocao(self, pocao):
        self.__pocao = pocao

    def usarPocao(self):
        if self.__pocao is not None:
            self.curar(self.__pocao.getValorCura())
            self.__pocao = None
            return True
        return False

    def estaVivo(self):
        return self.__vida > 0

    def mostrarEstado(self):
        print("\n===== ESTADO DO JOGADOR =====")
        print("Nome:", self.__nome)
        print("Integridade:", self.__vida, "/", self.__vidaMaxima)
        print("Nível:", self.__nivel)
        print("Experiência:", self.__experiencia)
        print("Créditos:", self.__moedas)
        print("Ataque base:", self.__ataque)
        print("Defesa base:", self.__defesa)
        print("Ataque total:", self.getAtaqueTotal())
        print("Defesa total:", self.getDefesaTotal())

        if self.__arma is None:
            print("Arma equipada: nenhuma. O mínimo possível para o mínimo possível.")
        else:
            print("Arma equipada:", self.__arma.getNome())

        if self.__armadura is None:
            print("Blindagem equipada: nenhuma. O corpo continua a ser o maior risco da operação.")
        else:
            print("Blindagem equipada:", self.__armadura.getNome())

        if self.__pocao is None:
            print("Nano kit guardado: nenhum. A sobrevivência continua a ser um hábito ruim.")
        else:
            print("Nano kit guardado:", self.__pocao.getNome())

