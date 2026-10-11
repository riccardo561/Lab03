class Strumento:
    def __init__(self,codice,tipo,marca,anno,valore):
        self.__codice = codice
        self.tipo=tipo
        self.marca=marca
        self.anno=anno
        self.valore=valore

    def __str__(self):
        return f'{self.__codice} {self.tipo} {self.marca} {self.anno} {self.valore}'
    @property
    def codice(self):
        return self.__codice
    @codice.setter
    def codice(self,codice):
        self.__codice = codice



