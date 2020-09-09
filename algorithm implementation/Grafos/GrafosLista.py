# -*- coding: utf-8 -*-
"""
Copyright(c) 2018 Gabriel Ramos Rodrigues Oliveira
"""

class GrafoLista:
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
        
    def __str__(self):    
        string = 'Lista de adjacencia\n'
        cont = 0
        for x in self.__adj_lista:
            x.sort()
            string += '{}: {}\n'.format(cont,x)
            cont += 1
        return string
            
    def __repr__(self):
        string = ''
        for x in self.__arestas:
            string += '{}'.format(x)
        return '{}(({}))'.format(__class__.__name__,string)
    
    def __getitem__(self,v):
        lista = []
        try:
            if not self.__peso:
                for vertice in self.__adj_lista[v]:
                    lista.append((v,vertice))               
            else:
                for vertice in self.__adj_lista[v]:
                    lista.append((v,vertice[0],vertice[1]))
            return tuple(lista)
        except:
            raise IndexError('Vertice -{}- não presente no Grafo')
                
                
    
    def add_aresta(self, v,_v,p=0):
        '''
        Método de criação de uma aresta ligando dois vertices já existentes
        '''
        if not self.__peso:
            if v <= self.__nvertices - 1 and _v <= self.__nvertices - 1:
                self.__adj_lista[v].append(_v)
                if not self.__direcionado:
                    self.__adj_lista[_v].append(v)
                    
    def to_matriz(self):
        '''
        Método que converte o Grafo de lista de adjacencia para uma Matriz de 
        adjacencia. Retornando o mesmo para ser utilizado, e printando para
        vizualização.
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
                self.__matriz = [[0]*self.nvertices for _ in range(self.nvertices)]
                self.__peso = True
                for tuplas in self.arestas:
                    self.__matriz[tuplas[0]][tuplas[1]] = tuplas[2]
                    if not self.__direcionado:
                        self.__matriz[tuplas[1]][tuplas[0]] = tuplas[2]
            except:
                raise IndexError('Index para vertice do grafo invalido')
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
        print(string)
        return self.__matriz
        
    def ligados(self,v,_v):
        '''
        Método que retorna True se os vertices passado como parametro estiverem
        ligados entre si, e False para o contrario.
        '''
        if v <= self.__nvertices - 1 and _v <= self.__nvertices - 1:
            if not self.__peso:
                for vertices in self.__adj_lista[v]:
                    if vertices == _v:
                        return True
                return False
            else:
                for vertices in self.__adj_lista[v]:
                    if vertices[0] == _v:
                        return True
                return False
    
    def grau_saida(self,v):
        '''
        Método que retorna um número inteiro com o grau de saída de um vertice 
        passado como parametro
        '''
        if v <= self.__nvertices - 1:
            return len(self.__adj_lista[v])
    
    def grau_entrada(self,v):
        '''
        Métoo que retorna um número inteiro com o grau de entrada de um vertice
        passado como parametro.
        '''
        cont = 0
        if v <= self.__nvertices - 1:
            for vertice in self.__adj_lista:
                if v in vertice:
                    cont += 1
            return cont
            
    @property
    def tree(self):
        self.busca_largura(0)
        return self._tree
    
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
                    for adjacente in self.__adj_lista[_v]:
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
        for adjacente in self.__adj_lista[vertice]:
            if not marcado[adjacente]:
                antecessor[adjacente] = vertice
                self.__dfs(v,adjacente,antecessor,marcado)      
    
if __name__ == '__main__':
    g = GrafoLista(((0,2),(0,5),(0,4),(2,3),(1,3),(3,5)))
    g1 = GrafoLista(((0,2,5),(0,5,3),(0,4,7),(2,3,6),(1,3,1),(3,5,9)))
    print('--- Sem peso ---')
    print(g)
    print('--- Com peso ---')
    print(g1)
