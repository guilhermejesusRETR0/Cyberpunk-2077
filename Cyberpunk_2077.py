# ============================================================
# CYBERPUNK_2077
# Ficha Prática de Programação Orientada a Objetos em Python
#
# Tema:
# Jogo de ação e exploração em ambiente cyberpunk, com combate
# por turnos, loja, inventário, caminhos não lineares e boss final.
#
# Regras da ficha:
# - Utilizar atributos privados
# - Utilizar getters e setters tradicionais
# - Completar os métodos assinalados com TODO
#
# ESTE É O FICHEIRO QUE DEVES CORRER PARA JOGAR.
# Ele só faz uma coisa: cria um Jogo novo e manda-o iniciar.
# Toda a lógica do jogo está distribuída pelos outros ficheiros
# (Jogo.py, Jogador.py, Loja.py, etc.).
# ============================================================
from Jogo import Jogo


def main():
    jogo = Jogo()     # Cria uma nova partida (do zero)
    jogo.iniciar()     # Começa a jogar (mostra intro, menu, etc.)


if __name__ == "__main__":
    # Isto garante que main() só corre quando executamos ESTE ficheiro
    # diretamente (ex: "python Cyberpunk_2077.py"), e não quando este
    # ficheiro é importado por engano a partir de outro sítio.
    main()
