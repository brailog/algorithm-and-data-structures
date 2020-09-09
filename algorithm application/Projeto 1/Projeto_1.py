import re
import os
import time
import numpy as np
from ngrama import Ngrama
from listaduplamente import *
#from profilefunc import profilefunc
#from memory_profiler import profile

class Corpus:
    def __init__(self):
        arq_src = os.listdir('dados/src')
        arq_sups = os.listdir('dados/susp')
        self.__vetor_arq_src = np.array(arq_src)
        self.__vetor_arq_susp = np.array(arq_sups)


    def verifiar_plagio(self,doc,limiar):
        plagio = []
        doc_suspeito = Documento(doc)
        cont = 0
        for files in self.__vetor_arq_src:
            cont += 1
            doc_analise = Documento('dados/src/{}'.format(files))
            var_limiar = doc_suspeito.contencao(doc_analise)
            if var_limiar > limiar:
                plagio.append(files)
        return plagio

class Documento:
    def __init__(self,fname):
        self.__list_duplamente_encadeada = Lista()
        def formatar_string(string):
            return re.findall('[a-zA-Z]+',string)

        with open(fname,'r',encoding='utf-8') as file:
            linhas = file.read()
            gerador = formatar_string(linhas.lower())
            self.__vetor_texto = np.array(gerador)

        self.gerar_ngrama()

    def gerar_ngrama(self):
        ngrama = [self.__vetor_texto[i:i+3] for i in range(len(self.__vetor_texto)-2)]
        for x in ngrama:
            n = Ngrama(x[0],x[1],x[2])
            self.__list_duplamente_encadeada.anexar(n)
        return self.__list_duplamente_encadeada

    def iterador_ngrama(self):
        return self.__list_duplamente_encadeada.__iter__()

    def get_ngrama_size(self):
        return len(self.__list_duplamente_encadeada)

    def contencao(self,v):
        isrc = self.iterador_ngrama()
        isusp = v.iterador_ngrama()
        aux = self.get_ngrama_size()

        vsrc = next(isrc)
        vsusp = next(isusp)

        cont = 0
        while True:
            try:
                while str(vsrc) != str(vsusp):
                    vsrc = next(isrc) #AQUI É ONDE MUDA O SUSPEITO
                    
                    print(vsrc,'-',vsusp)
                    if str(self.__list_duplamente_encadeada[aux-1]) == str(vsrc):
                        isrc = self.iterador_ngrama()
                        vsusp = next(isusp)
                else:
                    vsusp = next(isusp) #AQUI É ONDE MUDA O NÃO U
                    cont += 1
            except StopIteration:
                break



        return cont/self.get_ngrama_size()


a = Corpus()
print(a.verifiar_plagio('suspicious-document00005.txt',0.05))
