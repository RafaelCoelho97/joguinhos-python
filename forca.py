import random


def jogar():
    imprime_mensagem_de_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letra_acertada = cria_lacunas(palavra_secreta)  # para cada letra cria uma lacuna

    print(letra_acertada)

    enforcou = False
    acertou = False
    erro = 0

    # enquanto (TRUE E TRUE),enq uanto é tru ele continua funcionando
    # enquanto não acertou e não enforcou continua jogando
    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letra_acertada, palavra_secreta)

        else:
            erro += 1  # Caso erre, como tem 7 tentativas, incrementa uma, até chegar em 7 e ser enforcado
            desenha_forca(erro)

        enforcou = erro == 7
        acertou = "_" not in letra_acertada

        print(letra_acertada)

    if (acertou):
        imprime_mensagem_vencedor()

    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_de_abertura():
    print("**********************************")
    print("Bem vindo ao jogo da forca!")
    print("**********************************")
    print("")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # puxa os nomes do arquivo TXT dentro de uma variavel
    palavras = []  # Passamos para formato lista

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))  # puxa da lista de palavras, uma palavra randomicamente
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def cria_lacunas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:  # Caso acerte uma letra o index vai até a lacuna da letra
        # e incrementa a "letra" na lacuna, por exemplo Palavra Maca
        if (chute == letra):  # Chutei C o index começa com 0, no caso M, como chuteu C ele vai
            letra_acertada[index] = letra  # 0-M; 1-A; 2-C; 3-A...['_', '_', 'C', '_'], alterando a lacuna pela letra
        index += 1


def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if (erro == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erro == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erro == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erro == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erro == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erro == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erro == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



    # Exemplo para alterar o else
    # else:
    # erros=erros+1
    # print("Continue tentando, você tem {} tentativas ".format(6-erros))
    # if erros==6:
    #    enforcou=True
    #    print("Tente de novo, não foi dessa vez")
    # elif palavra_secreta == letras_acertadas:
    #    acertou=True
    #   print("Muito bem, você acertou a palavra secreta !!!")

if (__name__ == "__main__"):
    jogar()
