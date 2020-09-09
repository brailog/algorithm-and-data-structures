# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:55:40 2018

@author: Gabriel
"""

import sys

def ler_arquivo(file):
    '''
    Função que ler de um arquivo os valores do peso, valor agredodo do item e
    os itens 
    '''    
    valor = [0]
    peso = [0]
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

peso,valor,capacidade_maxima = ler_arquivo(sys.argv[1])

def max_valor(capacidade_maxima, numero_itens):
    '''
    Função que calcula, de forma recursiva, o maior valor possivel dado um 
    limite de peso e um array de itens e seus respectivos pesos
    :param numero_itens: Quantidade de itens
    :param capacidade_maxima: capacidade maxima que a locomotiva pode carregar
    :param return: Retorna o lucro maximo
    '''
    if capacidade_maxima == 0:
        return 0
    if numero_itens == 0:
        return 0
    elif peso[numero_itens] > capacidade_maxima:
        return max_valor(capacidade_maxima, numero_itens-1)
    else:
        return max(max_valor(capacidade_maxima-peso[numero_itens], numero_itens-1)+valor[numero_itens], 
                   max_valor(capacidade_maxima, numero_itens-1))

if __name__ == '__main__':
    print('De forma recurvisa\nO valor maximo possivel é:', max_valor(capacidade_maxima,len(peso)-1))