# 1. Faça um algoritmo para o jogo "pedra, papel e tesoura". O algoritmo deve
# receber a entrada do jogador 1 e a entrada do jogador 2. A saída deve ser uma 
# mensagem dizendo qual jogador ganhou ou uma mensagem dizendo que deu empate ou 
# uma mensagem dizendo que algum jogador colocou uma entrada incorreta.

# Obs. Pesquise sobre as regras do jogo. 
jogador1 = input("Digite sua jogada, player 1: (PEDRA, PAPEL, TESOURA) ")
player1 = jogador1.upper()

jogador2 = input("Digite sua jogada, player 2: (PEDRA, PAPEL, TESOURA) ")
player2 = jogador2.upper()

if player1 == "PEDRA" and player2 == "TESOURA":
    print("Jogador 1 venceu!")
elif player1 == "TESOURA" and player2 == "PAPEL":
    print("Jogador 1 venceu! ")
elif player1 == "PAPEL" and player2 == "PEDRA":
    print("Jogador 1 venceu!")
elif player1 == player2:
    print('EMPATE!')
elif player2 == "PEDRA" and player1 == "TESOURA":
    print("Jogador 2 venceu!")
elif player2 == "TESOURA" and player1 == "PAPEL":
    print("Jogador 2 venceu! ")
elif player2 == "PAPEL" and player1 == "PEDRA":
    print("Jogador 2 venceu!")
else: 
    print("Algum jogador fez uma jogada errada!")
