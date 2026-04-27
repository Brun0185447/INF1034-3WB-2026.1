import random

def jogar():
    lista_palavras = ["PYTHON", "DESENVOLVIMENTO", "COMPUTADOR", "ALGORITMO"]
    lista_palavras[0]
    palavra_secreta = random.choice(lista_palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcado = False
    acertou = False
    erros = 0
    
    print("Bem-vindo ao jogo da Forca!")
    print(letras_acertadas)

    while(not enforcado and not acertou):
        chute = input("Qual letra? ").strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

        enforcado = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

if(__name__ == "__main__"):
    jogar()