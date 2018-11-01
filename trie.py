import numpy as np

class No:
    def __init__(self,letra,docs=None):
        self.letra = letra
        self.docs = docs
        self.filho = np.ndarray(shape = 37, dtype = object)
    
    def __repr__(self):
        return '{0}({1}, {2})'.format(self.__class__.__name__,
                self.letra.__repr__(),self.docs.__repr__())
    
class Trie:
    def __init__(self):
        self.cabeca = No(None)
    
    def __repr__(self):
        return '{0}()'.format(self.__class__.__name__)
        
    def __getitem__(self,ngrama):
        gramas = str(ngrama)
        pos_atual = self.cabeca
        for c in gramas:
            index = self.posicao_letra(c)
            if pos_atual.filho[index] is None:
                raise KeyError(str(ngrama))
            pos_atual = pos_atual.filho[index]
        if pos_atual.docs is not None:
            return pos_atual.docs
        else:
            raise KeyError(str(ngrama))  
            
    def __contains__(self,ngrama):
        gramas = str(ngrama)
        pos_atual = self.cabeca
        for c in gramas:
            index = self.posicao_letra(c)
            if pos_atual.filho[index] is None:
                return False
            pos_atual = pos_atual.filho[index]
        if pos_atual.docs is not None:
            return True
        else:
            return False
       
        
    @staticmethod
    def posicao_letra(letra):
        '''
        :param letra: Caracter a ser convertido em sua posição numérica
        :return: Retorna inteiro correspondente a posição da letra
        '''
        if letra >= 'a' and letra <= 'z':
            return ord(letra) - ord('a')
        elif letra >= '0' and letra <= '9':
            return (ord(letra) - ord('0')) + 27
        #elif letra >= 'A' and letra <= 'Z':
        #    return ord(letra) - ord('A')
        else:
            return 26
            
    def inserir(self,ngrama):
        '''
        A função insere os caracter do ngrama como No da arvore Trie
        :param ngrama: Sequencia de N palavras advinda de um documento
        '''
        chave = str(ngrama)
        pos_atual = self.cabeca
        for c in chave:
            index = self.posicao_letra(c)
            if pos_atual.filho[index] is None:
                pos_atual.filho[index] = No(c)
            pos_atual = pos_atual.filho[index]
        if pos_atual.docs is None:
            pos_atual.docs = []
        pos_atual.docs.append(ngrama.get_doc)       