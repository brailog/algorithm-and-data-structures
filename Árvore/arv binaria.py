class No:
    def __init__(self,chave=None,valor=None,esquerda=None,direita=None):
        self.chave = chave
        self.valor = valor
        self.esquerda =	esquerda
        self.direita =	direita

class Arv_binaria:
    def __init__(self):
        self.raiz = None
    
    def __repr__(self):
        return '{0}()'.format(self.__class__.__name__)
    
    def inserir(self,chave,valor):
        '''
        Função inserir, acessivel para o usuario
        :param chave: Valor da chave
        :param valor: Valor a ser inserido
        '''
        self.raiz = self.__inserir(self.raiz,chave,valor)
    
    def __inserir(self,nodo,chave,valor):
        '''
        Função privada que faz o papel de inserir os elementos analisando a posição
        de cada nodo, se é maior, menor ou igual, e inserido em sua posição correta
        :param nodo: Nodo da arvore
        :param chave: Chave a ser inserida
        :param valor: Valor 
        '''
        if nodo is None:
            return No(chave,valor)
        if nodo.chave > chave:
            nodo.esquerda = self.__inserir(nodo.direita,chave,valor)
        elif nodo.chave < chave:
            nodo.direita = self.__inserir(nodo.esquerda,chave,valor)
        else:
            nodo.valor = valor
        return nodo
    
    def valor(self, chave):
        '''
        Função para acessar, se tiver, um valor correspondete a chave passada
        como parametro
        :param chave: Chave para acessar o suposto valor
        '''
        aux = self.raiz
        while not aux is None:
            if aux.chave == chave:
                return aux.valor
            elif aux.chave < chave:
                aux = aux.direita
            else:
                aux = aux.esquerda
        raise KeyError(chave)
    
    def remover(self,chave,valor):
        '''
        Função remover, acessivel para o usuario
        :param chave: Valor da chave a ser removido
        :param valor: Valor a ser removido
        '''
        self.__remove(chave,valor,self.raiz)
    
    def __remove(self,chave,valor,nodo):
        '''
        Função privada que faz o papel de remover os elementos, simplismente 
        removendo, ou reposicionado os filhos
        :param nodo: Nodo da arvore
        :param chave: Chave a ser inserida
        :param valor: Valor 
        '''
        if nodo is None:
            raise KeyError(chave)
         
        elif nodo.chave < chave:
            nodo.direita,valor = self.__remove(chave,valor,nodo.direita)
        elif nodo.chave > chave:
            nodo.esquerda,valor = self.__remove(chave,valor,nodo.esquerda)
        else:
            valor =	nodo.valor
            if nodo.direita is None:
                aux = nodo
                nodo = nodo.esquerda
                del aux
            elif nodo.esquerda is None:
                aux = nodo
                nodo = nodo.direita
                del aux
            else:
                nodo.esquerda = self.__antecessor(nodo,nodo.esquerda)
        return nodo,valor
    
    def __antecessor(self,q,r):
        '''
        Função auxiliar da função remover
        :param q: Filho do antecessor
        :param r: Filho do antecessor a esquerda
        '''
        if not r.direita is None:
            r.direita =	self.__antecessor(q,r.direita)
        else:
            q.valor = r.valor
            aux = r
            r =	r.esquerda
            del aux
        return r
    
    def em_ordem(self,p):
        '''
        Print de forma correta, em ordem.
        :param p: Nodo de partidada para a print
        '''
        if not p is None:
            self.em_ordem(p.esquerda)
            print(p.valor)
            self.em_ordem(p.direita)
    
    def pre_ordem(self,p):
        '''
        Print de forma correta, pre ordem.
        :param p: Nodo de partidada para a print
        '''
        if not p is None:
            print(p.valor)
            self.pre_ordem(p.esquerda)
            self.pre_ordem(p.direita)
            
    def pos_ordem(self,p):
        '''
        Print de forma correta, por ordem.
        :param p: Nodo de partidada para a print
        '''
        if not p is None:
            self.pos_ordem(p.esquerda)
            self.pos_ordem(p.direita)
            print(p.valor)

if __name__ == '__main__':
    Tree = Arv_binaria()