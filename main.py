import random
import time
import os

answer = 'sim'
hits = 0
wrong = 0
def logo():
    print(r'''     
      _  ___   ____  ___    ____    _      __  __ _____ __  __  ___  ____  ___    _    
     | |/ _ \ / ___|/ _ \  |  _ \  / \    |  \/  | ____|  \/  |/ _ \|  _ \|_ _|  / \   
  _  | | | | | |  _| | | | | | | |/ _ \   | |\/| |  _| | |\/| | | | | |_) || |  / _ \  
 | |_| | |_| | |_| | |_| | | |_| / ___ \  | |  | | |___| |  | | |_| |  _ < | | / ___ \ 
  \___/ \___/ \____|\___/  |____/_/   \_\ |_|  |_|_____|_|  |_|\___/|_| \_\___/_/   \_\
      ''')
    
while answer == 'sim' or answer == 's':
    logo()
    print('preste atenção aos números...')
    list1 = []
    list2 = []
    for i in range(4):
         number = random.randint(1,20)
         print(str(number).center(50), end='\r')
         list1.append(number)
         time.sleep(1) 
    print(' - ' * 20)

    print('digite os números na ordem inversa!')
    try: 
        for c in range(4,0,-1):
            list2.append(int( input(f'{c}º número: ')))
            
        list2.reverse()
        if list1 == list2:
            print('\nParabéns, você acertou')
            hits +=1
        else:
            print('\nVocê errou ahhh')
            wrong += 1
            
    except ValueError:
        print('\nX digite apenas números inteiros X')
        time.sleep(1)

    answer = input('\nQuer continuar jogando? ')
    os.system('cls')

logo()
print(f'Você acertou {hits} e errou {wrong}!')
