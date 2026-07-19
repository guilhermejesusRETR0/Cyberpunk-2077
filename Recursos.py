# ============================================================
# CLASSE RECURSOS
# Uma "caixa de ferramentas" com funções auxiliares usadas em todo o
# jogo: limpar a consola, tocar áudio, mostrar arte ASCII, pausas, etc.
# Todos os métodos são "@staticmethod", ou seja, chamam-se diretamente
# como Recursos.nomeDoMetodo(...) - não é preciso criar um objeto Recursos.
#
# NOTA: "winsound" só existe no Windows. Se estiveres noutro sistema
# operativo, o try/except abaixo evita que o programa rebente - o som
# simplesmente não vai funcionar, mas o resto do jogo continua normal.
# ============================================================

import os
import time

try:
    import winsound
except ImportError:
    winsound = None


class Recursos:

    @staticmethod
    def localizarAudio(caminhoFicheiro):
        # Tenta encontrar um ficheiro de áudio em vários locais possíveis
        # (pasta do projeto, pasta "musica", pasta "assets/audio", etc.).
        # Isto existe para o jogo continuar a encontrar os sons mesmo que
        # sejam corridos de pastas diferentes (ex: PyCharm vs terminal).
        caminhos = []
        baseDiretorio = os.path.dirname(os.path.abspath(__file__))

        if os.path.exists(caminhoFicheiro):
            return caminhoFicheiro

        if os.path.isabs(caminhoFicheiro):
            caminhos.append(caminhoFicheiro)
        else:
            caminhos.append(os.path.join(baseDiretorio, caminhoFicheiro))
            caminhos.append(os.path.join(baseDiretorio, "musica", os.path.basename(caminhoFicheiro)))
            caminhos.append(os.path.join(baseDiretorio, "assets", "audio", os.path.basename(caminhoFicheiro)))
            caminhos.append(os.path.join(os.getcwd(), caminhoFicheiro))
            caminhos.append(os.path.join(os.path.dirname(os.getcwd()), caminhoFicheiro))
            caminhos.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), caminhoFicheiro))
            caminhos.append(os.path.join(os.path.dirname(os.getcwd()), "musica", os.path.basename(caminhoFicheiro)))
            caminhos.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "musica", os.path.basename(caminhoFicheiro)))

        baseSuperior = os.path.abspath(os.path.join(baseDiretorio, ".."))
        if os.path.isdir(baseSuperior):
            caminhos.append(os.path.join(baseSuperior, "musica", os.path.basename(caminhoFicheiro)))
            caminhos.append(os.path.join(baseSuperior, "musica"))

        # Testamos cada caminho possível até encontrarmos um que exista de facto.
        for caminho in caminhos:
            if os.path.exists(caminho):
                return caminho

        # Última tentativa: procurar por um nome parecido dentro da pasta "musica".
        diretorioMusica = os.path.abspath(os.path.join(baseDiretorio, "musica"))
        if os.path.isdir(diretorioMusica):
            for nome in os.listdir(diretorioMusica):
                caminho = os.path.join(diretorioMusica, nome)
                if os.path.isfile(caminho) and nome.lower().endswith((".wav", ".mp3", ".ogg", ".m4a")):
                    nomeBase = os.path.splitext(nome)[0].lower()
                    nomePedido = os.path.splitext(os.path.basename(caminhoFicheiro))[0].lower()
                    if nomeBase == nomePedido or nomeBase.replace(" ", "") == nomePedido.replace(" ", "") or "rebel" in nomeBase and "rebel" in nomePedido:
                        return caminho

        # Se não encontrámos nada, devolvemos None (o som simplesmente não toca).
        return None

    @staticmethod
    def limparConsola():
        # No PyCharm, os comandos cls/clear nem sempre limpam bem a consola.
        # Esta solução é mais simples e funciona em praticamente todos os ambientes:
        # imprime 100 linhas em branco, "empurrando" o texto antigo para fora do ecrã.
        print("\n" * 100)

    @staticmethod
    def pausa(segundos):
        # Faz uma pausa na execução do programa.
        # Serve para dar mais ritmo à narrativa do jogo (ex: entre frases da intro).
        time.sleep(segundos)

    @staticmethod
    def imprimirAscii(caminhoFicheiro, textoAlternativo=""):
        # Tenta imprimir o conteúdo de um ficheiro de arte ASCII (.txt).
        # Se o ficheiro não existir (ou não conseguir ser lido por algum
        # motivo), mostra o "textoAlternativo" em vez de dar erro.
        if os.path.exists(caminhoFicheiro):
            try:
                with open(caminhoFicheiro, "r", encoding="utf-8") as ficheiro:
                    conteudo = ficheiro.read()
                    print(conteudo)
            except Exception:
                print(textoAlternativo)
        else:
            print(textoAlternativo)

    @staticmethod
    def tocarAudio(caminhoFicheiro):
        # Tenta tocar um ficheiro de áudio .wav uma única vez, sem bloquear
        # o resto do programa (SND_ASYNC). Só funciona no Windows.
        if winsound is None:
            return

        caminho = Recursos.localizarAudio(caminhoFicheiro)
        if caminho is not None:
            try:
                winsound.PlaySound(
                    caminho,
                    winsound.SND_FILENAME | winsound.SND_ASYNC
                )
            except Exception:
                pass

    @staticmethod
    def tocarAudioFundo(caminhoFicheiro):
        # Igual a tocarAudio(), mas com SND_LOOP: o som repete-se em loop
        # (ideal para música de fundo que toca enquanto o jogador explora).
        if winsound is None:
            return

        caminho = Recursos.localizarAudio(caminhoFicheiro)
        if caminho is not None:
            try:
                winsound.PlaySound(
                    caminho,
                    winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
                )
            except Exception:
                pass

    @staticmethod
    def tocarAudioBloqueante(caminhoFicheiro):
        # Toca um áudio e ESPERA que ele termine antes de continuar o
        # programa (ao contrário de tocarAudio/tocarAudioFundo).
        # Pode ser útil para sons curtos, como vitória ou derrota.
        if winsound is None:
            return

        if os.path.exists(caminhoFicheiro):
            try:
                winsound.PlaySound(
                    caminhoFicheiro,
                    winsound.SND_FILENAME
                )
            except Exception:
                pass

    @staticmethod
    def pararAudio():
        # Para qualquer áudio que esteja a tocar neste momento.
        # Só funciona se winsound estiver disponível (Windows).
        if winsound is not None:
            try:
                winsound.PlaySound(None, 0)
            except Exception:
                pass

    @staticmethod
    def esperarEnter(mensagem="Pressiona ENTER para continuar..."):
        # Pausa o jogo até o utilizador carregar em ENTER.
        input("\n" + mensagem)

    @staticmethod
    def imprimirLinha(tamanho=40, simbolo="="):
        # Imprime uma linha decorativa feita de um símbolo repetido
        # (ex: "========================================").
        print(simbolo * tamanho)

    @staticmethod
    def imprimirTitulo(titulo):
        # Imprime um título formatado, centrado entre duas linhas decorativas.
        # Usado, por exemplo, no cabeçalho do Afterlife.
        Recursos.imprimirLinha()
        print(titulo.center(40))
        Recursos.imprimirLinha()

    @staticmethod
    def verificarDiretorioMusica():
        # Verifica rapidamente se existe a pasta 'musica' em locais comuns.
        # Corre automaticamente ao importar este ficheiro (ver o fim do
        # ficheiro) só para dar uma pista, no arranque, se a pasta foi
        # encontrada ou não - não afeta o funcionamento do jogo.
        possiveis = [
            os.path.join(os.getcwd(), "musica"),
            os.path.join(os.path.dirname(os.getcwd()), "musica"),
            os.path.abspath(os.path.join(os.getcwd(), "..", "musica"))
        ]
        for p in possiveis:
            if os.path.isdir(p):
                print(f"Diretório 'musica' encontrado: {p}")
                return p
        print("Diretório 'musica' não encontrado.")
        return None


# Verificação rápida ao importar o módulo.
# Isto corre automaticamente sempre que qualquer ficheiro do jogo faz
# "from Recursos import Recursos" - é só um aviso informativo na consola.
try:
    Recursos.verificarDiretorioMusica()
except Exception:
    # Qualquer erro aqui não deve impedir o funcionamento do programa.
    pass
