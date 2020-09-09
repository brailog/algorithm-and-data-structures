'''
@author: grro

Script do Projeto

'''
import re
import os
import numpy as np
from ngrama import Ngrama
from listduplamenteencadeada import Lista
from trie import Trie
from profilefunc import profilefunc
from memory_profiler import profile

class Corpus:
    def __init__(self):
        self.__arvore = Trie()
        self.__start()
    
    def __start(self):
        '''
        Abre todos os arquivos src, intanciando cada arquivo a class Documento
        para ser aberto, e gerar seus n-gramas
        '''
        arq_src = os.listdir('dados/src')
        tam = len(arq_src)
        self.__arqsrc = np.ndarray(shape= tam, dtype = object)
        i = 0
        while i < tam:
            caminho = 'dados/src/{}'.format(arq_src[i])
            self.__arqsrc[i] = Documento(caminho)
            for ngrama in self.__arqsrc[i].listaNgrama:
                self.__arvore.inserir(ngrama)
            i += 1

    #@profilefunc
    #@profile
    def verifiar_plagio(self,doc,limiar):
        '''
        Recebe um documento suspeito e compara os ngramas do documento suspeito
        com os ngramas do documento atual a partir da árvore Trie na classe
        Corpus.
        :param doc: documento supeito a ser comparado
        :param limiar: limite de semelanhça entre os dois documentos
        (0 <= limiar <= 1)
        :return plagio: retorna True ou False se o documento for plágio ou não
        '''
        index = -1
        plagio = Lista()
        vetor_limiar = self.contencao(doc)
        for limias in vetor_limiar:
            index += 1
            if limias >= limiar:
                plagio.anexar(self.__arqsrc[index])
        
        return plagio
        
    def contencao(self,docsusp):
        '''
        Recebe um documento suspeito e um documento que possivelmente foi copiado
        e analisa a chance(porcentagem) de ter acontecido plágio entre esses documentos
        :param docsusp: documento suspeito a ser analisado        
        :param docsrc: documento que possivelmente foi copiado pelo suspeito
        :return: Retorna um vetor com a porcentagem de igualdade entre os documentos 
        '''
        self.contecao_geral = np.ndarray(shape= self.__arqsrc.size, dtype= float)
        dsusp = Documento(docsusp)
        for ngrama in dsusp.listaNgrama:
            self.__arvore.inserir(ngrama)
        cont = 0
        all_docs = self.__arqsrc.size -1 
        i = - 1
        while i != all_docs:
            i += 1
            cont = 0
            for ngrama in dsusp.listaNgrama:
                if self.__arqsrc[i] in self.__arvore[ngrama]:
                    print(self.__arqsrc[i],'=!=',self.__arvore[ngrama])
                    cont += 1
            self.contecao_geral[i] = cont/len(self.__arqsrc[i].listaNgrama)
        return self.contecao_geral
            
class Documento:
    def __init__(self,fname):
        self.__fname = fname
        self.__lista_duplamente_encadeada = Lista()
        def formatar_string(string):
            return re.findall('[a-zA-Z]+',string)

        with open(self.__fname,'r',encoding='utf-8') as file:
            linhas = file.read()
            gerador = formatar_string(linhas.lower())
            self.__vetor_texto = np.array(gerador)

        self.gerar_ngrama()
        
    @property
    def texto(self):
        return self.__vetor_texto
    
    @property
    def listaNgrama(self):
        return self.__lista_duplamente_encadeada
        
    def gerar_ngrama(self, n=3):
        fim = n - 1
        while fim < self.__vetor_texto.size:
            self.__lista_duplamente_encadeada.anexar(Ngrama(fim-(n-1),fim,self))
            fim += 1
        
    def iterador_ngrama(self):
        return self.__list_duplamente_encadeada.__iter__()

    def get_ngrama_size(self):
        return len(self.__list_duplamente_encadeada)
 
    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, repr(self.__fname))
    
if __name__ == "__main__":
    a = Corpus()
    print(a.verifiar_plagio('dados/susp/{}'.format('suspicious-document00005.txt'),0.7))
        