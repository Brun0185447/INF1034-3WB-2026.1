import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    
    usuario = input("Escolha (pedra, papel, tesoura): ").lower()
    
    computador = random.choice(opcoes)
    print(f"Computador escolheu: {computador}")

    
    if usuario == computador:
        return "Empate!"
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
         (usuario == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

print(jogar())