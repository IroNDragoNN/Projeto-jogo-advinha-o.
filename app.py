# Este é o meu primeiro projeto.
# Jogo de advinhação.

import os
from random import randint
from time import sleep
# Computador pensar...
computador = randint(0, 10)
#
print('Pensei em um número de 0 a 10. Quero ve-lo advinhar...\n')
sleep(2)

#
palpites = 0
vitorias = 0

while True:
    try:
        jogador = int(input('Digite um número entre 0 e 10 para tentar a sorte contra o computador: '))
        if jogador == computador:
            computador = randint(0, 10)
            print('Parabéns, você é um oponente formidável.')
            palpites += 1        
            vitorias += 1
            resposta = str(input('Gostaria de continuar tentando ?'))
            if resposta in 'NAOnao':
                break
        elif jogador < computador:
            print('Você errou! Tente um número maior, talvez acerte numa próxima, hehehe.')
            palpites += 1
        elif jogador > computador:
            print('Você errou! Tente um número menor, talvez acerte numa próxima, hehehe.')
            palpites += 1
        elif jogador > 10:
            print('Número inválido! Tente números entre 0 e 10.')
        else:
            print('Jogada inválida. Digite apenas números e que estejam entre 0 e 10')
    except ValueError as erro:
        os.system('cls')
        print('\n================================================')
        print('Você tentou inserir algo diferente de números...')
        print('Digite apenas números e que estejam entre 0 e 10.')        
        print('================================================\n')
        sleep(3)
        

print('\n================================================')
print(f'Foi um prazer jogar com você.')
print(f'Ao final, finalizou com {palpites} palpites e {vitorias} vitórias.')
print('================================================')
print('PROGRAMA FINALIZADO COM SUCESSO !\n3')