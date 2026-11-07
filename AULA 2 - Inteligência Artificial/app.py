#biblioteca para aleatoriedade

import random

print('JOGO DA ALEATOREDADE...')
print('GANHE ATÉ R$5k')
print('Escolha um número de 1 a 20')

numero_maquina = random.randint(1,20)
chances = 3

for x in range(3):    
    print('Voce tem', chances, 'chances')
    numero_usuario = int(input('Escolha o seu número>>'))
    chances = chances - 1
    if numero_maquina == numero_usuario:        
       print('VOCE GANHOU 5K!!')
    else:
       print('VOCE ERROU FEIO!!!')  
       if chances == 0:
          print('A maquina escolheu', numero_maquina)  

