# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 03:15:37 2018

@author: Gabriel
"""
class GrafoMatriz:
    def __init__(self,arestas,direcionado=False):
        self._tree = False
        self.__arestas = arestas
        self.__nvertices = 0
        self.__direcionado = direcionado
        self.__start
        
    @property
    def __start(self):
        
        '''
        Método para formatar o grafo sempre que precisar, formatando o tamanho 
        e "ligando" os vertices
        '''
        for vertices in self.__arestas:
            if vertices[0] > vertices[1]:
                self.__nvertices = vertices[0]
            else:
                self.__nvertices = vertices[1]  
            self.__nvertices += 1
            
        self.__matriz = [[0]*self.__nvertices for _ in range(self.__nvertices)]
        
        if len(self.__arestas[0]) == 2:
            try:
                self.__peso = False
                for tuplas in self.__arestas:
                    self.__matriz[tuplas[0]][tuplas[1]] = 1
                    if not self.__direcionado:
                        self.__matriz[tuplas[1]][tuplas[0]] = 1
            except:
                raise IndexError('Index para vertice do grafo invalido')
        elif len(self.__arestas[0]) == 3:
            try:
                self.__matriz = [[0]*self.__nvertices for _ in range(self.__nvertices)]
                self.__peso = True
                for tuplas in self.__arestas:
                    self.__matriz[tuplas[0]][tuplas[1]] = tuplas[2]
                    if not self.__direcionado:
                        self.__matriz[tuplas[1]][tuplas[0]] = tuplas[2]
            except:
                raise IndexError('Index para vertice do grafo invalido')
        else:
            raise IndexError('Número em tuplas maior que o experado')
            
    def __str__(self):
        string = '  '
        for i in range(len(self.__matriz)):
            string += '  {}'.format(i)
        string += '\n'
        cont = 0
        for _ in self.__matriz:
            string += '{}  '.format(cont)
            string += str(_)
            string += '\n'
            cont += 1 
        return string
        
    def __repr__(self):
        string = ''
        for x in self.__arestas:
            string += '{}'.format(x)
        return '{}(({}))'.format(__class__.__name__,string)
    
    def __getitem__(self,v):
        '''
        Método para acessar um vetor por meio de indexação.
        :return: Retorna, em forma de tupla, todas as arestas que se conecta 
        ao vertice passado como parametro, se existir peso, retorna com o peso 
        '''
        lista = []
        p= []
        try:
            if not self.__peso:
                adjacente = []
                for i,j in enumerate(self.__matriz[v]):
                    if j:
                        adjacente.append(i)
                for x in adjacente:
                    lista.append((v,x))
                return tuple(lista)
            else:
                adjacente = []
                for i,j in enumerate(self.__matriz[v]):
                    if j:
                        adjacente.append(i)
                for pesos in self.__matriz[v]:
                    if pesos >= 1:
                        p.append(pesos)
                i = len(p) - 1
                _i = 0
                while i >= _i:
                    lista.append((v,adjacente[_i],p[_i]))
                    _i += 1 
                return tuple(lista)
        except:
            raise IndexError('Vertice -{}- não encontrado no grafo'.format(v))
            
    @property
    def tree(self):
        self.busca_largura(0)
        return self._tree
            
    def to_lista(self):
        for vertices in self.__arestas:
            if vertices[0] > vertices[1]:
                self.__nvertices = vertices[0]
            else:
                self.__nvertices = vertices[1] 
        self.__nvertices += 1
        self.__adj_lista = [[] for _ in range(self.__nvertices)]
        
        if len(self.__arestas[0]) == 2:
            try:
                self.__peso = False
                for vertice in self.__arestas:
                    self.__adj_lista[vertice[0]].append(vertice[1])
                    if not self.__direcionado:
                        self.__adj_lista[vertice[1]].append(vertice[0])
            except:
                raise IndexError('Index para vertice do grafo invalido')
        
        elif len(self.__arestas[0]) == 3:
            try:
                self.__peso = True
                for vertice in self.__arestas:
                    self.__adj_lista[vertice[0]].append((vertice[1],vertice[2]))
                    if not self.__direcionado:
                        self.__adj_lista[vertice[1]].append((vertice[0],vertice[2]))
            except:
                raise IndexError('Index para vertice do grafo invalido')
        
        string = 'Lista de adjacencia\n'
        cont = 0
        for x in self.__adj_lista:
            x.sort()
            string += '{}: {}\n'.format(cont,x)
            cont += 1
        print(string)
        return self.__adj_lista
    
    def add_vertice(self,v,_v,p=0):
        '''
        Método para adicionar um novo vertice, ligando ele a um novo vertice
        :param v: Vertice a ser adicionado
        :param _v: Vertice a ser ligado com o vertice v
        :param p: Possivel peso do vertice
        '''
        if not self.__peso:
            if v > self.__nvertices - 1:
                self.__arestas = list(self.__arestas)
                self.__arestas.append((v,_v))
                self.__arestas = tuple(self.__arestas)
                self.__start
            else:
                raise IndexError('Vertice Invalido')
        else:
            if v > self.__nvertices - 1:
                self.__arestas = list(self.__arestas)
                self.__arestas.append((v,_v,p))
                self.__arestas = tuple(self.__arestas)
                self.__start
            else:
                raise IndexError('Vertice Invalido')
                
    def remover_vertice(self,v):
        '''
        Remove um vertice especifico passado como parametro.
        Se precisar do mesmo outra vez, utilize o método adicionar aresta.
        o vertice quando se é removido apenas tem todas a suas arestas "removidas"
        '''
        l = []
        if v <= self.__nvertices - 1:
            self.__arestas = list(self.__arestas)
            for tuplas in self.__arestas:
                if tuplas[0] == v or tuplas[1] == v:
                    continue
                else:
                    l.append(tuplas)
            self.__arestas = tuple(l)
            self.__start
            
    def adicionar_arestas(self,v,_v,p=0):
        '''
        Método para ligar dos vertices do grafo entre si.
        Se os vertices não existem ele apenas retorna um erro
        :param i: Primeiro vertice a ser ligado.
        :param j: Segundo vertice a ser ligado com o primeiro.
        :param p: Possivel peso do vertice
        '''
        try:
            if not self.__peso:
                if v <= self.__nvertices - 1 and _v <= self.__nvertices - 1:
                    self.__matriz[v][_v] = 1
                    if not self.__direcionado:
                        self.__matriz[_v][v] = 1
            else:
                if v <= self.__nvertices - 1 and _v <= self.__nvertices - 1:
                    self.__matriz[v][_v] = p
                    if not self.__direcionado:
                        self.__matriz[_v][v] = p
        except:
            raise IndexError('Vértice -{}- fora de tamanho'.format(v))
    
    def remover_aresta(self,v,_v,p=0):
        '''
        Método que remove uma aresta,especifica, entre dos vertices 
        '''
        if v <= self.__nvertices - 1 and _v <= self.__nvertices - 1:
            self.__matriz[v][_v] = 0
            if not self.__direcionado:
                self.__matriz[_v][v] = 0
                    
    def ligados(self,v,_v):
        '''
        Método que retorna True se os vertices passado como parametro estiverem
        ligados entre si, e False para o contrario.
        '''
        if v <= self.__nvertices - 1 and _v <= self.__nvertices - 1:
            return bool(self.__matriz[v][_v])
        raise IndexError('Vértice -{}- fora de tamanho'.format(v))
    
    def grau_saida(self,v):
        '''
        Método que retorna o grau de saida de um vertice passado como parametro
        '''
        cont = 0
        if v <= self.__nvertices - 1:
            for ligacao in self.__matriz[v]:
                if ligacao:
                    cont += 1
            return cont
        raise IndexError('Vértice -{}- fora de tamanho'.format(v))
    
    def grau_entrada(self,v):
        '''
        Método que retorne o grau de entrada de um vertice passado como parametro
        '''
        cont = 0
        if v <= self.__nvertices - 1:
            for ligacao in self.__matriz:
                if ligacao[v]:
                    cont += 1
            return cont
        raise IndexError('Vértice -{}- fora de tamanho'.format(v))
        
    def adjacentes_de(self,v):
        '''
        Método que retonar uma lista de todos os adjacentes de um vertice 
        passado como parametro
            '''
        try:
            adjacente = []
            for i,j in enumerate(self.__matriz[v]):
                if j:
                    adjacente.append(i)
            return adjacente
        except:
            raise IndexError('Vertice não encontrado no grafo')
    
    def busca_profundidade(self,v):
        '''
        Método de busca em profundidade sobre o grafo implementado
        :param v: Vertice inical da busca
        '''
        marcado = self.__nvertices * [False]
        antecessor = self.__nvertices*[-1]
        for vertice in range(v,self.__nvertices):
            if not marcado[vertice]:
                self.__dfs(v,vertice,antecessor,marcado)
        for i in range(0,self.__nvertices):
            print(antecessor[i],'É antecessor de ',i)
        del marcado
        del antecessor
        
    def __dfs(self,v,vertice,antecessor,marcado):
        '''
        Método recursivo para marcar todos os vertices na busca em profundidade
        :param v: Vertice inicial
        :param vertice: vertices do grafo
        :param antecessor: lista de antecessores
        :param marcado: vertices já marcado
        '''
        marcado[vertice] = True
        for adjacente in self.adjacentes_de(vertice):
            if not marcado[adjacente]:
                antecessor[adjacente] = vertice
                self.__dfs(v,adjacente,antecessor,marcado)
    
    def busca_largura(self,v):
        '''
        Método para busca em largura sobre o grafo implementado
        '''
        marcado = self.__nvertices * [False]
        antecessor = self.__nvertices * [-1]
        vertices = list()
        for vertice in range(v,self.__nvertices):
            if not marcado[vertice]:
                vertices.append(vertice)
                marcado[vertice] = True
                while len(vertices) > 0:
                    _v = vertices.pop(0)
                    for adjacente in self.adjacentes_de(_v):
                        if not marcado[adjacente]:
                            marcado[adjacente] = True
                            antecessor[adjacente] = _v
                            vertices.append(adjacente)
        
        cont = 0
        for i in range(0,self.__nvertices):
            print(antecessor[i],'É antecessor de ',i)
            if antecessor[i] == -1:
                cont += 1
                if cont > 1:
                    self._tree = True
        del marcado
        del antecessor
                            
if __name__ == '__main__':
    g = GrafoMatriz(((0,2),(0,5),(0,4),(2,3),(1,3),(3,5)))
    g1 = GrafoMatriz(((0,2,5),(0,5,3),(0,4,7),(2,3,6),(1,3,1),(3,5,9)))
    print('--- Sem peso ---')
    print(g)
    print('--- Com peso ---')
    print(g1)
    
    