import forca
import adivinhacao

def escolhe_jogo():
    print("----------------------------------")
    print("Meu primeiro programa P Y T H O N ")
    print("**********************************")
    print("********  Escolha o jogo  ********")
    print("**********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o Jogo escolhido ? "))

    if (jogo == 1):
        print("Jogo da Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar()

if __name__ == ("__main__"):
    escolhe_jogo()