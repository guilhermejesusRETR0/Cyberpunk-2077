# ============================================================
# CLASSE JOGO
# É o "maestro" de tudo: guarda o estado geral da partida (jogador,
# zona atual, loja, etc.) e controla o menu principal, o combate,
# a loja, o Afterlife e a progressão entre zonas.
#
# ESTRUTURA GERAL DO JOGO:
#   - Cada "zona" (masmorra) tem um número (1 a 5), um nome, uma
#     descrição, os caminhos para onde se pode avançar, e o inimigo
#     que aparece lá. Tudo isto está guardado em __dadosMasmorras.
#   - iniciar() é o ponto de entrada: mostra a intro, cria o jogador,
#     e depois fica num ciclo a mostrar o menu principal até o
#     jogador sair ou morrer (verificarFimJogo()).
#
# ONDE ALTERAR COISAS COMUNS:
#   - Para mudar zonas/inimigos: ver __dadosMasmorras no __init__.
#   - Para mudar o texto da intro: ver mostrarIntroducao().
#   - Para mudar os atributos iniciais do jogador: ver criarJogador().
#   - Para mudar as opções do menu: ver mostrarMenuPrincipal() e iniciar().
# ============================================================

from Inimigo import Inimigo
from Jogador import Jogador
from Loja import Loja
from Masmorra import Masmorra
from Recursos import Recursos
from Afterlife import Afterlife


class Jogo:
    def __init__(self):
        self.__jogador = None            # Ainda não existe jogador até iniciar() correr
        self.__masmorraAtual = 1         # O jogo comeca sempre na zona 1
        self.__inimigoAtual = None       # Nenhum inimigo em combate no inicio
        self.__loja = Loja()
        self.__afterlife = Afterlife()
        self.__terminado = False         # Fica True quando o jogo deve parar
        self.__totalMasmorras = 5        # Numero total de zonas no jogo
        self.__descansosUsados = 0
        self.__descansosMaximos = self.calcularDescansosMaximos()

        # Dados brutos de configuracao de cada zona: nome, descricao,
        # para onde se pode avancar ("caminhos") e os dados do inimigo
        # que aparece nessa zona (nome, vida, ataque, defesa, exp, moedas).
        #
        # PARA ADICIONAR/ALTERAR UMA ZONA: basta editar/acrescentar uma
        # entrada neste dicionario. Não é preciso tocar em mais nada.
        self.__dadosMasmorras = {
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

        # Objetos Masmorra propriamente ditos, construidos a partir dos
        # dados brutos acima (ver criarMasmorras()).
        self.__masmorras = {}
        self.criarMasmorras()

    # ---------- GETTERS ----------

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

    def getMasmorras(self):
        return dict(self.__masmorras)

    def getTotalMasmorras(self):
        return self.__totalMasmorras

    # ---------- SETTERS ----------

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

    # ---------- LEITURA DE INPUT (funções auxiliares) ----------
    # Estas três funções existem para ler o que o jogador escreve na
    # consola de forma "segura" - ou seja, sem o programa rebentar se
    # o jogador escrever algo inesperado ou fechar o programa a meio.

    def lerOpcao(self, mensagem):
        # Lê uma linha de texto simples do jogador (sem validação de tipo).
        # Se o jogador fechar o programa (Ctrl+C ou EOF), terminamos o jogo
        # em vez de deixar o programa rebentar com um erro feio.
        try:
            return input(mensagem).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nA ligacao com a rede caiu. O ciclo termina aqui.")
            self.__terminado = True
            return ""

    def lerInteiroEntre(self, mensagem, minimo, maximo):
        # Lê um número inteiro do jogador, repetindo a pergunta enquanto
        # a resposta não for um número válido dentro do intervalo pedido.
        # Isto evita que o jogo rebente se o jogador escrever texto em
        # vez de um número (ex: escrever "abc" numa pergunta que espera 1-5).
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
        # Pausa a execução até o jogador pressionar ENTER.
        # Usa-se em vez de Recursos.esperarEnter() quando também queremos
        # proteção contra o jogador fechar o programa a meio (Ctrl+C).
        try:
            input("\n" + mensagem)
        except (EOFError, KeyboardInterrupt):
            pass

    # ---------- CRIAÇÃO E CONSULTA DE MASMORRAS ----------

    def criarMasmorras(self):
        # Constrói os objetos Masmorra (ver Masmorra.py) a partir dos
        # dados brutos definidos em __dadosMasmorras.
        self.__masmorras = {}
        for numero, dados in self.__dadosMasmorras.items():
            self.__masmorras[numero] = Masmorra(numero, dados["nome"], dados["descricao"], dados["caminhos"])
        return self.__masmorras

    def procurarMasmorraPorNumero(self, numero):
        # Devolve o objeto Masmorra correspondente a este número.
        # Se o número não existir (situação anormal), devolve a última
        # zona como "rede de segurança" para o jogo nunca rebentar.
        return self.__masmorras.get(numero, self.__masmorras[self.__totalMasmorras])

    def calcularDescansosMaximos(self):
        # Fórmula do jogo: o número de descansos permitidos é o total
        # de zonas a dividir por 3 (divisão inteira).
        return self.__totalMasmorras // 3

    # ---------- CICLO PRINCIPAL DO JOGO ----------

    def iniciar(self):
        # Ponto de entrada do jogo: mostra a intro, pede o nome do
        # jogador, cria a personagem, e entra no ciclo do menu principal.
        self.mostrarIntroducao()

        nome = self.lerOpcao("\nInsere o nome da tua mercenaria: ")
        if self.__terminado:
            return

        if nome == "":
            nome = "Nyx"
            print("Nao escreveste nome. O sistema atribuiu-te um codinome de servico: Nyx.")

        self.criarJogador(nome)

        # Ciclo principal: repete o menu até o jogo terminar
        # (jogador saiu, morreu, ou venceu o jogo).
        while not self.verificarFimJogo():
            self.mostrarMenuPrincipal()
            opcao = self.lerInteiroEntre("Escolha: ", 1, 8)
            if self.verificarFimJogo() or opcao is None:
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
                self.mostrarInventario()

            elif opcao == 5:
                self.descansarJogador()

            elif opcao == 6:
                self.mostrarCaminhosDisponiveis()

            elif opcao == 7:
                self.visitarAfterlife()

            elif opcao == 8:
                Recursos.pararAudio()
                print("\nDecidiste desaparecer da cidade.")
                self.__terminado = True

    def mostrarIntroducao(self):
        # Mostra o ecrã de abertura do jogo: logo ASCII, som e texto
        # narrativo. Se quiseres alterar a história de abertura, é
        # aqui que deves editar os textos dos vários print().
        Recursos.limparConsola()
        print("\033[33m")  # Código ANSI: muda a cor do texto para amarelo
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
        print("\033[0m")  # Código ANSI: volta à cor normal do texto

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
        # Cria a personagem do jogador com os valores iniciais do jogo.
        # PARA ALTERAR OS VALORES INICIAIS (vida, ataque, moedas, etc.),
        # basta mudar os números aqui.
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
        # Mostra o menu principal. Se quiseres adicionar/remover uma
        # opção, tens de fazer 3 coisas em conjunto:
        #   1. Adicionar/remover o "print" correspondente aqui.
        #   2. Ajustar o intervalo em "self.lerInteiroEntre('Escolha: ', 1, 8)"
        #      dentro de iniciar(), se mudares o número total de opções.
        #   3. Adicionar/remover o "elif opcao == N:" dentro de iniciar().
        Recursos.limparConsola()
        print("\n===== MENU PRINCIPAL =====")
        print("Zona atual:", self.__masmorraAtual)
        print("Descansos usados:", self.__descansosUsados, "/", self.__descansosMaximos)
        print("1 - Ver estado")
        print("2 - Explorar masmorra")
        print("3 - Visitar loja")
        print("4 - Ver inventario")
        print("5 - Descansar")
        print("6 - Ver caminhos disponiveis")
        print("7 - Visitar Afterlife")
        print("8 - Sair")

    # ---------- EXPLORAÇÃO E COMBATE ----------

    def criarInimigoAtual(self):
        # Cria um novo Inimigo com base nos dados guardados para a zona atual.
        dados = self.__dadosMasmorras.get(self.__masmorraAtual, self.__dadosMasmorras[self.__totalMasmorras])
        return Inimigo(*dados["inimigo"])

    def explorarMasmorra(self):
        # Mostra a informação da zona atual e coloca o jogador em combate
        # contra o inimigo dessa zona.
        if self.__jogador is None:
            print("Ainda nao existe uma mercenaria criada.")
            return

        masmorra = self.procurarMasmorraPorNumero(self.__masmorraAtual)
        self.__inimigoAtual = self.criarInimigoAtual()

        masmorra.mostrarInformacao()
        masmorra.mostrarCaminhosDisponiveis()
        print("\nAo entrares, sentes o pulso da cidade na pele.")
        print("Um alvo apareceu na tua frente!")
        print("Inimigo:", self.__inimigoAtual.getNome())

        self.iniciarCombate()

    def __contraAtacarSeNecessario(self):
        # Função auxiliar interna: faz o inimigo atacar de volta, DEPOIS
        # da ação do jogador, se o inimigo ainda estiver vivo.
        # Se esse contra-ataque matar o jogador, chama processarDerrota()
        # e devolve True (sinal para o combate parar imediatamente).
        if self.__inimigoAtual is not None and self.__inimigoAtual.estaVivo():
            self.__inimigoAtual.atacar(self.__jogador)
            if not self.__jogador.estaVivo():
                self.processarDerrota()
                return True
        return False

    def iniciarCombate(self):
        # O ciclo de combate: mostra as opções, executa a ação escolhida,
        # e, se necessário, faz o inimigo contra-atacar. Repete até o
        # jogador ou o inimigo morrer, ou o jogador fugir.
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
                # Atacar: o jogador dá dano ao inimigo. Se o inimigo
                # morrer com este ataque, processamos a vitória e
                # terminamos o combate (o inimigo já não pode contra-atacar).
                self.__jogador.atacar(self.__inimigoAtual)
                if not self.__inimigoAtual.estaVivo():
                    self.processarVitoria()
                    break
                if self.__contraAtacarSeNecessario():
                    break

            elif opcao == 2:
                # Usar MaxDoc (poção): cura o jogador. Note-se que usar
                # uma poção NÃO impede o inimigo de atacar a seguir.
                if self.__jogador.usarPocao():
                    if self.__inimigoAtual.estaVivo() and self.__contraAtacarSeNecessario():
                        break
                else:
                    print("Nao tens MaxDocs guardados.")
                    if self.__contraAtacarSeNecessario():
                        break

            elif opcao == 3:
                # Usar consumível de combate: causa dano ao inimigo
                # (dano aleatório, ver ConsumivelCombate.gerarDano()).
                if self.__jogador.usarConsumivelCombate(self.__inimigoAtual):
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
                # Ver estado: apenas mostra informação, mas ainda "gasta"
                # o turno (o inimigo ataca a seguir).
                self.__jogador.mostrarEstado()
                self.__inimigoAtual.mostrarEstado()
                if self.__contraAtacarSeNecessario():
                    break

            elif opcao == 5:
                # Fugir: termina o combate imediatamente, sem recompensa
                # e sem o inimigo atacar.
                print("Fugiste do combate.")
                break

    # ---------- CAMINHOS E PROGRESSÃO ----------

    def mostrarCaminhosDisponiveis(self):
        # Mostra, fora de combate, para que zonas o jogador pode seguir
        # a partir da zona atual (opção 6 do menu principal).
        masmorra = self.procurarMasmorraPorNumero(self.__masmorraAtual)
        print("\n===== CAMINHOS DISPONIVEIS =====")
        masmorra.mostrarCaminhosDisponiveis()
        for numero in masmorra.getCaminhosDisponiveis():
            print(f"  Zona {numero}: {self.procurarMasmorraPorNumero(numero).getNome()}")
        self.esperarEnterSeguro("Premir ENTER para voltar a rua...")

    def escolherProximaMasmorra(self, caminhos):
        # Pede ao jogador para escolher, entre a lista de caminhos
        # possíveis, para onde quer avançar depois de vencer um combate.
        # Devolve o número da zona escolhida (ou None se cancelado).
        if not caminhos:
            return None

        print("\nCaminhos disponiveis:")
        for indice, zona in enumerate(caminhos, start=1):
            print(f"{indice} - Zona {zona}: {self.procurarMasmorraPorNumero(zona).getNome()}")

        escolha = self.lerInteiroEntre(f"Escolhe um caminho (1-{len(caminhos)}): ", 1, len(caminhos))
        if self.__terminado or escolha is None:
            return None

        return caminhos[escolha - 1]

    def processarVitoria(self):
        # Chamado quando o jogador vence um combate.
        # Dá experiência (com bónus de companheiros, se houver) e moedas,
        # e depois decide o que acontece a seguir: fim do jogo (se esta
        # era a última zona) ou escolha da próxima zona.
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

        # Se esta era a última zona (o "boss final"), o jogo termina em vitória.
        if self.__masmorraAtual >= self.__totalMasmorras:
            print("Conseguiste destruir o nucleo da IA e salvar a cidade.")
            Recursos.pararAudio()
            self.__terminado = True
            return

        caminhos = self.procurarMasmorraPorNumero(self.__masmorraAtual).getCaminhosDisponiveis()
        if not caminhos:
            print("Nao ha mais caminhos disponiveis.")
            self.__terminado = True
            return

        proximaZona = self.escolherProximaMasmorra(caminhos)
        if proximaZona is not None:
            self.avancarParaMasmorra(proximaZona)

    def processarDerrota(self):
        # Chamado quando a vida do jogador chega a 0. Termina o jogo.
        print("\nDerrota!")
        print("Os teus implantes falham. A cidade nao te esquece.")
        Recursos.pararAudio()
        self.__terminado = True

    def avancarParaMasmorra(self, numero):
        # Move o jogador para a zona indicada (se ela existir).
        if numero in self.__masmorras:
            self.__masmorraAtual = numero
            print(f"Seguiste para a zona {self.__masmorraAtual}.")
        else:
            print("Essa zona nao existe.")

    # ---------- INVENTÁRIO, LOJA E AFTERLIFE ----------

    def mostrarInventario(self):
        # Mostra as poções e consumíveis guardados pelo jogador
        # (opção 4 do menu principal).
        print("\n===== INVENTARIO =====")
        self.__jogador.mostrarPocoes()
        self.__jogador.mostrarConsumiveisCombate()
        print("Total:", self.__jogador.consultarTotalItensInventario(), "/", self.__jogador.getLimiteInventario())
        self.esperarEnterSeguro("Premir ENTER para voltar a rua...")

    def visitarLoja(self):
        # Gera os produtos da loja para a zona atual e deixa o jogador
        # comprar itens num ciclo, até escolher saír ou a loja ficar
        # sem stock.
        if self.__jogador is None:
            print("Ainda nao existe uma mercenaria criada.")
            return

        self.__loja.gerarProdutos(self.__masmorraAtual)

        while not self.__terminado:
            Recursos.limparConsola()
            self.__loja.mostrarLoja()
            if not self.__loja.getItensVisiveis():
                self.esperarEnterSeguro("A loja ficou sem stock. Pressiona ENTER para sair...")
                return

            print("\n0 - Sair do mercado")
            escolha = self.lerInteiroEntre(
                f"Escolhe um item (0-{len(self.__loja.getItensVisiveis())}): ",
                0,
                len(self.__loja.getItensVisiveis())
            )

            if self.__terminado or escolha is None:
                return

            if escolha == 0:
                print("Saiste do mercado.")
                return

            self.__loja.venderItem(self.__jogador, escolha)
            if not self.__loja.getItensVisiveis():
                self.esperarEnterSeguro("A loja ficou sem stock. Pressiona ENTER para sair...")
                return

            self.esperarEnterSeguro("Pressiona ENTER para continuar a ver a loja...")

    def visitarAfterlife(self):
        # Mostra o menu do Afterlife (recrutamento de mercenários),
        # num ciclo, até o jogador escolher voltar para a rua.
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

    # ---------- DESCANSO E FIM DE JOGO ----------

    def descansarJogador(self):
        # Recupera 25 pontos de vida ao jogador, se ainda houver
        # descansos disponíveis (ver calcularDescansosMaximos()).
        if self.__jogador is None:
            print("Ainda nao existe uma mercenaria criada.")
            return

        if self.__descansosUsados >= self.__descansosMaximos:
            print("Ja atingiste o limite de descansos.")
            return

        self.__jogador.recuperarVida(25)
        self.__descansosUsados += 1
        print(f"Descanso usado. Total: {self.__descansosUsados}/{self.__descansosMaximos}.")

    def verificarFimJogo(self):
        # Devolve True se o jogo deve parar: ou porque foi marcado
        # como terminado (__terminado), ou porque o jogador morreu.
        # É esta função que controla o ciclo principal em iniciar().
        return self.__terminado or (self.__jogador is not None and not self.__jogador.estaVivo())
