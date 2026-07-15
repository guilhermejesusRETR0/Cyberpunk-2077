from Inimigo import Inimigo
from Jogador import Jogador
from Loja import Loja
from Masmorra import Masmorra
from Recursos import Recursos
from Afterlife import Afterlife


class Jogo:
    def __init__(self):
        self.__jogador = None
        self.__masmorraAtual = 1
        self.__inimigoAtual = None
        self.__loja = Loja()
        self.__afterlife = Afterlife()
        self.__terminado = False
        self.__totalZonas = 5
        self.__descansosUsados = 0
        self.__descansosMaximos = self.__totalZonas // 3
        self.__zonas = {
            1: {
                "nome": "Bairro controlado por gangues",
                "descricao": "Neon a piscar, portas corroidas e um cheiro a polvora que nunca te abandona.",
                "caminhos": [2, 3],
                "inimigo": ("Ganger de neon", 30, 7, 2, 20, 15),
            },
            2: {
                "nome": "Estacao de metro abandonada",
                "descricao": "Tuneis de ferro, cablagem exposta e ecos que parecem vir de dentro da tua cabeca.",
                "caminhos": [3, 4],
                "inimigo": ("Mercenario com implantes", 45, 10, 4, 30, 25),
            },
            3: {
                "nome": "Laboratorio clandestino",
                "descricao": "Agua a pingar, sistemas em falha e um cheiro quimico que te faz duvidar da tua propria genetica.",
                "caminhos": [4, 5],
                "inimigo": ("Androide de seguranca", 65, 13, 6, 45, 35),
            },
            4: {
                "nome": "Central de dados",
                "descricao": "Paineis de vidro, servidores a rugir e a sensacao de que alguem te esta a observar desde o silencio.",
                "caminhos": [5],
                "inimigo": ("Drone de combate", 85, 17, 8, 60, 50),
            },
            5: {
                "nome": "Nucleo da IA",
                "descricao": "O ultimo piso. O coracao da maquina. Aqui termina a fuga ou termina a tua historia.",
                "caminhos": [],
                "inimigo": ("IA de seguranca", 120, 22, 12, 100, 100),
            },
        }

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
            return input(mensagem).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nA ligacao com a rede caiu. O ciclo termina aqui.")
            self.__terminado = True
            return ""

    def lerInteiroEntre(self, mensagem, minimo, maximo):
        while not self.__terminado:
            valorTexto = self.lerOpcao(mensagem)
            if self.__terminado:
                return None

            try:
                valor = int(valorTexto)
            except ValueError:
                print("Entrada invalida.")
                continue

            if minimo <= valor <= maximo:
                return valor

            print(f"Escolhe um valor entre {minimo} e {maximo}.")

        return None

    def esperarEnterSeguro(self, mensagem):
        try:
            input("\n" + mensagem)
        except (EOFError, KeyboardInterrupt):
            pass

    def __dadosZona(self, numeroZona):
        return self.__zonas.get(numeroZona, self.__zonas[self.__totalZonas])

    def iniciarJogo(self):
        self.mostrarIntroducao()

        nome = self.lerOpcao("\nInsere o nome da tua mercenaria: ")
        if self.__terminado:
            return

        if nome == "":
            nome = "Nyx"
            print("Nao escreveste nome. O sistema atribuiu-te um codinome de servico: Nyx.")

        self.criarJogador(nome)

        while not self.__terminado:
            self.mostrarMenuPrincipal()
            opcao = self.lerInteiroEntre("Escolha: ", 1, 6)
            if self.__terminado or opcao is None:
                break

            Recursos.limparConsola()

            if opcao == 1:
                self.__jogador.mostrarEstado()
                self.esperarEnterSeguro("Premir ENTER para voltar a rua...")

            elif opcao == 2:
                self.explorarMasmorra()

            elif opcao == 3:
                self.visitarLoja()

            elif opcao == 4:
                self.visitarAfterlife()

            elif opcao == 5:
                self.descansar()

            elif opcao == 6:
                Recursos.pararAudio()
                print("\nDecidiste desaparecer da cidade.")
                self.__terminado = True

    def mostrarIntroducao(self):
        Recursos.limparConsola()
        print("\033[33m")
        Recursos.tocarAudio("assets/audio/intro.wav")
        Recursos.tocarAudioFundo("The-Rebel-Path-_Cyberpunk-2077-Soundtrack_.wav")
        Recursos.imprimirAscii(
            "assets/ascii/logo.txt",
            """
    ======================================
              CYBERPUNK_2077
    ======================================
            """
        )
        print("\033[0m")

        Recursos.pausa(1)
        print("\nNeon. Chuva. Maquinas a consumir o resto da tua sanidade.")
        Recursos.pausa(1)
        print("Es um mercenario contratado para entrar numa instalacao fortificada.")
        Recursos.pausa(1)
        print("No fundo dessa estrutura, uma IA experimental prepara-se para tomar o controlo da cidade.")
        Recursos.pausa(1)
        print("O teu trabalho e simples: infiltrar-te, sobreviver e destruir o nucleo antes que a megacorporacao te use como peca de reposicao.")
        print()
        Recursos.pausa(1)
        print("Nao ha herois aqui. So gente com implantes, dividas e ma sorte.")
        print("Bem-vindo ao abismo digital.")

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
        print("Classificacao: Mercenario de rua")
        print("Estado: com um credito e varios problemas")

    def mostrarMenuPrincipal(self):
        Recursos.limparConsola()
        print("\n===== MENU PRINCIPAL =====")
        print("Zona atual:", self.__masmorraAtual)
        print("Descansos usados:", self.__descansosUsados, "/", self.__descansosMaximos)
        print("1 - Ver perfil")
        print("2 - Explorar zona")
        print("3 - Visitar mercado negro")
        print("4 - Visitar Afterlife")
        print("5 - Procurar assistencia")
        print("6 - Sair")

    def criarMasmorraAtual(self):
        dados = self.__dadosZona(self.__masmorraAtual)
        return Masmorra(
            self.__masmorraAtual,
            dados["nome"],
            dados["descricao"],
            dados["caminhos"]
        )

    def criarInimigoDaMasmorra(self):
        dados = self.__dadosZona(self.__masmorraAtual)
        return Inimigo(*dados["inimigo"])

    def explorarMasmorra(self):
        if self.__jogador is None:
            print("Ainda nao existe uma mercenaria criada.")
            return

        masmorra = self.criarMasmorraAtual()
        self.__inimigoAtual = self.criarInimigoDaMasmorra()

        masmorra.mostrarInfo()
        print("\nAo entrares, sentes o pulso da cidade na pele.")
        print("Um alvo apareceu na tua frente!")
        print("Inimigo:", self.__inimigoAtual.getNome())

        self.iniciarCombate()

    def __contraAtacarSeNecessario(self):
        if self.__inimigoAtual is not None and self.__inimigoAtual.estaVivo():
            self.__inimigoAtual.atacar(self.__jogador)
            if not self.__jogador.estaVivo():
                self.processarDerrota()
                return True
        return False

    def iniciarCombate(self):
        if self.__jogador is None or self.__inimigoAtual is None:
            print("Nao ha combate activo.")
            return

        print("\n===== COMBATE =====")

        while not self.__terminado and self.__jogador.estaVivo() and self.__inimigoAtual.estaVivo():
            print("\n1 - Atacar")
            print("2 - Usar MaxDoc")
            print("3 - Usar consumivel")
            print("4 - Ver estado")
            print("5 - Fugir")
            opcao = self.lerInteiroEntre("Escolha: ", 1, 5)

            if self.__terminado or opcao is None:
                break

            if opcao == 1:
                self.__jogador.atacar(self.__inimigoAtual)
                if not self.__inimigoAtual.estaVivo():
                    self.processarVitoria()
                    break
                if self.__contraAtacarSeNecessario():
                    break

            elif opcao == 2:
                if self.__jogador.usarPocao():
                    if self.__inimigoAtual.estaVivo() and self.__contraAtacarSeNecessario():
                        break
                else:
                    print("Nao tens MaxDocs guardados.")
                    if self.__contraAtacarSeNecessario():
                        break

            elif opcao == 3:
                if self.__jogador.usarConsumivel(self.__inimigoAtual):
                    if not self.__inimigoAtual.estaVivo():
                        self.processarVitoria()
                        break
                    if self.__contraAtacarSeNecessario():
                        break
                else:
                    print("Nao tens consumiveis guardados.")
                    if self.__contraAtacarSeNecessario():
                        break

            elif opcao == 4:
                self.__jogador.mostrarEstado()
                self.__inimigoAtual.mostrarEstado()
                if self.__contraAtacarSeNecessario():
                    break

            elif opcao == 5:
                print("Fugiste do combate.")
                break

    def escolherProximaZona(self, caminhos):
        if not caminhos:
            return None

        print("\nCaminhos disponiveis:")
        for indice, zona in enumerate(caminhos, start=1):
            dados = self.__dadosZona(zona)
            print(f"{indice} - Zona {zona}: {dados['nome']}")

        escolha = self.lerInteiroEntre(f"Escolhe um caminho (1-{len(caminhos)}): ", 1, len(caminhos))
        if self.__terminado or escolha is None:
            return None

        return caminhos[escolha - 1]

    def processarVitoria(self):
        print("\nVitoria!")
        print(f"{self.__jogador.getNome()} derrotou {self.__inimigoAtual.getNome()}.")

        xpBase = self.__inimigoAtual.getExperiencia()
        bonusXP = self.__jogador.getTotalBonusExperienciaCompanheiros()
        xpTotal = xpBase + (xpBase * bonusXP // 100)
        if bonusXP:
            print(f"Os teus companheiros aumentam a experiencia recebida em {bonusXP}%.")

        self.__jogador.ganharExperiencia(xpTotal)
        self.__jogador.ganharMoedas(self.__inimigoAtual.getMoedas())
        self.__inimigoAtual = None

        if self.__masmorraAtual >= self.__totalZonas:
            print("Conseguiste destruir o nucleo da IA e salvar a cidade.")
            Recursos.pararAudio()
            self.__terminado = True
            return

        caminhos = self.__dadosZona(self.__masmorraAtual)["caminhos"]
        if not caminhos:
            print("Nao ha mais caminhos disponiveis.")
            self.__terminado = True
            return

        proximaZona = self.escolherProximaZona(caminhos)
        if proximaZona is not None:
            self.__masmorraAtual = proximaZona
            print(f"Seguiste para a zona {self.__masmorraAtual}.")

    def processarDerrota(self):
        print("\nDerrota!")
        print("Os teus implantes falham. A cidade nao te esquece.")
        Recursos.pararAudio()
        self.__terminado = True

    def avancarMasmorra(self):
        if self.__masmorraAtual < self.__totalZonas:
            self.__masmorraAtual += 1
            print(f"Avancaste para a zona {self.__masmorraAtual}.")
        else:
            print("Ja atingiste o ultimo ponto da rede.")

    def visitarLoja(self):
        if self.__jogador is None:
            print("Ainda nao existe uma mercenaria criada.")
            return

        self.__loja.gerarProdutos(self.__masmorraAtual)

        while not self.__terminado:
            Recursos.limparConsola()
            self.__loja.mostrarProdutos()
            if not self.__loja.getItensDisponiveis():
                self.esperarEnterSeguro("A loja ficou sem stock. Pressiona ENTER para sair...")
                return

            print("\n0 - Sair do mercado")
            escolha = self.lerInteiroEntre(
                f"Escolhe um item (0-{len(self.__loja.getItensDisponiveis())}): ",
                0,
                len(self.__loja.getItensDisponiveis())
            )

            if self.__terminado or escolha is None:
                return

            if escolha == 0:
                print("Saiste do mercado.")
                return

            self.__loja.comprarItem(self.__jogador, escolha)
            if not self.__loja.getItensDisponiveis():
                self.esperarEnterSeguro("A loja ficou sem stock. Pressiona ENTER para sair...")
                return

            self.esperarEnterSeguro("Pressiona ENTER para continuar a ver a loja...")

    def visitarAfterlife(self):
        if self.__jogador is None:
            print("Ainda nao existe uma mercenaria criada.")
            return

        while not self.__terminado:
            self.__afterlife.mostrarMercenarios(self.__jogador)
            escolha = self.lerInteiroEntre("Escolhe um mercenario (1-5): ", 1, 5)

            if self.__terminado or escolha is None:
                return

            if escolha == 5:
                print("\nSaiste do Afterlife.")
                return

            self.__afterlife.mostrarDetalhesMercenario(self.__jogador, escolha)

    def descansar(self):
        if self.__jogador is None:
            print("Ainda nao existe uma mercenaria criada.")
            return

        if self.__descansosUsados >= self.__descansosMaximos:
            print("Ja atingiste o limite de descansos.")
            return

        self.__jogador.curar(25)
        self.__descansosUsados += 1
        print(f"Descanso usado. Total: {self.__descansosUsados}/{self.__descansosMaximos}.")

    def verificarFimDoJogo(self):
        return self.__terminado or (self.__jogador is not None and not self.__jogador.estaVivo())
