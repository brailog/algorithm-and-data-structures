# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 23:49:08 2018
@author: Gabriel
"""
import numpy as np

class Grafo:
    def __init__(self, v=None):
        if v is not None:
            self.vertice = v
            self.matriz = np.zeros([v,v], dtype='b')
            self.vazio = False
        else:
            self.vertice = None
            self.matriz = [[]]
            self.vazio = True
            
    def __str__(self):
        string = ''
        for x in self.matriz:
            string += str(x)
            string += '\n'
        return string
    
    def __repr__(self):
        return '{}({})'.format(__class__.__name__, self.vertice)
    
    def ligar_vertice(self,i,j):
        '''
        Método para ligar dos vertices do grafo entre si.
        Se os vertices não existem ele apenas retorna um erro
        :param i: Primeiro vertice a ser ligado.
        :param j: Segundo vertice a ser ligado com o primeiro.
        '''
        if self.vazio:
            raise IndexError('Grafo Vazio')
        try:
            if i < self.matriz.size -1 and j < self.matriz.size:
                self.matriz[i,j] = 1
                self.matriz[j,i] = 1
        except:
            raise IndexError('Vértice fora de tamanho')
        
    def adjacentes_de(self,v):
        '''
        Método que retonar uma lista de todos os adjacentes de um vertice 
        passado como parametro
            '''
        try:
            adjacente = []
            for i,j in enumerate(self.matriz[v]):
                if j:
                    adjacente.append(i)
            return adjacente
        except:
            raise IndexError('Vertice não encontrado no grafo')
            
if __name__ == '__main__':
    g = Grafo(7)
    g.ligar_vertice(0,1)
    g.ligar_vertice(0,2)
    g.ligar_vertice(1,3)
    g.ligar_vertice(3,4)
    g.ligar_vertice(2,4) 
    g.ligar_vertice(4,5)
    g.ligar_vertice(2,1)
    g.ligar_vertice(5,6)
    print(g)  
    print(g.adjacentes_de(4))