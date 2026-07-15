import random

from Arma import Arma
from Armadura import Armadura
from Consumivel import Consumivel
from Pocao import Pocao


class Loja:
    def __init__(self):
        self.__itensDisponiveis = []
        self.__armaDisponivel = None
        self.__armaduraDisponivel = None
        self.__pocaoDisponivel = None
        self.__consumivelDisponivel = None

    def getArmaDisponivel(self):
        return self.__armaDisponivel

    def getArmaduraDisponivel(self):
        return self.__armaduraDisponivel

    def getPocaoDisponivel(self):
        return self.__pocaoDisponivel

    def getConsumivelDisponivel(self):
        return self.__consumivelDisponivel

    def getItensDisponiveis(self):
        return list(self.__itensDisponiveis)

    def setArmaDisponivel(self, arma):
        self.__armaDisponivel = arma

    def setArmaduraDisponivel(self, armadura):
        self.__armaduraDisponivel = armadura

    def setPocaoDisponivel(self, pocao):
        self.__pocaoDisponivel = pocao

    def setConsumivelDisponivel(self, consumivel):
        self.__consumivelDisponivel = consumivel

    def __atualizarItensPrincipais(self):
        self.__armaDisponivel = None
        self.__armaduraDisponivel = None
        self.__pocaoDisponivel = None
        self.__consumivelDisponivel = None

        for item in self.__itensDisponiveis:
            tipo = item["tipo"]
            objeto = item["objeto"]

            if tipo == "arma" and self.__armaDisponivel is None:
                self.__armaDisponivel = objeto
            elif tipo == "armadura" and self.__armaduraDisponivel is None:
                self.__armaduraDisponivel = objeto
            elif tipo == "pocao" and self.__pocaoDisponivel is None:
                self.__pocaoDisponivel = objeto
            elif tipo == "consumivel" and self.__consumivelDisponivel is None:
                self.__consumivelDisponivel = objeto

    def __criarArma(self, zona):
        tier = max(1, zona + random.randint(0, 1))
        bonusAtaque = 2 + (tier * 2) + random.randint(0, tier)
        preco = 8 + bonusAtaque * 5
        nomes = ["Lamina", "Pistola", "Rifle", "Katana", "Carabina", "Canhao"]
        nome = f"{random.choice(nomes)} Mk{tier}"
        return Arma(nome, bonusAtaque, preco)

    def __criarArmadura(self, zona):
        tier = max(1, zona + random.randint(0, 1))
        bonusDefesa = 1 + (tier * 2) + random.randint(0, tier)
        preco = 7 + bonusDefesa * 5
        nomes = ["Colete", "Blindagem", "Exoesqueleto", "Placas", "Manto"]
        nome = f"{random.choice(nomes)} Mk{tier}"
        return Armadura(nome, bonusDefesa, preco)

    def __criarPocao(self, zona):
        tier = max(1, zona + random.randint(0, 1))
        valorCura = 15 + (tier * 8) + random.randint(0, tier * 4)
        preco = 5 + valorCura // 2
        nomes = ["MaxDoc", "MaxDoc", "MaxDoc", "MaxDoc", "MaxDoc"]
        nome = f"{random.choice(nomes)} Mk{tier}"
        return Pocao(nome, valorCura, preco)

    def __criarConsumivel(self, zona):
        tier = max(1, zona + random.randint(0, 1))
        danoMinimo = 4 + (tier * 3)
        danoMaximo = danoMinimo + 4 + (tier * 2)
        preco = 10 + danoMaximo * 2
        nomes = ["Granada", "Carga", "Dardo", "Dispositivo", "Pulso"]
        nome = f"{random.choice(nomes)} Mk{tier}"
        return Consumivel(nome, danoMinimo, danoMaximo, preco)

    def gerarProdutos(self, numeroMasmorra):
        zona = max(1, numeroMasmorra)
        quantidade = random.randint(6, 10)
        tiposObrigatorios = ["arma", "armadura", "pocao", "consumivel"]

        self.__itensDisponiveis = []

        for tipo in tiposObrigatorios:
            self.__itensDisponiveis.append({
                "tipo": tipo,
                "objeto": self.__criarItem(tipo, zona),
            })

        while len(self.__itensDisponiveis) < quantidade:
            tipo = random.choice(tiposObrigatorios)
            self.__itensDisponiveis.append({
                "tipo": tipo,
                "objeto": self.__criarItem(tipo, zona),
            })

        random.shuffle(self.__itensDisponiveis)
        self.__atualizarItensPrincipais()

    def __criarItem(self, tipo, zona):
        if tipo == "arma":
            return self.__criarArma(zona)
        if tipo == "armadura":
            return self.__criarArmadura(zona)
        if tipo == "pocao":
            return self.__criarPocao(zona)
        return self.__criarConsumivel(zona)

    def __descricaoItem(self, item):
        tipo = item["tipo"]
        objeto = item["objeto"]

        if tipo == "arma":
            return f"[Arma] {objeto.getNome()} | Ataque +{objeto.getBonusAtaque()} | Preco {objeto.getPreco()}"
        if tipo == "armadura":
            return f"[Armadura] {objeto.getNome()} | Defesa +{objeto.getBonusDefesa()} | Preco {objeto.getPreco()}"
        if tipo == "pocao":
            return f"[MaxDoc] {objeto.getNome()} | Cura {objeto.getValorCura()} | Preco {objeto.getPreco()}"
        return f"[Consumivel] {objeto.getNome()} | Dano {objeto.getDanoMinimo()}-{objeto.getDanoMaximo()} | Preco {objeto.getPreco()}"

    def mostrarProdutos(self):
        print("\n===== MERCADO NEGRO =====")
        print("O vendedor olha para ti como quem ja viu pior.")

        if not self.__itensDisponiveis:
            print("Nao ha itens disponiveis neste momento.")
            return

        for indice, item in enumerate(self.__itensDisponiveis, start=1):
            print(f"{indice} - {self.__descricaoItem(item)}")

    def __comprarItem(self, jogador, indice):
        if indice < 1 or indice > len(self.__itensDisponiveis):
            print("Escolha invalida.")
            return False

        item = self.__itensDisponiveis[indice - 1]
        tipo = item["tipo"]
        objeto = item["objeto"]
        preco = objeto.getPreco()

        if tipo in ("pocao", "consumivel") and jogador.inventarioCheio():
            print("O teu inventario esta cheio. Liberta espaco antes de comprar mais itens.")
            return False

        if not jogador.gastarMoedas(preco):
            print("Nao tens creditos suficientes para esta compra.")
            return False

        sucesso = False
        if tipo == "arma":
            jogador.equiparArma(objeto)
            print(f"Compraste e equipaste {objeto.getNome()}!")
            sucesso = True
        elif tipo == "armadura":
            jogador.equiparArmadura(objeto)
            print(f"Compraste e equipaste {objeto.getNome()}!")
            sucesso = True
        elif tipo == "pocao":
            sucesso = jogador.guardarPocao(objeto)
            if sucesso:
                print(f"Compraste {objeto.getNome()}!")
        else:
            sucesso = jogador.adicionarConsumivel(objeto)
            if sucesso:
                print(f"Compraste {objeto.getNome()}!")

        if not sucesso:
            jogador.ganharMoedas(preco)
            print("Nao foi possivel concluir a compra.")
            return False

        self.__itensDisponiveis.pop(indice - 1)
        self.__atualizarItensPrincipais()
        return True

    def comprarItem(self, jogador, indice):
        return self.__comprarItem(jogador, indice)

    def __comprarPrimeiroDoTipo(self, jogador, tipo):
        for indice, item in enumerate(self.__itensDisponiveis, start=1):
            if item["tipo"] == tipo:
                return self.__comprarItem(jogador, indice)

        print("Nao ha nenhum item desse tipo disponivel.")
        return False

    def comprarArma(self, jogador):
        return self.__comprarPrimeiroDoTipo(jogador, "arma")

    def comprarArmadura(self, jogador):
        return self.__comprarPrimeiroDoTipo(jogador, "armadura")

    def comprarPocao(self, jogador):
        return self.__comprarPrimeiroDoTipo(jogador, "pocao")

    def comprarConsumivel(self, jogador):
        return self.__comprarPrimeiroDoTipo(jogador, "consumivel")
