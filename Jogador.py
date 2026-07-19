# ============================================================
# CLASSE JOGADOR
# Representa a personagem principal controlada por quem está a jogar.
# É a classe mais "central" do jogo: guarda a vida, o nível, o dinheiro,
# o equipamento e o inventário, e tem os métodos de combate/cura/loja.
# ============================================================

class Jogador:

    def __init__(self, nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas):
        self.__nome = nome
        self.__vidaMaxima = vidaMaxima
        self.__vida = vidaMaxima              # Começa sempre com a vida no máximo
        self.__ataque = ataque                # Ataque BASE (sem contar arma/companheiros)
        self.__defesa = defesa                # Defesa BASE (sem contar armadura)
        self.__nivel = nivel
        self.__experiencia = experiencia
        self.__moedas = moedas
        self.__arma = None                    # Nenhuma arma equipada no início
        self.__armadura = None                # Nenhuma armadura equipada no início
        self.__inventarioPocoes = []          # Lista de poções (MaxDocs) guardadas
        self.__inventarioConsumiveisCombate = []  # Lista de consumíveis de combate guardados
        self.__limiteInventario = 10          # Poções + consumíveis não podem passar disto
        self.__companheiros = []              # Lista de companheiros já recrutados

    # ---------- GETTERS ----------

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
        # Devolve a primeira poção do inventário (ou None se não houver nenhuma).
        if self.__inventarioPocoes:
            return self.__inventarioPocoes[0]
        return None

    def getInventarioPocoes(self):
        # Devolve uma CÓPIA da lista de poções (para não deixar código
        # de fora alterar o inventário real por engano).
        return list(self.__inventarioPocoes)

    def getInventarioConsumiveisCombate(self):
        return list(self.__inventarioConsumiveisCombate)

    def getLimiteInventario(self):
        return self.__limiteInventario

    def consultarTotalItensInventario(self):
        # Conta quantos itens (poções + consumíveis) estão no inventário.
        # Armas e armaduras NÃO contam para este limite.
        return len(self.__inventarioPocoes) + len(self.__inventarioConsumiveisCombate)

    def inventarioCheio(self):
        # True se já não há espaço para mais poções/consumíveis.
        return self.consultarTotalItensInventario() >= self.__limiteInventario

    # ---------- SETTERS ----------

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        # "max(0, min(vida, self.__vidaMaxima))" garante duas coisas ao mesmo
        # tempo: a vida nunca fica negativa, e nunca ultrapassa a vida máxima.
        self.__vida = max(0, min(vida, self.__vidaMaxima))

    def setVidaMaxima(self, vidaMaxima):
        self.__vidaMaxima = vidaMaxima
        # Se a vida atual for maior que a nova vida máxima, ajustamos.
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
        # Substitui TODO o inventário de poções por, no máximo, uma poção.
        # (Normalmente usa-se adicionarPocao() em vez deste método.)
        self.__inventarioPocoes = []
        if pocao is not None:
            self.__inventarioPocoes.append(pocao)

    def setConsumiveisCombate(self, consumiveis):
        self.__inventarioConsumiveisCombate = list(consumiveis) if consumiveis is not None else []

    # ---------- INVENTÁRIO ----------

    def podeAdicionarItem(self):
        return not self.inventarioCheio()

    def adicionarPocao(self, pocao):
        # Tenta guardar uma poção no inventário.
        # Devolve False se o inventário estiver cheio ou se pocao for None.
        if pocao is None or self.inventarioCheio():
            return False

        self.__inventarioPocoes.append(pocao)
        return True

    def adicionarConsumivelCombate(self, consumivel):
        # Igual ao adicionarPocao(), mas para consumíveis de combate.
        if consumivel is None or self.inventarioCheio():
            return False

        self.__inventarioConsumiveisCombate.append(consumivel)
        return True

    def removerConsumivelCombate(self, indice=0):
        # Remove e devolve o consumível na posição "indice" (por defeito,
        # o primeiro da lista). Devolve None se o índice não existir.
        if indice < 0 or indice >= len(self.__inventarioConsumiveisCombate):
            return None

        return self.__inventarioConsumiveisCombate.pop(indice)

    # ---------- COMPANHEIROS ----------

    def temCompanheiro(self, nomeCompanheiro):
        # Verifica se já existe, na equipa, um companheiro com este nome.
        return any(c.getNome() == nomeCompanheiro for c in self.__companheiros)

    def recrutarCompanheiro(self, companheiro):
        # Adiciona o companheiro à equipa e aplica de imediato o bónus
        # de vida máxima dele (se tiver), curando o jogador na mesma quantidade.
        self.__companheiros.append(companheiro)
        bonusVida = companheiro.getBonusVidaMaxima()
        if bonusVida:
            self.__vidaMaxima += bonusVida
            self.__vida += bonusVida
            if self.__vida > self.__vidaMaxima:
                self.__vida = self.__vidaMaxima

    def getTotalBonusAtaqueCompanheiros(self):
        # Soma o bónus de ataque de TODOS os companheiros recrutados.
        return sum(c.getBonusAtaque() for c in self.__companheiros)

    def getTotalBonusCuraCompanheiros(self):
        # Soma o bónus de cura de todos os companheiros (usado ao curar).
        return sum(c.getBonusCura() for c in self.__companheiros)

    def getTotalBonusExperienciaCompanheiros(self):
        # Soma o bónus de % de experiência de todos os companheiros.
        return sum(c.getBonusExperiencia() for c in self.__companheiros)

    # ---------- COMBATE ----------

    def getAtaqueTotal(self):
        # Ataque total = ataque base + bónus da arma equipada (se houver)
        # + bónus de ataque dado pelos companheiros recrutados.
        ataqueTotal = self.__ataque
        if self.__arma is not None:
            ataqueTotal += self.__arma.getBonusAtaque()
        ataqueTotal += self.getTotalBonusAtaqueCompanheiros()
        return ataqueTotal

    def getDefesaTotal(self):
        # Defesa total = defesa base + bónus da armadura equipada (se houver).
        defesaTotal = self.__defesa
        if self.__armadura is not None:
            defesaTotal += self.__armadura.getBonusDefesa()
        return defesaTotal

    def receberDano(self, dano):
        # Chamado quando o jogador recebe um ataque.
        # "dano" é o valor de ataque BRUTO de quem atacou; é aqui que
        # descontamos a defesa total do jogador.
        danoReal = dano - self.getDefesaTotal()

        # O dano mínimo é sempre 1, mesmo com defesa muito alta.
        if danoReal < 1:
            danoReal = 1

        self.__vida -= danoReal
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, inimigo):
        # Chamado quando o jogador ataca um inimigo.
        # Passamos o ataque total (já com bónus de arma/companheiros);
        # é o Inimigo.receberDano() que desconta a defesa do inimigo.
        dano = self.getAtaqueTotal()
        inimigo.receberDano(dano)
        print(f"{self.__nome} lancou um ataque em {inimigo.getNome()} e causou {dano} de dano.")

    # ---------- CURA / EXPERIÊNCIA / NÍVEL / MOEDAS ----------

    def recuperarVida(self, valor):
        # Recupera vida ao jogador, tendo em conta o bónus de cura dos
        # companheiros. A vida nunca ultrapassa a vida máxima.
        valor += self.getTotalBonusCuraCompanheiros()
        self.__vida += valor
        if self.__vida > self.__vidaMaxima:
            self.__vida = self.__vidaMaxima
        print(f"{self.__nome} recuperou {valor} de integridade.")

    def ganharExperiencia(self, valor):
        # Soma experiência e sobe de nível automaticamente cada vez
        # que a experiência atinge 100 (pode subir vários níveis de seguida
        # se ganhar muita experiência de uma vez, por isso o "while").
        self.__experiencia += valor
        while self.__experiencia >= 100:
            self.__experiencia -= 100
            self.subirNivel()

    def subirNivel(self):
        # Aumenta o nível e melhora os atributos base do jogador.
        # A vida é totalmente restaurada ao subir de nível.
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
        # Só gasta as moedas se o jogador tiver o suficiente.
        # Devolve True se conseguiu pagar, False caso contrário.
        if self.__moedas >= valor:
            self.__moedas -= valor
            return True
        return False

    # ---------- EQUIPAMENTO E ITENS ----------

    def equiparArma(self, arma):
        self.__arma = arma

    def equiparArmadura(self, armadura):
        self.__armadura = armadura

    def guardarPocao(self, pocao):
        # Nome usado pela Loja para guardar uma poção comprada.
        # É apenas um "atalho" para adicionarPocao().
        return self.adicionarPocao(pocao)

    def usarPocao(self):
        # Usa a primeira poção do inventário: cura o jogador e remove-a.
        # Devolve True se usou uma poção, False se não havia nenhuma.
        if self.__inventarioPocoes:
            pocao = self.__inventarioPocoes.pop(0)
            self.recuperarVida(pocao.getValorCura())
            print(f"{self.__nome} usou {pocao.getNome()} e recuperou {pocao.getValorCura()} de integridade.")
            return True
        return False

    def usarConsumivelCombate(self, inimigo):
        # Usa o primeiro consumível de combate do inventário: causa dano
        # aleatório ao inimigo (gerarDano()) e remove o item do inventário.
        # Devolve True se usou um consumível, False se não havia nenhum.
        if not self.__inventarioConsumiveisCombate or inimigo is None:
            return False

        consumivel = self.__inventarioConsumiveisCombate.pop(0)
        dano = consumivel.gerarDano()
        inimigo.receberDano(dano)
        print(f"{self.__nome} usou {consumivel.getNome()} e causou {dano} de dano em {inimigo.getNome()}.")
        return True

    def estaVivo(self):
        return self.__vida > 0

    # ---------- MOSTRAR INFORMAÇÃO ----------

    def mostrarPocoes(self):
        # Lista todas as poções (MaxDocs) que o jogador tem guardadas.
        print("MaxDocs no inventario:")
        if not self.__inventarioPocoes:
            print("Nenhuma.")
        else:
            for pocao in self.__inventarioPocoes:
                print(" -", pocao.getNome(), "(cura", pocao.getValorCura(), ")")

    def mostrarConsumiveisCombate(self):
        # Lista todos os consumíveis de combate que o jogador tem guardados.
        print("Consumiveis de combate no inventario:")
        if not self.__inventarioConsumiveisCombate:
            print("Nenhum.")
        else:
            for consumivel in self.__inventarioConsumiveisCombate:
                print(
                    " -",
                    consumivel.getNome(),
                    "(dano",
                    consumivel.getDanoMinimo(),
                    "-",
                    consumivel.getDanoMaximo(),
                    ")"
                )

    def mostrarEstado(self):
        # Imprime um resumo completo do estado do jogador: vida, nível,
        # equipamento, inventário e companheiros. Usado no menu "Ver estado".
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
        print("Inventario:", self.consultarTotalItensInventario(), "/", self.__limiteInventario)

        if self.__arma is None:
            print("Arma equipada: nenhuma.")
        else:
            print("Arma equipada:", self.__arma.getNome())

        if self.__armadura is None:
            print("Armadura equipada: nenhuma.")
        else:
            print("Armadura equipada:", self.__armadura.getNome())

        self.mostrarPocoes()
        self.mostrarConsumiveisCombate()

        print("Companheiros recrutados:")
        if not self.__companheiros:
            print("Nenhum.")
        else:
            for companheiro in self.__companheiros:
                print(" -", companheiro.getNome(), "(", companheiro.getPapel(), ")")
