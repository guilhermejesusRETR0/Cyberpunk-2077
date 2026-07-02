import os
import time

try:
    import winsound
except ImportError:
    winsound = None


# ============================================================
# CLASSE RECURSOS
# ============================================================

class Recursos:

    @staticmethod
    def localizarAudio(caminhoFicheiro):
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

        for caminho in caminhos:
            if os.path.exists(caminho):
                return caminho

        diretorioMusica = os.path.abspath(os.path.join(baseDiretorio, "musica"))
        if os.path.isdir(diretorioMusica):
            for nome in os.listdir(diretorioMusica):
                caminho = os.path.join(diretorioMusica, nome)
                if os.path.isfile(caminho) and nome.lower().endswith((".wav", ".mp3", ".ogg", ".m4a")):
                    nomeBase = os.path.splitext(nome)[0].lower()
                    nomePedido = os.path.splitext(os.path.basename(caminhoFicheiro))[0].lower()
                    if nomeBase == nomePedido or nomeBase.replace(" ", "") == nomePedido.replace(" ", "") or "rebel" in nomeBase and "rebel" in nomePedido:
                        return caminho

        return None

    @staticmethod
    def limparConsola():
        # No PyCharm, os comandos cls/clear nem sempre limpam bem a consola.
        # Esta solução é mais simples e funciona em praticamente todos os ambientes.
        print("\n" * 100)

    @staticmethod
    def pausa(segundos):
        # Faz uma pausa na execução do programa.
        # Serve para dar mais ritmo à narrativa do jogo.
        time.sleep(segundos)

    @staticmethod
    def imprimirAscii(caminhoFicheiro, textoAlternativo=""):
        # Tenta imprimir o conteúdo de um ficheiro ASCII.
        # Se o ficheiro não existir, mostra um texto alternativo.

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
        # Tenta tocar um ficheiro de áudio .wav.
        # O winsound funciona apenas em Windows.
        # Se não for possível tocar áudio, o programa continua normalmente.

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
        # Toca um áudio e espera que ele termine antes de continuar.
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
        # Para qualquer áudio que esteja a tocar.
        # Só funciona se winsound estiver disponível.

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
        # Imprime uma linha decorativa.
        print(simbolo * tamanho)

    @staticmethod
    def imprimirTitulo(titulo):
        # Imprime um título formatado para a consola.

        Recursos.imprimirLinha()
        print(titulo.center(40))
        Recursos.imprimirLinha()

    @staticmethod
    def verificarDiretorioMusica():
        # Verifica rapidamente se existe a pasta 'musica' em locais comuns.
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


# Verificação rápida ao importar o módulo
try:
    Recursos.verificarDiretorioMusica()
except Exception:
    # Qualquer erro aqui não deve impedir o funcionamento do programa
    pass