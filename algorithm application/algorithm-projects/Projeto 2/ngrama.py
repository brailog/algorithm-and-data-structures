class Ngrama:
    def __init__(self,inicio,fim,doc):
        '''
        :param inicio: número inteiro que indica o início do intervalo do ngrama
        :param fim: número inteiro que indica o fim do intervalo do ngrama
        :param doc: referência ao documento ao qual o ngrama se refere
        '''
        self.__inicio = inicio
        self.__fim = fim
        self.__doc = doc

    def __repr__(self):
        return '{0}({1}, {2}, {3})'.format(self.__class__.__name__,
                self.__inicio, self.__fim,self.__doc.__repr__())

    def __str__(self):
        content = ' '.join(self.__doc.texto[i] for i in range(self.__inicio, 
                           self.__fim+1))
        return content
    
    @property
    def get_doc(self):
        return self.__doc
    
    def __contains__(self,palavra):
        index = self.__inicio
        while index <= self.__fim:
            if self.__doc.texto[index] == palavra:
                return True
            index += 1
        return False
    
    def __eq__(self,sp_ngrama):
        index = self.__inicio
        _index = sp_ngrama.__inicio
        while index <= self.__fim:
            if self.__doc.texto[index] != sp_ngrama.texto[_index]:
                return False
            index += 1
            _index += 1
        return True
