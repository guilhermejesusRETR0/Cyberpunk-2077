import os
import random
from Companheiro import Companheiro
from Recursos import Recursos


class Afterlife:
    def __init__(self):
        self.__mercenarios = []
        self.gerarMercenarios()

    def lerOpcaoSimNao(self, mensagem):
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
                "A atiradora letal que transforma os teus ataques em tiros críticos." ,
                random.randint(60, 80),
                "panam.txt",
                bonusCritico=10,
            ),
        ]

    def getMercenarios(self):
        return self.__mercenarios

    def obterResumoBonus(self, mercenario):
        partes = []
        if mercenario.getBonusAtaque():
            partes.append(f"+{mercenario.getBonusAtaque()} ataque")
        if mercenario.getBonusVidaMaxima():
            partes.append(f"+{mercenario.getBonusVidaMaxima()} vida máxima")
        if mercenario.getBonusCura():
            partes.append(f"+{mercenario.getBonusCura()} cura")
        if mercenario.getBonusCritico():
            partes.append(f"+{mercenario.getBonusCritico()} dano crítico")
        if mercenario.getBonusExperiencia():
            partes.append(f"+{mercenario.getBonusExperiencia()}% experiência")
        return ", ".join(partes)

    def mostrarMercenarios(self, jogador):
        Recursos.imprimirTitulo("AFTERLIFE")
        print("O bar do Afterlife está cheio de rumores e contratos. Escolhe um nome para ver o perfil completo.")
        print()

        for indice, mercenario in enumerate(self.__mercenarios, start=1):
            status = "(recrutado)" if jogador.temCompanheiro(mercenario.getNome()) else ""
            print(f"{indice} - {mercenario.getNome()} {status}")

        print("5 - Voltar para a rua")

    def mostrarDetalhesMercenario(self, jogador, escolha):
        if escolha < 1 or escolha > len(self.__mercenarios):
            print("Escolha inválida no Afterlife.")
            return

        mercenario = self.__mercenarios[escolha - 1]
        print()
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
