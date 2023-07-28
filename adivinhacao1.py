import random


print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

print("Qual o nível de dificuldade? ")
print("(01)- Fácil  (02)- Médio   (03)- Difícil ")

nivel = int(input("Defina um nível: "))
numero_secreto = random.randrange(1,101) 
tentativas = 0
pontos = 100

if(nivel == 1):
    tentativas = 7
elif(nivel == 2):
    tentativas = 5
else:
    tentativas = 3


for rodada in range (1, tentativas+1):
    print("Tentativa {} de {}". format(rodada, tentativas) )

    chute_str = input("Digite um número de 1 a 100: ")
    print("Você digitou", chute_str)

    chute = int(chute_str) 

    if (chute < 1 or chute > 100):
     print("Número inválido! Digite um número entre 1 e 100.")
     continue
     
    acertou = chute == numero_secreto
    errou_maior = chute > numero_secreto
    errou_menor = chute < numero_secreto

    if(acertou):
        print("Parabéns, você acertou! total de pontos: {}".format(pontos))
        break
    else:
        if(errou_maior):
            print("Que pena, você errou! O número que você digitou é maior que o número secreto")
        elif(errou_menor):
            print("Que pena, você errou! O número que você digitou é menor que o número secreto")
            pontos_perdidos = abs (numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    
print("Fim de jogo! Total de pontos: {}".format(pontos))
print("O número secreto era {}". format(numero_secreto))
