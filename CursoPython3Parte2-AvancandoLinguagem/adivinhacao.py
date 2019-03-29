import random


def jogar():
    imprime_titulo()

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 100

    nivel = carrega_nivel_dificuldade()

    total_de_tentativas = inicializa_total_de_tentativas(nivel)


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi MAIOR do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi MENOR do que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Você fez {} pontos!".format(pontos))
    print("Fim do jogo!!!!!!")


def imprime_titulo():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def carrega_nivel_dificuldade():
    print("Qual o nível de dificuldade ?")
    print("(1)Fácil (2)Médio (3)Difícil")
    return int(input("Define o nível: "))


def inicializa_total_de_tentativas(nivel):
    if (nivel == 1):
        return 20
    elif (nivel == 2):
        return 10
    elif (nivel == 3):
        return 5


if (__name__ == "__main__"):
    jogar()
