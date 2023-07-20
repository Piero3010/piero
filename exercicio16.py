#16. Escreva um algoritmo para ler o
#número total de eleitores de um
#município, o número de votos brancos,
#nulos e válidos. Calcular e escrever o
#percentual que cada um representa em
#relação ao total de eleitores.
def coletarPositivoInteiro():
    num = int(input())
    while(num <= 0):
        print('Erro!!! informe um valor positivo')
        num = int(input('Informe um número: '))
    return num

def transformarPercentual(num, total):
    percentual = (total / num) * 100
    return percentual

def eleicao():
    print('Informe o total de votos brancos: ')
    brancos = coletarPositivoInteiro()
    print('Informe o total de votos nulos: ')
    nulos   = coletarPositivoInteiro()
    print('Informe o toal de votos validos: ')
    validos = coletarPositivoInteiro()
    print('Informe o total de eleitores: ')
    total   = coletarPositivoInteiro()
    #Verificar se o total é igual a brancos, válidos e nulos
    if((brancos+nulos+validos) == total):
        pBrancos = transformarPercentual(brancos,total)
        pNulos   = transformarPercentual(nulos,total)
        pValidos = transformarPercentual(validos,total)
        return 'Votos Brancos: {}%\nVotos Nulos: {}%\nVotos Validos: {}%'.format(pBrancos,pNulos,pValidos)
    else:
        return 'Número de brancos, validos e nulos é diferente do total de eleitores, digite novamente!'
