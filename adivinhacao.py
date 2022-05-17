import random

def imprimir_comeco():
    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("**********************************")


def imprimir_niveis():
    print("Qual nivel de dificuldade?")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")
    nivel = int(input("Define o nível:"))


def jogar_adv():


    imprimir_comeco()

    numero_secreto = random.randrange(0, 101)
    #round(random.random() * 100) 0.0 e 1.0
    #(Comentario é feito com #)
    total_tentativas = 0
    pontos = 1000
    nivel = 3

    imprimir_niveis()


    if (nivel==1):
        total_tentativas= 20
    elif(nivel==2):
        total_tentativas= 10
    elif(nivel==3):
        total_tentativas= 5
    else:
        print("Valor invalido")


    for rodada in range(1, total_tentativas + 1):

        print("Tentativa {0} de {1}".format(rodada, total_tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou:", chute)
        numero = int(chute)

        if (numero < 1 or numero > 100):
            print("Você deve digitar um valor entre 1 e 100!")
            continue

        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos e em {} tentativas".format(pontos, rodada))
            break
        else:
            if (maior):
                print("O seu chute foi MAIOR que o número secreto")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

            elif (menor):
                print("O seu chute foi MENOR que o número secreto")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos
        print(numero_secreto)
    print("Fim do jogo!")


if(__name__ == "__main__"):
    jogar_adv()