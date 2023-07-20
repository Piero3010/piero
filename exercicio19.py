#19. Escreva um programa para informar o
#maior elemento de um vetor de 5 posições do
#tipo inteiro.
def maiorElemento(num):
    for i in range(num):
        num = int(input('Informe a {}ª posição: '.format(i + 1)))
        print('Informe a maior nota!')
        notas.append(num)  # Adicionando notas no vetor
    if (len(num) > posicao):
        print('Impossível remover, pois o tamanho é maior que a posição')
    else:
        del(notas[posicao]) #Excluindo um dado do vetor
        print('Fim!')