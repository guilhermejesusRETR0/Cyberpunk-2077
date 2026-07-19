# ============================================================
# CLASSE LOJA
# Representa o "mercado negro" que o jogador visita em cada zona.
# A loja tem um catálogo completo de itens (armasDisponiveis,
# armadurasDisponiveis, etc.) mas só MOSTRA 10 itens ao jogador de
# cada vez, escolhidos ao acaso (itensVisiveis).
#
# COMO FUNCIONA POR DENTRO:
# 1. gerarProdutos() cria o catálogo completo (vários itens de cada tipo).
# 2. gerarItensVisiveis() escolhe 10 desses itens ao acaso para mostrar,
#    e organiza-os por tipo (armas, depois armaduras, depois poções,
#    depois consumíveis) só para ficar mais fácil de ler.
# 3. venderItem() processa a compra de um dos itens visíveis.
# ============================================================

import random

from Arma import Arma
from Armadura import Armadura
from ConsumivelCombate import ConsumivelCombate
from Pocao import Pocao


class Loja:

    # Lista de possíveis nomes de vendedor - um é escolhido ao acaso
    # sempre que a loja gera produtos novos (gerarProdutos).
    __NOMES_VENDEDOR = [
        "Viktor, o negociante da Combat Zone",
        "Rogue Amendiares",
        "Wakako Okada",
        "Dino Dinovic",
    ]

    def __init__(self):
        self.__nomeVendedor = random.choice(self.__NOMES_VENDEDOR)
        self.__armasDisponiveis = []       # Catálogo completo de armas desta visita
        self.__armadurasDisponiveis = []   # Catálogo completo de armaduras desta visita
        self.__pocoesDisponiveis = []      # Catálogo completo de poções desta visita
        self.__consumiveisDisponiveis = []  # Catálogo completo de consumíveis desta visita
        self.__itensVisiveis = []          # Os 10 itens escolhidos para mostrar ao jogador

    # ---------- GETTERS ----------

    def getNomeVendedor(self):
        return self.__nomeVendedor

    def getArmasDisponiveis(self):
        return list(self.__armasDisponiveis)

    def getArmadurasDisponiveis(self):
        return list(self.__armadurasDisponiveis)

    def getPocoesDisponiveis(self):
        return list(self.__pocoesDisponiveis)

    def getConsumiveisDisponiveis(self):
        return list(self.__consumiveisDisponiveis)

    def getItensVisiveis(self):
        # Devolve os itens atualmente mostrados na loja (no máximo 10).
        return list(self.__itensVisiveis)

    # ---------- SETTERS ----------

    def setNomeVendedor(self, nomeVendedor):
        self.__nomeVendedor = nomeVendedor

    def setArmasDisponiveis(self, armas):
        self.__armasDisponiveis = list(armas) if armas is not None else []

    def setArmadurasDisponiveis(self, armaduras):
        self.__armadurasDisponiveis = list(armaduras) if armaduras is not None else []

    def setPocoesDisponiveis(self, pocoes):
        self.__pocoesDisponiveis = list(pocoes) if pocoes is not None else []

    def setConsumiveisDisponiveis(self, consumiveis):
        self.__consumiveisDisponiveis = list(consumiveis) if consumiveis is not None else []

    # ---------- CRIAÇÃO DE ITENS (uso interno) ----------
    # Estes métodos privados (começam com "__") criam um item aleatório,
    # ficando mais fortes e mais caros conforme a zona ("tier") aumenta.
    # Se quiseres alterar preços/força dos itens da loja, é AQUI que
    # deves alterar os números.

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
        nome = f"MaxDoc Mk{tier}"
        return Pocao(nome, valorCura, preco)

    def __criarConsumivel(self, zona):
        tier = max(1, zona + random.randint(0, 1))
        danoMinimo = 4 + (tier * 3)
        danoMaximo = danoMinimo + 4 + (tier * 2)
        preco = 10 + danoMaximo * 2
        nomes = ["Granada", "Carga", "Dardo", "Dispositivo", "Pulso"]
        nome = f"{random.choice(nomes)} Mk{tier}"
        return ConsumivelCombate(nome, danoMinimo, danoMaximo, preco)

    # ---------- GERAÇÃO DE PRODUTOS ----------

    def gerarProdutos(self, numeroMasmorra):
        # Gera o catálogo completo da loja para a zona atual.
        # Cada tipo de item tem entre 4 e 6 exemplares (número aleatório).
        # No final, chama gerarItensVisiveis() para escolher quais os 10
        # itens que vão realmente aparecer ao jogador.
        zona = max(1, numeroMasmorra)
        self.__nomeVendedor = random.choice(self.__NOMES_VENDEDOR)

        self.__armasDisponiveis = [self.__criarArma(zona) for _ in range(random.randint(4, 6))]
        self.__armadurasDisponiveis = [self.__criarArmadura(zona) for _ in range(random.randint(4, 6))]
        self.__pocoesDisponiveis = [self.__criarPocao(zona) for _ in range(random.randint(4, 6))]
        self.__consumiveisDisponiveis = [self.__criarConsumivel(zona) for _ in range(random.randint(4, 6))]

        self.gerarItensVisiveis()

    def gerarItensVisiveis(self):
        # Junta todo o catálogo (armas + armaduras + poções + consumíveis)
        # numa única lista, embaralha, e escolhe os primeiros 10.
        # Depois ordena esses 10 por tipo, só para a exibição ficar
        # organizada (armas, armaduras, poções, consumíveis).
        todosItens = []
        todosItens += [{"tipo": "arma", "objeto": arma} for arma in self.__armasDisponiveis]
        todosItens += [{"tipo": "armadura", "objeto": armadura} for armadura in self.__armadurasDisponiveis]
        todosItens += [{"tipo": "pocao", "objeto": pocao} for pocao in self.__pocoesDisponiveis]
        todosItens += [{"tipo": "consumivel", "objeto": consumivel} for consumivel in self.__consumiveisDisponiveis]

        random.shuffle(todosItens)
        itensEscolhidos = todosItens[:10]

        # "ordemTipos" define a ordem de exibição: quanto menor o número,
        # mais acima o item aparece na lista mostrada ao jogador.
        ordemTipos = {"arma": 0, "armadura": 1, "pocao": 2, "consumivel": 3}
        itensEscolhidos.sort(key=lambda item: ordemTipos[item["tipo"]])

        self.__itensVisiveis = itensEscolhidos
        return list(self.__itensVisiveis)

    def __descricaoItem(self, item):
        # Constrói a linha de texto usada para mostrar um item na loja.
        tipo = item["tipo"]
        objeto = item["objeto"]

        if tipo == "arma":
            return f"[Arma] {objeto.getNome()} | Ataque +{objeto.getBonusAtaque()} | Preco {objeto.getPreco()}"
        if tipo == "armadura":
            return f"[Armadura] {objeto.getNome()} | Defesa +{objeto.getBonusDefesa()} | Preco {objeto.getPreco()}"
        if tipo == "pocao":
            return f"[MaxDoc] {objeto.getNome()} | Cura {objeto.getValorCura()} | Preco {objeto.getPreco()}"
        return f"[Consumivel] {objeto.getNome()} | Dano {objeto.getDanoMinimo()}-{objeto.getDanoMaximo()} | Preco {objeto.getPreco()}"

    def mostrarLoja(self):
        # Imprime a lista de itens visíveis (com número à frente de cada
        # um, para o jogador poder escolher pelo número em venderItem()).
        print("\n===== MERCADO NEGRO =====")
        print("Vendedor:", self.__nomeVendedor)
        print("O vendedor olha para ti como quem ja viu pior.")

        if not self.__itensVisiveis:
            print("Nao ha itens disponiveis neste momento.")
            return

        for indice, item in enumerate(self.__itensVisiveis, start=1):
            print(f"{indice} - {self.__descricaoItem(item)}")

    def __removerDoCatalogo(self, tipo, objeto):
        # Depois de um item ser vendido, removemo-lo também do catálogo
        # completo (não só da lista visível), para não voltar a aparecer.
        if tipo == "arma" and objeto in self.__armasDisponiveis:
            self.__armasDisponiveis.remove(objeto)
        elif tipo == "armadura" and objeto in self.__armadurasDisponiveis:
            self.__armadurasDisponiveis.remove(objeto)
        elif tipo == "pocao" and objeto in self.__pocoesDisponiveis:
            self.__pocoesDisponiveis.remove(objeto)
        elif tipo == "consumivel" and objeto in self.__consumiveisDisponiveis:
            self.__consumiveisDisponiveis.remove(objeto)

    def venderItem(self, jogador, indice):
        # Processa a compra do item na posição "indice" (o número que o
        # jogador escolheu no menu da loja, começando em 1).
        # Faz várias verificações antes de concluir a venda:
        #   - o índice é válido?
        #   - se for poção/consumível, o inventário do jogador tem espaço?
        #   - o jogador tem créditos suficientes?
        # Devolve True se a compra foi concluída, False caso contrário.
        if indice < 1 or indice > len(self.__itensVisiveis):
            print("Escolha invalida.")
            return False

        item = self.__itensVisiveis[indice - 1]
        tipo = item["tipo"]
        objeto = item["objeto"]
        preco = objeto.getPreco()

        if tipo in ("pocao", "consumivel") and jogador.inventarioCheio():
            print("O teu inventario esta cheio. Liberta espaco antes de comprar mais itens.")
            return False

        if not jogador.gastarMoedas(preco):
            print("Nao tens creditos suficientes para esta compra.")
            return False

        # Dependendo do tipo de item, a ação após a compra é diferente:
        # armas/armaduras equipam-se logo; poções/consumíveis vão para o inventário.
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
            sucesso = jogador.adicionarConsumivelCombate(objeto)
            if sucesso:
                print(f"Compraste {objeto.getNome()}!")

        if not sucesso:
            # Se por algum motivo o item não pôde ser entregue (ex: inventário
            # ficou cheio entre a verificação e agora), devolvemos as moedas.
            jogador.ganharMoedas(preco)
            print("Nao foi possivel concluir a compra.")
            return False

        # Remove o item comprado da loja (não pode ser comprado outra vez).
        self.__itensVisiveis.pop(indice - 1)
        self.__removerDoCatalogo(tipo, objeto)
        return True
