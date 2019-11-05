import os
import time

print("###############################")
print("##### JOGO DA ADIVINHAÇÃO #####")
print("###############################\n")

#menu das opções
opçao = 0

while opçao != 2:
    print("MENU DE OPÇÕES")
    print(''' 
    [ 1 ] Iniciar o jogo
    [ 2 ] Sair do jogo
    ''')

    opçao = int(input("Escolha uma opção: "))
    os.system("cls")
    if opçao == 1:
        #variaveis 
        numero_secreto = 42 
        total_de_tentativas = 3
        rodada = 1
#jogo
        print("Jogo sendo iniciado ........")
        while(total_de_tentativas > 0):
            
            time.sleep(2)
            os.system("cls")

            print('tentativas {} de {}.'.format(rodada, total_de_tentativas))
            chute = int(input("Digite um numero: "))

            print("Você digitou: ", chute)
            time.sleep(2)
            os.system("cls")
             
            if(numero_secreto == chute):
                print('''Você acertou!
                Fim de jogo''')
                break
            elif(chute > numero_secreto):
                print("Você errou!, O seu chute foi maior que o numero secreto")
                
            elif(chute < numero_secreto):
                print("Você errou!, O seu chute foi menor que o numero secreto")
                
    
                total_de_tentativas = total_de_tentativas - 1
                print("você tem {} tentativas".format(total_de_tentativas))

                if(total_de_tentativas == 0):
                    print("Fim de jogo!!")
                    break
#opçao de finalizao do jogo 
    elif opçao == 2:
        print("\nJogo sendo finalizado!!")
        break
    else:
        print("Opção invalida")



