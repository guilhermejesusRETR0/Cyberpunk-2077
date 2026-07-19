# ============================================================
# CLASSE MASMORRA
# Representa uma "zona" do jogo (ex: um bairro, uma estação de metro).
# Cada masmorra tem um nome, uma descrição e sabe para que outras
# zonas o jogador pode avançar a partir dela (caminhosDisponiveis).
# Esta classe é só para mostrar informação - não tem lógica de combate.
# ============================================================

class Masmorra:

    def __init__(self, numero, nome, descricao, caminhosDisponiveis=None):
        # Construtor: cria uma nova zona/masmorra.
        # "caminhosDisponiveis" é uma lista de números de outras zonas
        # para onde o jogador pode ir a partir desta (ex: [2, 3]).
        # Se não passarmos nada, fica como lista vazia (zona sem saída).
        self.__numero = numero
        self.__nome = nome
        self.__descricao = descricao
        self.__caminhosDisponiveis = list(caminhosDisponiveis) if caminhosDisponiveis is not None else []

    # ---------- GETTERS ----------

    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    def getDescricao(self):
        return self.__descricao

    def getCaminhosDisponiveis(self):
        # Devolvemos uma CÓPIA da lista (list(...)) e não a lista original,
        # para evitar que quem chamar este método altere por acidente
        # os caminhos reais desta masmorra.
        return list(self.__caminhosDisponiveis)

    # ---------- SETTERS ----------

    def setNumero(self, numero):
        self.__numero = numero

    def setNome(self, nome):
        self.__nome = nome

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setCaminhosDisponiveis(self, caminhosDisponiveis):
        self.__caminhosDisponiveis = list(caminhosDisponiveis) if caminhosDisponiveis is not None else []

    # ---------- OUTROS MÉTODOS ----------

    def mostrarInformacao(self):
        # Imprime o nome e a descrição desta zona (usado ao explorar).
        print("\n===== ZONA ATUAL =====")
        print("Número:", self.__numero)
        print("Nome:", self.__nome)
        print("Descrição:", self.__descricao)

    def mostrarCaminhosDisponiveis(self):
        # Imprime para que zonas o jogador pode seguir a partir desta.
        if self.__caminhosDisponiveis:
            print("Caminhos possiveis:", ", ".join(str(caminho) for caminho in self.__caminhosDisponiveis))
        else:
            print("Caminhos possiveis: nenhum")
