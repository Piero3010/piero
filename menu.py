from exercicio01 import dobro
from exercicio01 import triplo
from exercicio02 import reajuste
from exercicio03 import parImpar
from exercicio03 import positivoNegativo
from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import exercicio06
from exercicio07 import impares
from exercicio08 import somar10Inteiros
from exercicio09 import somarNumero
from exercicio10 import calcularMedia
from exercicio11 import maiorMenor
from exercicio12 import positivoNegativo
from exercicio13 import fatorial
from exercicio14 import mediaVolei
from exercicio15 import miss
from exercicio16 import eleicao
#from exercicio17 import
#from exercicio18 import
#from exercicio19 import
from exercicio20 import vetoresPares
from exercicio20 import vetoresImpares
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
def mostrarMenu():
    print('\n\n\nEscolha uma das opções abaixo: '+
          '\n0. SAIR'         +
          '\n1. Exercício 01' +
          '\n2. Exercício 02' +
          '\n3. Exercício 03' +
          '\n4. Exercício 04' +
          '\n5. Exercício 05' +
          '\n6. Exercício 06' +
          '\n7. Exercício 07' +
          '\n8. Exercício 08' +
          '\n9. Exercício 09' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n12. Exercício 12' +
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20' +
          '\n21. Preencher Vetor' +
          '\n22. Consultar Vetor' +
          '\n23. Apagar posição Vetor')

def operacao():
    opcao = 1 #Instanciar = Dar um valor inicial
    while(opcao != 0):
        mostrarMenu()
        #Coletar a opção do usuário
        opcao = int(input('Digita aqui o número da opção escolhida: '))

        #Executo a ação
        if(opcao == 0):
            #Instruções do exercício 01
            print('Obrigado!')
        elif(opcao == 1):
            #Exercício01
            print('\nExercício01')
            print(dobro())
            print(triplo())
        elif(opcao == 2):
            #Exercício02
            print('\nExercício02')
            num = int(input('Informe o salario: '))
            print(reajuste(salario))
        elif(opcao == 3):
            #Exercício03
            print('\nExercício03')
            print(parImpar(num))
            num = int(input('Informe um número: '))
            print(positivoNegativo(num))
            num = int(input('Informe um número: '))
        elif(opcao == 4):
            #Exercício 04
            print('\nExercício04')
            print(somarInteiro())
        elif(opcao == 5):
            #Exercício05
            print('\nExercício05')
            num = int(input('Informe um número: '))
            n = coletarPositivo()
            tabuada(num, n)
        elif(opcao == 6):
            #Exercício06
            print('\nExercício06')
            inicio = int(input('Informe o início: '))
            fim = int(input('Informe o fim: '))
            exercicio06(inicio,fim)
        elif(opcao == 7):
            #Exercício07
            print('\nExercício07')
            impares()
        elif(opcao == 8):
            #Exercício08
            print('\nExercício08')
            print(somar10Inteiros())
        elif(opcao == 9):
            #Exercicio 09
            print('\n. Exercício09')
            print(somarNumero())
        elif(opcao == 10):
            #Exercício10
            print('\nExercício10')
            print(calcularMedia())
        elif(opcao == 11):
            #Exercício11
            print('\nExercício11')
            print(maiorMenor())
        elif(opcao == 12):
            #Exercício12
            print('\nExercício12')
            print(positivoNegativo())
        elif(opcao == 13):
            #Exercício13
            print('\nExercício13')
            num = int(input('Informe um número: '))
            print(fatorial(num))
        elif(opcao == 14):
            #Exercício14
            print('\nExercício14')
            print(mediaVolei())
        elif(opcao == 15):
            #Exercício15
            print('\nExercício15')
            print(miss())
        elif(opcao == 16):
            #Exercício16
            print('\nExercício16')
            print(eleicao())
        elif(opcao == 17):
            return
        elif(opcao == 18):
            return
        elif(opcao == 19):
            return
        elif(opcao == 20):
            print('\nExercício 20')
            vetoresPares = int(input('Informe os números pares: '))
            vetoresImpares = int(input('Informe os números impares: '))
            print(vetoresPares)
            print(vetoresImpares)
        elif(opcao == 21):
            num = int(input('Informe o tamanho do Vetor: '))
            preencherVetor(num)
        elif(opcao == 22):
            num = int(input('Informe o tamanho do Vetor: '))
            consultarVetor(num)
        elif(opcao == 23):
            posicao = int(input('Informe a posição que deseja apagar: '))
            apagarPosicao(posicao-1)
        else:
            print('Opção escolhida não é válida, digite novamente!')