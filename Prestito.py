
class Prestiti:
    def __init__(self,codice_prestito,cognome_allievo,data,id_strumento):
        self.__data = data
        self.__id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo
        self.__codice_prestito=codice_prestito
    def __str__(self):
        return f'{self.__codice_prestito} {self.__id_strumento} {self.cognome_allievo} {self.__data}'
    @property
    def codice_prestito(self):
        return self.__codice_prestito
    @codice_prestito.setter
    def codice_prestito(self,codice_prestito):
        self.__codice_prestito=codice_prestito
    @property
    def id_strumento(self):
        return self.__id_strumento
    @id_strumento.setter
    def id_strumento(self,id_strumento):
        self.__id_strumento=id_strumento
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,data):
        self.__data=data