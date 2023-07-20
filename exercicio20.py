#20. Crie um programa que armazene 10
#números digitados pelo usuário em dois
#vetores: um somente para números pares,
#e outro somente para números ímpares.
#Após, exiba os valores dos dois vetores
#na tela, em sequência. Obs.: As posições
#que não receberem valores exibirão o
#número zero.
def vetoresPares(par):
    for i in range(10):
        num = int(input('Informe o {}º número: '.format(i + 1)))
        print('Informe os números pares')
        if (len(par) < número):
            if (num % 2 == 0):
                soma += num
                contador += 1
            print('Impossível remover, pois o tamanho é maior que a posição')
        #Parar no décimo número par
def vetoresImpares(impar):
    for i in range(10):
        num = int(input('Informe o {}º número: '.format(i + 1)))
        if (num % 2 != 0):
            soma += num
            contador += 1
        print('Informe os números ímpares')
    #Parar no décimo número ímpar