# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:46:46 2018

@author: Gabriel

A estrutura otima para esssa situação é a utilização de uma MATRIZ
"""
import sys

def ler_arquivo(file):
    '''
    Função que ler de um arquivo os valores do peso, valor agredodo do item e
    os itens 
    '''    
    valor = []
    peso = []
    n = ''
    with open(file,'r') as f:
        capacidade_maxima = f.readline()
        capacidade_maxima = capacidade_maxima[0:len(capacidade_maxima) -1]
        a = f.read()
        try:
            for x in a:
                if x == '\n':
                    valor.append(int(n))
                    n = ''
                elif x != ',':
                    n += x
                else:
                    peso.append(int(n))
                    n = ''
        except:
            pass

    return peso,valor,int(capacidade_maxima)

def escolhidos_valor(peso,valor,capacidade_maxima):
    '''
    Função que calcula o maior valor possivel dado um limite de peso 
    e um array de itens e seus respectivos pesos
    :param peso: Lista de pesos dos itens 
    :param valor: Lista dos valores dos itens 
    :param capacidade_maxima: capacidade maxima que a locomotiva pode carregar
    :param return: Retorna o valor maximo e os items necessario para que o valor 
    seja o maximo
    '''
    itens_escolhidos = []
    
    matriz = [[float('inf')]*(capacidade_maxima +1) for _ in range(len(peso)+1)]
    for capacidade in range(capacidade_maxima + 1):
        for item in range(len(peso) +1):
            if capacidade == 0 or item == 0:
                matriz[item][capacidade] = 0
            elif peso[item-1] > capacidade:
                matriz[item][capacidade] = matriz[item-1][capacidade]
            else:
                matriz[item][capacidade] = max(matriz[item-1][capacidade], matriz[item-1][capacidade-peso[item-1]] + valor[item-1]) 
    #Linhas de codigo para descobri quais os itens que foram selecinados para o valor ser maximo
    valor = matriz[len(peso)][capacidade_maxima]
    for item in range(len(peso),0,-1):
        if matriz[item][capacidade_maxima] != matriz[item-1][capacidade_maxima]:
            itens_escolhidos.append(item)
            capacidade_maxima -= peso[item-1]
    return 'O valor maximo é: {}\ne os itens que você deve escolher para esse valor ser maximo é: {}'.format(valor,itens_escolhidos)

if __name__ == '__main__':
    peso,valor,capacidade_maxima = ler_arquivo(sys.argv[1])
    print(escolhidos_valor(peso,valor,capacidade_maxima))
    