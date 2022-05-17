import forca
import adivinhacao


def imprime_mensagem_de_abertura():
    print("**********************************")
    print("##### ESCOLHA SEU JOGO ###########")
    print("**********************************")

    print("1 - Forca")
    print("2 - Adivinhação")


def choose(jogo):
    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()

    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar_adv()



def escolhe_jogo():


    imprime_mensagem_de_abertura()

    jogo= int(input("Qual Jogo:"))

    choose(jogo)


if(__name__ == "__main__"):
    escolhe_jogo()

