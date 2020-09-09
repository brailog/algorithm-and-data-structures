class _No:
    def __init__(self,anterior,proximo,item):
        self.anterior = anterior
        self.proximo = proximo
        self.item = item

class iterador:
    def __init__(self, lista):
        self.atual = lista.primeiro
    def __next__(self):
        if self.atual.proximo is None:
            raise StopIteration
        else:
            self.atual = self.atual.proximo
            return self.atual.item

class Lista:
    def __init__(self,*args):
        self.tamanho = 0
        self.primeiro = self.ultimo = _No(None,None,None)

    def anexar(self,item):
        self.ultimo.proximo = _No(self.ultimo,None,item)
        self.ultimo = self.ultimo.proximo
        self.tamanho += 1

    def __iter__(self):
        return iterador(self)
    
    def __len__(self):
        return self.tamanho


    def add_ordenado(self, i, item):
        cont += -1
        posicao = self.primeiro
        while i == cont or self.proximo is None:
            posicao = posicao.proximo
            cont += 1
        posicao.anterior =No(posisao.anterior,posicao,item)
        posicao.anterior.anterior.proximo = posicao.anterior
        self.tamanho += 1

    def remove_no_fim(self,):
        aux = self.ultimo
        self.ultimo = self.ultimo.anterior
        self.ultimo.proximo = None
        aux.anterior = None
        val = aux.item
        aux.item = None
        self.tamanho -= 1
        del(aux)
        return val

    def __getitem__(self, i):
        atual = self.primeiro
        cont = -1
        while atual.proximo is not None and cont != i:
            atual = atual.proximo
            cont += 1
        if cont == i:
            return atual.item
        else:
            return IndexError

    def __repr__(self):
        saida = f'{self.__class__.__name__}('
        content = ', '.join(x.__repr__() for x in self)
        saida+= content + ')'
        return saida

    def __str__(self):
        saida = f'('
        content = ', '.join(x.__repr__() for x in self)
        saida+= content + ')'
        return saida