# ============================================================
# CLASSE AFTERLIFE
# Representa o bar "Afterlife", onde o jogador pode ver e recrutar
# mercenários (Companheiros) para a sua equipa.
#
# COMO ADICIONAR UM NOVO MERCENÁRIO:
# Vai ao método gerarMercenarios() lá abaixo e acrescenta um novo
# bloco Companheiro(...) à lista. Não te esqueças de também colocar
# o ficheiro .txt com a arte ASCII dele na pasta "companheiros/".
# ============================================================

import os
import random
from Companheiro import Companheiro
from Recursos import Recursos


class Afterlife:

    def __init__(self):
        self.__mercenarios = []   # Lista com todos os mercenários disponíveis no bar
        self.gerarMercenarios()   # Já preenchemos a lista logo ao criar o Afterlife

    def lerOpcaoSimNao(self, mensagem):
        # Pergunta ao jogador uma questão de sim/não (ex: "queres recrutar?").
        # Aceita respostas como "s", "sim", "n", "nao", em qualquer capitalização.
        # Devolve True para sim, False para não, e None se o jogador cancelar
        # a entrada (ex: fechar o programa a meio).
        while True:
            try:
                resposta = input(mensagem).strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nEntrada cancelada.")
                return None

            if resposta.startswith("s"):
                return True
            if resposta.startswith("n"):
                return False

            print("Opcao invalida. Responde com s ou n.")

    def gerarMercenarios(self):
        # Cria a lista fixa de mercenários disponíveis no Afterlife.
        # Os valores de preço (random.randint) variam um pouco a cada
        # vez que o jogo é iniciado, para dar variedade.
        self.__mercenarios = [
            Companheiro(
                "Johnny Silverhand",
                "Mercenário",
                "O veterano com cicatrizes e munição mental.",
                random.randint(55, 70),
                "johnny silverhand.txt",
                bonusAtaque=10,
            ),
            Companheiro(
                "Lucy",
                "Netrunner",
                "A especialista em redes que consegue virar qualquer combate a teu favor.",
                random.randint(45, 60),
                "lucy.txt",
                bonusExperiencia=10,
            ),
            Companheiro(
                "Trauma Team",
                "Médico de campo",
                "O médico de elite que aumenta a tua sobrevivência em cada missão.",
                random.randint(35, 50),
                "trauma team.txt",
                bonusVidaMaxima=10,
                bonusCura=10,
            ),
            Companheiro(
                "Panam",
                "Sniper",
                "A atiradora letal que aumenta a potência de cada disparo teu.",
                random.randint(60, 80),
                "panam.txt",
                bonusAtaque=10,
            ),
        ]

    def getMercenarios(self):
        return self.__mercenarios

    def obterResumoBonus(self, mercenario):
        # Constrói um texto curto tipo "+10 ataque, +10% experiência"
        # juntando só os bónus que este mercenário realmente tem.
        partes = []
        if mercenario.getBonusAtaque():
            partes.append(f"+{mercenario.getBonusAtaque()} ataque")
        if mercenario.getBonusVidaMaxima():
            partes.append(f"+{mercenario.getBonusVidaMaxima()} vida máxima")
        if mercenario.getBonusCura():
            partes.append(f"+{mercenario.getBonusCura()} cura")
        if mercenario.getBonusExperiencia():
            partes.append(f"+{mercenario.getBonusExperiencia()}% experiência")
        return ", ".join(partes)

    def mostrarMercenarios(self, jogador):
        # Mostra a lista de mercenários disponíveis (menu do Afterlife).
        # Junto a cada nome aparece "(recrutado)" se o jogador já o tiver.
        Recursos.imprimirTitulo("AFTERLIFE")
        print("O bar do Afterlife está cheio de rumores e contratos. Escolhe um nome para ver o perfil completo.")
        print()

        for indice, mercenario in enumerate(self.__mercenarios, start=1):
            status = "(recrutado)" if jogador.temCompanheiro(mercenario.getNome()) else ""
            print(f"{indice} - {mercenario.getNome()} {status}")

        print("5 - Voltar para a rua")

    def mostrarDetalhesMercenario(self, jogador, escolha):
        # Mostra o perfil completo de um mercenário (arte, descrição, bónus,
        # preço) e, se ainda não foi recrutado, pergunta se o jogador quer
        # recrutá-lo agora.
        if escolha < 1 or escolha > len(self.__mercenarios):
            print("Escolha inválida no Afterlife.")
            return

        mercenario = self.__mercenarios[escolha - 1]
        print()
        # Vai buscar a arte ASCII do mercenário à pasta "companheiros/".
        # Se o ficheiro não existir, mostra o texto alternativo em vez de dar erro.
        caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "companheiros", mercenario.getArquivo())
        Recursos.imprimirAscii(caminho, "[Arte não disponível]")
        print("\n===== PERFIL DO MERCENÁRIO =====")
        print("Nome:", mercenario.getNome())
        print("Papel:", mercenario.getPapel())
        print("Descrição:", mercenario.getDescricao())
        print("Bónus:", self.obterResumoBonus(mercenario))
        print("Preço:", mercenario.getPreco(), "créditos")

        if jogador.temCompanheiro(mercenario.getNome()):
            print("\nEste mercenário já faz parte da tua equipa.")
            return

        escolha_compra = self.lerOpcaoSimNao("Queres recrutar este mercenario? (s/n): ")
        if escolha_compra is None:
            return

        if escolha_compra:
            self.recrutarMercenario(jogador, escolha)
        else:
            print("Voltaste para a lista de mercenários.")

    def recrutarMercenario(self, jogador, escolha):
        # Tenta recrutar o mercenário escolhido: verifica se já não está
        # na equipa e se o jogador tem créditos suficientes.
        if escolha < 1 or escolha > len(self.__mercenarios):
            print("Escolha inválida no Afterlife.")
            return

        mercenario = self.__mercenarios[escolha - 1]

        if jogador.temCompanheiro(mercenario.getNome()):
            print(f"{mercenario.getNome()} já faz parte da tua equipa.")
            return

        if jogador.gastarMoedas(mercenario.getPreco()):
            jogador.recrutarCompanheiro(mercenario)
            print(f"Recrutaste {mercenario.getNome()}!")
            caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "companheiros", mercenario.getArquivo())
            Recursos.imprimirAscii(caminho, "[Arte não disponível]")
            print("Este companheiro ficará contigo até o jogo reiniciar.")
        else:
            print("Não tens créditos suficientes para recrutar este mercenário.")
