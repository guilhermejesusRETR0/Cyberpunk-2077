import random


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
        self.__pocoes = []
        self.__consumiveis = []
        self.__limiteInventario = 10
        self.__companheiros = []

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
        if self.__pocoes:
            return self.__pocoes[0]
        return None

    def getPocoes(self):
        return list(self.__pocoes)

    def getConsumiveis(self):
        return list(self.__consumiveis)

    def getLimiteInventario(self):
        return self.__limiteInventario

    def getQuantidadeItensInventario(self):
        return len(self.__pocoes) + len(self.__consumiveis)

    def inventarioCheio(self):
        return self.getQuantidadeItensInventario() >= self.__limiteInventario

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        self.__vida = max(0, min(vida, self.__vidaMaxima))

    def setVidaMaxima(self, vidaMaxima):
        self.__vidaMaxima = vidaMaxima
        if self.__vida > self.__vidaMaxima:
            self.__vida = self.__vidaMaxima

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
        self.__pocoes = []
        if pocao is not None:
            self.__pocoes.append(pocao)

    def setConsumiveis(self, consumiveis):
        self.__consumiveis = list(consumiveis) if consumiveis is not None else []

    def podeAdicionarItem(self):
        return not self.inventarioCheio()

    def adicionarPocao(self, pocao):
        if pocao is None or self.inventarioCheio():
            return False

        self.__pocoes.append(pocao)
        return True

    def adicionarConsumivel(self, consumivel):
        if consumivel is None or self.inventarioCheio():
            return False

        self.__consumiveis.append(consumivel)
        return True

    def removerConsumivel(self, indice=0):
        if indice < 0 or indice >= len(self.__consumiveis):
            return None

        return self.__consumiveis.pop(indice)

    def temCompanheiro(self, nomeCompanheiro):
        return any(c.getNome() == nomeCompanheiro for c in self.__companheiros)

    def recrutarCompanheiro(self, companheiro):
        self.__companheiros.append(companheiro)
        bonusVida = companheiro.getBonusVidaMaxima()
        if bonusVida:
            self.__vidaMaxima += bonusVida
            self.__vida += bonusVida
            if self.__vida > self.__vidaMaxima:
                self.__vida = self.__vidaMaxima

    def getTotalBonusAtaqueCompanheiros(self):
        return sum(c.getBonusAtaque() + c.getBonusCritico() for c in self.__companheiros)

    def getTotalBonusCuraCompanheiros(self):
        return sum(c.getBonusCura() for c in self.__companheiros)

    def getTotalBonusExperienciaCompanheiros(self):
        return sum(c.getBonusExperiencia() for c in self.__companheiros)

    def getAtaqueTotal(self):
        ataqueTotal = self.__ataque
        if self.__arma is not None:
            ataqueTotal += self.__arma.getBonusAtaque()
        ataqueTotal += self.getTotalBonusAtaqueCompanheiros()
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
        print(f"{self.__nome} lancou um ataque em {inimigo.getNome()} e causou {dano} de dano.")

    def curar(self, valor):
        valor += self.getTotalBonusCuraCompanheiros()
        self.__vida += valor
        if self.__vida > self.__vidaMaxima:
            self.__vida = self.__vidaMaxima
        print(f"{self.__nome} recuperou {valor} de integridade.")

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
        print(f"{self.__nome} subiu para o nivel {self.__nivel}.")
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
        return self.adicionarPocao(pocao)

    def usarPocao(self):
        if self.__pocoes:
            pocao = self.__pocoes.pop(0)
            self.curar(pocao.getValorCura())
            print(f"{self.__nome} usou {pocao.getNome()} e recuperou {pocao.getValorCura()} de integridade.")
            return True
        return False

    def usarConsumivel(self, inimigo):
        if not self.__consumiveis or inimigo is None:
            return False

        consumivel = self.__consumiveis.pop(0)
        dano = random.randint(consumivel.getDanoMinimo(), consumivel.getDanoMaximo())
        inimigo.receberDano(dano)
        print(f"{self.__nome} usou {consumivel.getNome()} e causou {dano} de dano em {inimigo.getNome()}.")
        return True

    def estaVivo(self):
        return self.__vida > 0

    def mostrarEstado(self):
        print("\n===== ESTADO DO JOGADOR =====")
        print("Nome:", self.__nome)
        print("Integridade:", self.__vida, "/", self.__vidaMaxima)
        print("Nivel:", self.__nivel)
        print("Experiencia:", self.__experiencia)
        print("Creditos:", self.__moedas)
        print("Ataque base:", self.__ataque)
        print("Defesa base:", self.__defesa)
        print("Ataque total:", self.getAtaqueTotal())
        print("Defesa total:", self.getDefesaTotal())
        print("Inventario MaxDocs/Consumiveis:", self.getQuantidadeItensInventario(), "/", self.__limiteInventario)

        if self.__arma is None:
            print("Arma equipada: nenhuma.")
        else:
            print("Arma equipada:", self.__arma.getNome())

        if self.__armadura is None:
            print("Armadura equipada: nenhuma.")
        else:
            print("Armadura equipada:", self.__armadura.getNome())

        print("MaxDocs no inventario:")
        if not self.__pocoes:
            print("Nenhuma.")
        else:
            for maxdoc in self.__pocoes:
                print(" -", maxdoc.getNome(), "(cura", maxdoc.getValorCura(), ")")

        print("Consumiveis no inventario:")
        if not self.__consumiveis:
            print("Nenhum.")
        else:
            for consumivel in self.__consumiveis:
                print(
                    " -",
                    consumivel.getNome(),
                    "(dano",
                    consumivel.getDanoMinimo(),
                    "-",
                    consumivel.getDanoMaximo(),
                    ")"
                )

        print("Companheiros recrutados:")
        if not self.__companheiros:
            print("Nenhum.")
        else:
            for companheiro in self.__companheiros:
                print(" -", companheiro.getNome(), "(", companheiro.getPapel(), ")")
