# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:19:54 2018

Copyright(c) 2018 Gabriel Ramos Rodrigues Oliveira
"""

class No:
    def __init__(self,item=None,proximo=None):
        self.item = item
        self.proximo = proximo
        
    def __repr__(self):
        return "No({})".format(self.item.__repr__())
    
    def __str__(self):
        return self.item.__str__()
        
class iterador:
    def __init__(self, lista):
        self.atual = lista.primeiro
    def __next__(self):
        if self.atual.proximo is None:
            raise StopIteration
        else:
            self.atual = self.atual.proximo
            return self.atual.item

class ListaEncadeada:
    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanho_lista = 0
        
    def __len__(self):
        return int(self.tamanho_lista)
    
    def __str__(self):
        saida = f'('
        content = ', '.join(x.__repr__() for x in self)
        saida+= content + ')'
        return saida
    
    def __repr__(self):
        saida = f'{self.__class__.__name__}('
        content = ', '.join(x.__repr__() for x in self)
        saida+= content + ')'
        return saida
    
    def __iter__(self):
        return iterador(self)    
    
    def __getitem__(self, i):
        '''
        Busca de elemento por meio da atribuição - item[index] - 
        :param i: Index do item a ser buscado
        '''
        cont = -1
        aux = self.primeiro
        while aux is not None and cont < i:
            cont += 1
            aux = aux.proximo
        if aux is None:
            raise IndexError('list index out of range')
        return aux.item 

    def __contains__(self,item):
        '''
        Método utilizado para saber se o item está contido na lista por meio de
        - item in ListaEncadeada - 
        '''
        aux = self.primeiro.proximo
        while not aux is None and aux.item != item:
            aux = aux.proximo
        try:
            return aux.item is not None
        except:
            return False           
        
    @property
    def __vazia(self):
        '''
        Verifica se a lista está vazia
        :return : Retorna se a lista é vazia ou não
        '''
        return self.primeiro == self.ultimo 
    
    def inserir(self,item):
        '''
        Adiciona um item qualquer, no final da lista
        :param item: Elemento a ser adicionado no final da lista
        '''
        self.ultimo.proximo = No(item,None)
        self.ultimo = self.ultimo.proximo
        self.tamanho_lista += 1
               
    def inserir_inicio(self,item):
        '''
        Adiciona um item qualquer, no inicio da lista
        :param item: Elemento a ser adicionado no final da lista
        '''
        self.primeiro.proximo = No(item,self.primeiro.proximo)
        if self.__vazia:
            self.ultimo = self.primeiro.proximo
        self.tamanho_lista += 1
    
    def inserir_ordenado(self,item):
        '''
        Adiciona um item qualquer, no inicio da lista
        :param item: Elemento a ser adicionado no final da lista
        '''
        if self.__vazia:
            self.inserir(item)
            return
        no_anterior = self.primeiro
        no_atual = self.primeiro.proximo
        
        while not no_atual is None and no_atual.item < item:
            no_anterior = no_atual
            no_atual = no_anterior.proximo
        no_anterior.proximo = No(item,no_atual)
        if no_atual is None:
            self.ultimo = no_anterior.proximo
        self.tamanho_lista += 1
        
    def remover_ultimo(self):
        '''
        Remove o ultimo item da lista
        '''
        if self.__vazia:
            return None
        aux = self.primeiro
        while aux.proximo != self.ultimo:
            aux = aux.proximo
        item = self.ultimo.item
        ultimo = aux
        ultimo.proximo = None
        del aux
        self.tamanho_lista += -1
        return item
    
    def remover_primeiro(self):
        '''
        Remove o primeiro item da lista
        '''
        if self.__vazia:
            return None
        aux = self.primeiro.proximo
        self.primeiro.proximo = aux.proximo
        item = aux.item
        if self.ultimo == aux:
            self.ultimo = self.primeiro
        aux.prox = None
        del aux
        self.tamanho_lista += -1
        return item


if __name__ == '__main__':
    l = ListaEncadeada()
    l.inserir('a')
    l.inserir('b')
    l.inserir('cavalaria')
    print(l)
    l.remover_primeiro()
    print(l)
    