
print("Seja bem vindo ao Quiz!!!")
resposta = input (" 1-  Para sim / 2- Para não ")
pontos = 0
vidas = 0

if (resposta == '2'):
    print ("Você saiu do jogo!:(")
    quit()
elif (resposta != '1'):
    print ("Opção inválida!")
    quit()

#print("Defina o nível que quer jogar:\n 1- Fácil \n2- Médio\n 3- Difícil ")
#nivel = input ("Resposta: ")
#if (nivel == 1):
    vidas = 4
#elif ( nivel == 2):
    vidas = 3
#elif (nivel == 3):
    vidas = 2
#FAZER COM QUE AS RESPOSTAS PAREM DE SER GERADAS QUANDO AS VIDAS ACABAREM



print ("Começando o quiz...")

print ("De quem é a famosa frase “Penso, logo existo”? \n A) Platão \n B) Galileu Galilei \n C) Descartes\n D) Sócrates")
resposta1 = input("Resposta: ")
up_resposta1 = resposta1.upper()

if( up_resposta1 != 'C'): 
    print ("Você errou! A resposta era C - Descartes. :(")
elif (up_resposta1 == 'C'):
    print ("Parbéns, você acertou! +10 pontos :)")
    pontos = pontos + 10

print ("Próxima pergunta...\n")
print ("De onde é a invenção do chuveiro elétrico? \n A) França \nB) Inglaterra \nC) Brasil \nD) Austrália")
resposta2 = input("Resposta: ")
resposta2_up = resposta2.upper()

if( resposta2_up != 'B'):
    print ("Que pena, você errou!:( A resposta era B - Brasil")
elif (resposta2_up == 'B'):
    print ( "Uhull, você acertou!! +10 pontos:)")
    pontos = pontos + 10

print("Próxima pergunta...\n")

print ("Quantas casas decimais tem o número pi? \n A) Duas \n B) Centenas \n C) Infinitas \nD) Vinte")
resposta3 = input("Resposta: ")
resposta3_up = resposta3.upper()

if (resposta3_up != 'C'):
    print ("Poxa, resposta errada!A resposta era C - Infinitas")
elif (resposta3_up == 'C'):
    print ("Resposta correta, mandou bem!! +10 pontos:)")
    pontos = pontos + 10

print("Próxima pergunta...\n")

print ("Qual o número mínimo de jogadores em cada time numa partida de futebol? \n A) 8 \n B) 10 \n C) 9 \n D) 7")
resposta4 = input("Resposta: ")
resposta4_up = resposta4.upper()

if (resposta4_up != 'D'):
    print ("Poxa, resposta errada!A resposta era D - 7")
elif (resposta4_up == 'D'):
    print ("Acertou a resposta, Boa!! +10 pontos:)")
    pontos = pontos + 10

print("Próxima pergunta...\n")

print ("Quem pintou 'Guernica'? \n A) Paul Cézanne \n B) Pablo Picasso \n C) Diego Rivera \n D) Tarsila do Amaral")
resposta5 = input("Resposta: ")
resposta5_up = resposta5.upper()

if (resposta5_up != 'B'):
    print ("Você errou! A resposta era B - Pablo Picasso")
elif (resposta5_up == 'B'):
    print ("Parabéns, certa resposta!! +10 pontos:)\n")
    pontos = pontos + 10

print("Você aceita uma rodada Bônus? \nObs: Se você errar perde tudo, mas se acertar multplica seus pontos por 100\n 1- Para aceitar | 2-Para recusar")
bonus = input("Resposta: ")
if(bonus != '1'):
    print("Tudo bem! Aqui está a sua pontuação \n Pontuação final: {}".format(pontos))
else:
    print("\n***Pergunta bônus*** \n")
    print ("Minsk é capital de qual país? \nA) Irlanda \nB) Bielorrúsia\nC) Marrocos\nD)Groenlândia")
    resp_bonus = input ("Resposta: ")
    resp_bonus2 = resp_bonus.upper()
    if(resp_bonus2 != 'B'):
        pontos = 0
        print ("\nQue pena, você errou!\n Pontuação final: {}".format(pontos))
    else:
        pontos = pontos * 100
        print("\nPARABÉNS, VOCÊ ACERTOU!!!\n Pontuação final: {}".format(pontos))



