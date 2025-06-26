import time
import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar_jogo():
    limpar_tela()
    print("Jogo começado!\n\n")# O "/n" faz uma quebra de linha para o próximo print ou input
    pontos = 0

    numero_base = random.randint(1, 5)
    print("Os dois números escolhidos pelo sistema foram: {} + {}".format(numero_base, numero_base))

    try:
        print("Novo desafio!")
        print("Quanto é {} + {}?".format(numero_base, numero_base))

        tentativa = input("Digite a resposta (ou 'sair' para encerrar): ")
        if tentativa.lower() == "sair":
            print("Jogo encerrado. Pontuação final: {} pontos".format(pontos))
            return

        resposta = int(tentativa)

        if resposta == numero_base + numero_base:
            pontos += 15
            print("Você acertou e ganhou 15 pontos! Total de pontos: {}\n".format(pontos))
        else:
            print("Você errou! Seu recorde foi de {} pontos.".format(pontos))
            return

        time.sleep(2)
        limpar_tela()

        # Loop infinito de desafio
        while True:
            print("Novo desafio!")
            print("Quanto é {} + {}?".format(resposta, resposta))

            tentativa = input("Digite a resposta (ou 'sair' para encerrar): ")

            if tentativa.lower() == "sair":
                print("Jogo encerrado. Pontuação final: {} pontos".format(pontos))
                break

            try:
                tentativa = int(tentativa)
                if tentativa == resposta + resposta:
                    pontos += 15
                    print("Acertou! +15 pontos! Total: {}\n".format(pontos))
                    resposta = tentativa
                    time.sleep(2)
                    limpar_tela()
                else:
                    print("Errou! A resposta certa era {}.".format(resposta + resposta))
                    print("Pontuação final: {} pontos".format(pontos))
                    break
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

    except ValueError:
        print("Entrada inválida. Jogo encerrado.")

# Início do jogo
comeco = input("Deseja começar o jogo? (sim/não): ").lower()

if comeco == "sim":
    iniciar_jogo()
elif comeco == "não":
    print("Jogo interrompido.")
else:
    print("Digite pelo menos uma opção válida!")
