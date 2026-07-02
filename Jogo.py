from Inimigo import Inimigo
from Jogador import Jogador
from Loja import Loja
from Masmorra import Masmorra
from Recursos import Recursos


class Jogo:
    def __init__(self):
        self.__jogador = None
        self.__masmorraAtual = 1
        self.__inimigoAtual = None
        self.__loja = Loja()
        self.__terminado = False

    def getJogador(self):
        return self.__jogador

    def getMasmorraAtual(self):
        return self.__masmorraAtual

    def getInimigoAtual(self):
        return self.__inimigoAtual

    def getLoja(self):
        return self.__loja

    def getTerminado(self):
        return self.__terminado

    def setJogador(self, jogador):
        self.__jogador = jogador

    def setMasmorraAtual(self, masmorraAtual):
        self.__masmorraAtual = masmorraAtual

    def setInimigoAtual(self, inimigoAtual):
        self.__inimigoAtual = inimigoAtual

    def setLoja(self, loja):
        self.__loja = loja

    def setTerminado(self, terminado):
        self.__terminado = terminado

    def lerOpcao(self, mensagem):
        try:
            return input(mensagem)
        except (EOFError, KeyboardInterrupt):
            print("\nA ligação com a rede caiu. O ciclo termina aqui.")
            self.__terminado = True
            return ""

    def iniciarJogo(self):
        self.mostrarIntroducao()

        nome = self.lerOpcao("\nInsere o nome da tua mercenária: ")

        if self.__terminado:
            return

        if nome == "":
            nome = "Nyx"
            print("Não escreveste nome. O sistema atribuiu-te um codinome de serviço:")
            print("Nyx.")

        self.criarJogador(nome)

        while self.__terminado is False:
            self.mostrarMenuPrincipal()
            opcao = self.lerOpcao("Escolha: ")

            if self.__terminado:
                break

            Recursos.limparConsola()

            if opcao == "1":
                Recursos.limparConsola()
                self.__jogador.mostrarEstado()
                Recursos.esperarEnter("Premir ENTER para voltar à rua...")

            elif opcao == "2":
                self.explorarMasmorra()

            elif opcao == "3":
                self.visitarLoja()

            elif opcao == "4":
                self.descansar()

            elif opcao == "5":
                Recursos.pararAudio()
                print("\nDecidiste desaparecer da cidade.")
                print("Os sensores da megacorporação nem notam a tua ausência.")
                print("A tua conta de créditos continua a zero, como sempre.")
                self.__terminado = True

            else:
                print("\nOpção inválida.")
                print("Até na sombra da cidade se esperava mais precisão.")

    def mostrarIntroducao(self):
        Recursos.limparConsola()
        print("\033[33m")  # Amarelo
        Recursos.tocarAudio("assets/audio/intro.wav")
        Recursos.tocarAudioFundo("The-Rebel-Path-_Cyberpunk-2077-Soundtrack_.wav")
        Recursos.imprimirAscii(
            "assets/ascii/logo.txt",
            """
    ======================================
               CYBERDUNGEONS
    ======================================
            """
        )
        print("\033[0m")  # Reset

        Recursos.pausa(1)

        print("\nNeon. Chuva. Máquinas a consumir o resto da tua sanidade.")
        Recursos.pausa(1)
        print("És um mercenário contratado para entrar numa instalação fortificada.")
        Recursos.pausa(1)
        print("No fundo dessa estrutura, uma IA experimental prepara-se para tomar o controlo da cidade.")
        Recursos.pausa(1)
        print("O teu trabalho é simples: infiltrar-te, sobreviver e destruir o núcleo antes que a megacorporação te use como peça de reposição.")
        print()
        Recursos.pausa(1)
        print("Não há heróis aqui. Só gente com implantes, dívidas e má sorte.")
        print("Bem-vindo ao abismo digital.")
        print("O teu relógio já está a contar os segundos até a primeira falha de sistema.")

    def criarJogador(self, nome):
        vidaMaxima = 100
        ataque = 10
        defesa = 5
        nivel = 1
        experiencia = 0
        moedas = 40

        self.__jogador = Jogador(nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas)

        print("\nPerfil activado com sucesso.")
        print("Nome:", nome)
        print("Classificação: Mercenário de rua")
        print("Estado: com um crédito e vários problemas")

    def mostrarMenuPrincipal(self):
        Recursos.limparConsola()
        print("\n===== MENU PRINCIPAL =====")
        print("Zona atual:", self.__masmorraAtual)
        print("1 - Ver perfil")
        print("2 - Explorar zona")
        print("3 - Visitar mercado negro")
        print("4 - Procurar assistência")
        print("5 - Sair")

    def criarMasmorraAtual(self):
        if self.__masmorraAtual == 1:
            return Masmorra(
                1,
                "Bairro controlado por gangues",
                "Neon a piscar, portas corroídas e um cheiro a pólvora que nunca te abandona."
            )

        elif self.__masmorraAtual == 2:
            return Masmorra(
                2,
                "Estação de metro abandonada",
                "Túneis de ferro, cablagem exposta e ecos que parecem vir de dentro da tua cabeça."
            )

        elif self.__masmorraAtual == 3:
            return Masmorra(
                3,
                "Laboratório clandestino",
                "Água a pingar, sistemas em falha e um cheiro químico que te faz duvidar da tua própria genética."
            )

        elif self.__masmorraAtual == 4:
            return Masmorra(
                4,
                "Central de dados",
                "Painéis de vidro, servidores a rugir e a sensação de que alguém te está a observar desde o silêncio."
            )

        else:
            return Masmorra(
                5,
                "Complexo industrial automatizado",
                "Robôs a trabalhar, alarmes a gritar e o último piso a cheirar a futuro em decomposição."
            )

    def criarInimigoDaMasmorra(self):
        if self.__masmorraAtual == 1:
            return Inimigo("Ganger de neon", 30, 7, 2, 20, 15)

        elif self.__masmorraAtual == 2:
            return Inimigo("Mercenário com implantes", 45, 10, 4, 30, 25)

        elif self.__masmorraAtual == 3:
            return Inimigo("Andróide de segurança", 65, 13, 6, 45, 35)

        elif self.__masmorraAtual == 4:
            return Inimigo("Drone de combate", 85, 17, 8, 60, 50)

        else:
            return Inimigo("IA de segurança", 120, 22, 12, 100, 100)

    def explorarMasmorra(self):
        masmorra = self.criarMasmorraAtual()
        self.__inimigoAtual = self.criarInimigoDaMasmorra()

        masmorra.mostrarInfo()

        print("\nAo entrares, sentes o pulso da cidade na pele.")
        print("O teu visor dispara uma mensagem de alerta:")
        print('"Falha de sistema detectada. A rua não está a cooperar."')

        print("\nUm alvo apareceu na tua frente!")
        print("Inimigo:", self.__inimigoAtual.getNome())

        self.iniciarCombate()

    def iniciarCombate(self):
        print("\n===== COMBATE =====")

        while True:
            print("\n1 - Atacar")
            print("2 - Usar nano kit")
            print("3 - Ver estado")
            print("4 - Fugir")
            opcao = self.lerOpcao("Escolha: ")

            if self.__terminado:
                break

            if opcao == "1":
                self.__jogador.atacar(self.__inimigoAtual)
                if not self.__inimigoAtual.estaVivo():
                    self.processarVitoria()
                    break

                self.__inimigoAtual.atacar(self.__jogador)
                if not self.__jogador.estaVivo():
                    self.processarDerrota()
                    break

            elif opcao == "2":
                if self.__jogador.usarPocao():
                    print("Usaste um nano kit.")
                else:
                    print("Não tens nano kits guardados.")

                if self.__inimigoAtual.estaVivo():
                    self.__inimigoAtual.atacar(self.__jogador)
                    if not self.__jogador.estaVivo():
                        self.processarDerrota()
                        break

            elif opcao == "3":
                self.__jogador.mostrarEstado()
                self.__inimigoAtual.mostrarEstado()

            elif opcao == "4":
                print("Fugiste do combate.")
                break

            else:
                print("Opção inválida.")

    def processarVitoria(self):
        print("\nVitória!")
        print(f"{self.__jogador.getNome()} destruiu {self.__inimigoAtual.getNome()}.")
        self.__jogador.ganharExperiencia(self.__inimigoAtual.getExperiencia())
        self.__jogador.ganharMoedas(self.__inimigoAtual.getMoedas())

        if self.__masmorraAtual == 5:
            print("Conseguiste invadir o núcleo da IA e cortar o controlo da megacorporação.")
            self.__terminado = True
        else:
            print("Recebeste créditos e podes avançar para a próxima zona.")
            self.avancarMasmorra()

    def processarDerrota(self):
        print("\nDerrota!")
        print("Os teus implantes falham. A cidade não te esquece e tu deixas de existir em modo de economia.")
        self.__terminado = True

    def avancarMasmorra(self):
        if self.__masmorraAtual < 5:
            self.__masmorraAtual += 1
            print(f"Avançaste para a zona {self.__masmorraAtual}.")
        else:
            print("Já atingiste o último ponto da rede.")

    def visitarLoja(self):
        self.__loja.gerarProdutos(self.__masmorraAtual)
        self.__loja.mostrarProdutos()

        print("\n===== MERCADO NEGRO =====")
        print("1 - Comprar arma inteligente")
        print("2 - Comprar blindagem cibernética")
        print("3 - Comprar nano kit")
        print("4 - Sair do mercado")

        opcao = input("Escolha: ")

        if opcao == "1":
            self.__loja.comprarArma(self.__jogador)

        elif opcao == "2":
            self.__loja.comprarArmadura(self.__jogador)

        elif opcao == "3":
            self.__loja.comprarPocao(self.__jogador)

        elif opcao == "4":
            print("\nSaíste do mercado.")
            print("O vendedor murmura: 'Volta quando estiveres mais desesperado e com mais créditos.'")

        else:
            print("\nOpção inválida no mercado.")
            print("O vendedor encolhe os ombros como se a culpa fosse do sistema.")

    def descansar(self):
        if self.__jogador is not None:
            self.__jogador.curar(25)
            print("Entraste na clínica clandestina e recuperaste parte da tua integridade.")
        else:
            print("Ainda não existe uma mercenária criada.")

    def verificarFimDoJogo(self):
        return self.__terminado or (self.__jogador is not None and not self.__jogador.estaVivo())
