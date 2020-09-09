class Ngrama:
    def __init__(self, palavra1,palavra2,palavra3):
        self.__palavra1 = palavra1
        self.__palavra2 = palavra2
        self.__palavra3 = palavra3

    def __str__(self):
        return '({},{},{})'.format(self.__palavra1, self.__palavra2, self.__palavra3)

    def __repr__(self):
        return 'Ngrama({},{},{})'.format(self.__palavra1, self.__palavra2, self.__palavra3)




