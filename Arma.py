# ============================================================
# CLASSE ARMA
# Representa uma arma que o jogador pode comprar e equipar.
# Uma arma dá um bónus fixo de ataque enquanto estiver equipada.
# ============================================================

class Arma:

    def __init__(self, nome, bonusAtaque, preco):
        # Construtor: é chamado sempre que criamos uma arma nova.
        # Exemplo de uso: Arma("Katana Mk2", 8, 48)
        self.__nome = nome                # Nome da arma (texto)
        self.__bonusAtaque = bonusAtaque  # Quanto ataque extra esta arma dá
        self.__preco = preco              # Quanto custa em créditos

    # ---------- GETTERS ----------
    # Os métodos "get..." servem apenas para LER o valor de um atributo.
    # Como os atributos começam com "__", não podem ser lidos diretamente
    # de fora da classe (ex: arma.__nome dá erro) - por isso usamos getters.

    def getNome(self):
        return self.__nome

    def getBonusAtaque(self):
        return self.__bonusAtaque

    def getPreco(self):
        return self.__preco

    # ---------- SETTERS ----------
    # Os métodos "set..." servem para ALTERAR o valor de um atributo
    # depois da arma já ter sido criada.

    def setNome(self, nome):
        self.__nome = nome

    def setBonusAtaque(self, bonusAtaque):
        self.__bonusAtaque = bonusAtaque

    def setPreco(self, preco):
        self.__preco = preco

    # ---------- OUTROS MÉTODOS ----------

    def mostrarDados(self):
        # Imprime na consola as informações desta arma.
        # Útil para mostrar os detalhes de um item na loja.
        print("Arma:", self.__nome)
        print("Bónus de ataque:", self.__bonusAtaque)
        print("Preço:", self.__preco, "créditos")
