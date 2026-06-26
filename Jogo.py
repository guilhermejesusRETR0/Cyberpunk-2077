try:
    from FichaPratica04.Inimigo import Inimigo
    from FichaPratica04.Jogador import Jogador
    from FichaPratica04.Loja import Loja
    from FichaPratica04.Masmorra import Masmorra
    from FichaPratica04.Recursos import Recursos
except ModuleNotFoundError:
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
            print("\nEntrada encerrada. O jogo termina.")
            self.__terminado = True
            return ""

    def iniciarJogo(self):
        self.mostrarIntroducao()

        nome = self.lerOpcao("\nInsere o nome da tua personagem: ")

        if self.__terminado:
            return

        if nome == "":
            nome = "Joaquim"
            print("Não escreveste nome. O sistema medieval atribuiu-te um nome altamente épico:")
            print("Joaquim.")

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
                Recursos.esperarEnter("Premir ENTER para voltar ao menu...")

            elif opcao == "2":
                self.explorarMasmorra()

            elif opcao == "3":
                self.visitarLoja()

            elif opcao == "4":
                self.descansar()

            elif opcao == "5":
                Recursos.pararAudio()
                print("\nDecidiste sair do jogo.")
                print("A máquina do tempo fica para outro dia.")
                print("O ano 1272 agradece a tua curta visita.")
                self.__terminado = True

            else:
                print("\nOpção inválida.")
                print("Até no ano 1272 era esperado saber escolher uma opção do menu.")

    def mostrarIntroducao(self):
        Recursos.limparConsola()
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

        Recursos.pausa(1)

        print("\nAno 2077.")
        Recursos.pausa(1)
        print("A humanidade finalmente conseguiu viajar no tempo.")
        Recursos.pausa(1)
        print("Infelizmente, alguém decidiu testar a máquina numa sexta-feira à tarde.")
        Recursos.pausa(1)
        print("Como seria de esperar, correu mal.")
        print()
        Recursos.pausa(1)
        print("Durante a viagem, ocorreu uma ruptura temporal.")
        print("A tua personagem foi enviada para o ano 1272.")
        print("Sem internet. Sem GPS. Sem carregador. Sem garantias.")
        print()
        Recursos.pausa(1)
        print("A máquina do tempo caiu algures no fundo de várias masmorras medievais.")
        print("Para regressares ao ano 2077, tens de sobreviver, lutar e recuperar o núcleo temporal.")
        print()
        Recursos.pausa(1)
        print("Bem-vindo a Cyberdungeons.")
        print("Um RPG medieval com problemas tecnológicos que ninguém pediu.")

    def criarJogador(self, nome):
        vidaMaxima = 100
        ataque = 10
        defesa = 5
        nivel = 1
        experiencia = 0
        moedas = 40

        self.__jogador = Jogador(nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas)

        print("\nPersonagem criada com sucesso.")
        print("Nome:", nome)
        print("Ano de origem: 2077")
        print("Ano atual: 1272")
        print("Estado emocional: confuso, mas funcional.")

    def mostrarMenuPrincipal(self):
        Recursos.limparConsola()
        print("\n===== MENU PRINCIPAL =====")
        print("Masmorra atual:", self.__masmorraAtual)
        print("1 - Ver personagem")
        print("2 - Explorar masmorra")
        print("3 - Visitar loja")
        print("4 - Descansar")
        print("5 - Sair")

    def criarMasmorraAtual(self):
        if self.__masmorraAtual == 1:
            return Masmorra(
                1,
                "Masmorra da Floresta Perdida",
                "Uma floresta húmida onde até as árvores parecem julgar as tuas escolhas."
            )

        elif self.__masmorraAtual == 2:
            return Masmorra(
                2,
                "Cripta dos Ecos Temporais",
                "Uma cripta onde se ouvem vozes do passado, do futuro e de alunos a perguntar se isto sai no teste."
            )

        elif self.__masmorraAtual == 3:
            return Masmorra(
                3,
                "Fortaleza do Gelo Eterno",
                "Uma fortaleza gelada. O frio é tanto que até os bugs congelam."
            )

        elif self.__masmorraAtual == 4:
            return Masmorra(
                4,
                "Templo da Fenda Temporal",
                "Um templo instável onde ontem, hoje e amanhã discutem quando é que se assinam as folhas."
            )

        else:
            return Masmorra(
                5,
                "Câmara da Máquina do Tempo",
                "A última masmorra. A máquina está perto. O Wi-Fi ainda não."
            )

    def criarInimigoDaMasmorra(self):
        if self.__masmorraAtual == 1:
            return Inimigo("Goblin da Floresta", 30, 7, 2, 20, 15)

        elif self.__masmorraAtual == 2:
            return Inimigo("Esqueleto da Cripta", 45, 10, 4, 30, 25)

        elif self.__masmorraAtual == 3:
            return Inimigo("Cavaleiro de Gelo", 65, 13, 6, 45, 35)

        elif self.__masmorraAtual == 4:
            return Inimigo("Cultista da Fenda", 85, 17, 8, 60, 50)

        else:
            return Inimigo("Guardião do Núcleo Temporal", 120, 22, 12, 100, 100)

    def explorarMasmorra(self):
        masmorra = self.criarMasmorraAtual()
        self.__inimigoAtual = self.criarInimigoDaMasmorra()

        masmorra.mostrarInfo()

        print("\nAo entrares, sentes uma energia estranha no ar.")
        print("O teu relógio futurista mostra a seguinte mensagem:")
        print('"Erro 1272: realidade medieval não suportada."')

        print("\nUm inimigo apareceu!")
        print("Inimigo:", self.__inimigoAtual.getNome())

        self.iniciarCombate()

    def iniciarCombate(self):
        print("\n===== COMBATE =====")

        while True:
            print("\n1 - Atacar")
            print("2 - Usar poção")
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
                    print("Usaste uma poção.")
                else:
                    print("Não tens poções guardadas.")

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
        print(f"{self.__jogador.getNome()} derrotou {self.__inimigoAtual.getNome()}.")
        self.__jogador.ganharExperiencia(self.__inimigoAtual.getExperiencia())
        self.__jogador.ganharMoedas(self.__inimigoAtual.getMoedas())

        if self.__masmorraAtual == 5:
            print("Conseguiste recuperar o núcleo temporal e regressar ao futuro!")
            self.__terminado = True
        else:
            print("Recebeste recompensas e podes avançar para a próxima masmorra.")
            self.avancarMasmorra()

    def processarDerrota(self):
        print("\nDerrota!")
        print("Ficaste sem vida. A tua aventura termina aqui.")
        self.__terminado = True

    def avancarMasmorra(self):
        if self.__masmorraAtual < 5:
            self.__masmorraAtual += 1
            print(f"Avançaste para a masmorra {self.__masmorraAtual}.")
        else:
            print("Já atingiste a última masmorra.")

    def visitarLoja(self):
        self.__loja.gerarProdutos(self.__masmorraAtual)
        self.__loja.mostrarProdutos()

        print("\n===== MENU DA LOJA =====")
        print("1 - Comprar arma")
        print("2 - Comprar armadura")
        print("3 - Comprar poção")
        print("4 - Sair da loja")

        opcao = input("Escolha: ")

        if opcao == "1":
            self.__loja.comprarArma(self.__jogador)

        elif opcao == "2":
            self.__loja.comprarArmadura(self.__jogador)

        elif opcao == "3":
            self.__loja.comprarPocao(self.__jogador)

        elif opcao == "4":
            print("\nSaíste da loja.")
            print("O ferreiro grita: 'Volta sempre! E traz moedas, não aceitamos MB Way!'")

        else:
            print("\nOpção inválida na loja.")
            print("O ferreiro suspira medievalmente.")

    def descansar(self):
        if self.__jogador is not None:
            self.__jogador.curar(25)
            print("Descansaste e recuperaste parte da tua vida.")
        else:
            print("Ainda não existe um jogador criado.")

    def verificarFimDoJogo(self):
        return self.__terminado or (self.__jogador is not None and not self.__jogador.estaVivo())
