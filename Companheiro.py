# ============================================================
# CLASSE COMPANHEIRO
# Representa um mercenário que pode ser recrutado no Afterlife
# (ver Afterlife.py). Cada companheiro dá um bónus passivo ao
# jogador enquanto estiver na equipa (ex: mais ataque, mais vida).
#
# IMPORTANTE PARA QUEM QUER ADICIONAR NOVOS COMPANHEIROS:
# Os parâmetros "bonus..." têm todos o valor 0 por defeito. Isto
# significa que, ao criar um companheiro novo, só precisas de indicar
# os bónus que ele realmente tem (os outros ficam a 0 automaticamente).
# Exemplo: Companheiro("Nome", "Papel", "Descricao", 50, "ficheiro.txt", bonusAtaque=10)
# ============================================================

class Companheiro:

    def __init__(
        self,
        nome,
        papel,
        descricao,
        preco,
        arquivo,
        bonusAtaque=0,
        bonusVidaMaxima=0,
        bonusCura=0,
        bonusExperiencia=0
    ):
        self.__nome = nome                        # Nome do mercenário (ex: "Johnny Silverhand")
        self.__papel = papel                      # Função dele (ex: "Netrunner", "Sniper")
        self.__descricao = descricao              # Texto descritivo mostrado no perfil
        self.__preco = preco                      # Quanto custa recrutá-lo, em créditos
        self.__arquivo = arquivo                  # Nome do ficheiro .txt com a arte ASCII dele
        self.__bonusAtaque = bonusAtaque          # Bónus de ataque dado ao jogador
        self.__bonusVidaMaxima = bonusVidaMaxima  # Bónus de vida máxima dado ao jogador
        self.__bonusCura = bonusCura              # Bónus de cura dado ao jogador (poções/descanso)
        self.__bonusExperiencia = bonusExperiencia  # Bónus de % de experiência ganha em combate

    # ---------- GETTERS ----------

    def getNome(self):
        return self.__nome

    def getPapel(self):
        return self.__papel

    def getDescricao(self):
        return self.__descricao

    def getPreco(self):
        return self.__preco

    def getArquivo(self):
        return self.__arquivo

    def getBonusAtaque(self):
        return self.__bonusAtaque

    def getBonusVidaMaxima(self):
        return self.__bonusVidaMaxima

    def getBonusCura(self):
        return self.__bonusCura

    def getBonusExperiencia(self):
        return self.__bonusExperiencia

    # ---------- OUTROS MÉTODOS ----------

    def mostrarDados(self):
        # Imprime os dados deste companheiro na consola.
        # Só mostra os bónus que o companheiro realmente tem (diferentes de 0).
        print(f"{self.__nome} - {self.__papel}")
        print(self.__descricao)
        print("Preço:", self.__preco, "créditos")
        if self.__bonusAtaque:
            print("Bónus de ataque:", self.__bonusAtaque)
        if self.__bonusVidaMaxima:
            print("Bónus de vida máxima:", self.__bonusVidaMaxima)
        if self.__bonusCura:
            print("Bónus de cura:", self.__bonusCura)
        if self.__bonusExperiencia:
            print("Bónus de experiência:", self.__bonusExperiencia)
