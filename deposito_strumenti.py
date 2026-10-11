from csv import reader
from logging import exception

from Strumenti import Strumento
from operator import attrgetter
from Prestito import Prestiti
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.__nome=nome
        self.__responsabile=responsabile
        self.lista_strumento=[]
        self.lista_prestiti=[]
        self.lista_codici=[]
    @property
    def responsabile(self):
        return self.__responsabile
    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile=responsabile
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome=nome
    def __str__(self):
        return f'{self.responsabile}'

    def carica_file_strumenti(self, file_path):
        try:
            file=open(file_path,'r')
            csvreader=reader(file)
            for riga in csvreader:
                    if riga[0].strip() not in self.lista_codici:
                        self.lista_codici.append(riga[0].strip())
                        strumento=Strumento(riga[0],riga[1],riga[2],riga[3],riga[4])
                        self.lista_strumento.append(strumento)


            print('strumenti caricati dal file correttamente.')
            return self.lista_strumento
        except:
            raise Exception('file non trovato')



    def stampa_lista(self):
        for strumento in self.lista_strumento:
            print(strumento.__str__())


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        if len(self.lista_strumento)==0:
            print('Prima devi inserire gli strumenti presenti nel deposito per catalogarli')
        else:
            codice= 'S'+str(len(self.lista_strumento)+1)
            strumento=Strumento(codice,tipo, marca, anno_acquisto, valore)
            self.lista_strumento.append(strumento)
            return strumento

    def strumenti_ordinati_per_marca(self):
        print('Qui sono elencati gli strumenti ordinati per marca: ')
        return sorted(self.lista_strumento,key=attrgetter('marca'))


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        loans=True
        for s in self.lista_strumento:
            if id_strumento!=s.codice:
                loans=False
            else:
                loans=True
                break
        if not loans:
            raise Exception('Lo strumento non è presente nella lista dei disponibili')
        if loans:
            for p in self.lista_prestiti:
                if id_strumento==p.id_strumento:
                    loans=False
                    break
                else:
                    loans=True

        if not loans:
            raise Exception('Lo strumento è già stato prestato')
        else:
            codice_prestito= 'P'+str(len(self.lista_prestiti)+1)
            prestito=Prestiti(codice_prestito,cognome_allievo,data,id_strumento)
            self.lista_prestiti.append(prestito)
            return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        loanp=True
        if loanp:
            for p in self.lista_prestiti:
                if id_prestito!=p.codice_prestito:
                    loanp=False
                else:
                    loanp=True
                    self.lista_prestiti.remove(p)
                    print('Prestito rimosso con successo')
                    break
            if not loanp:
                raise Exception('Il codice prestito non è valido')
            else:
                self.lista_prestiti


