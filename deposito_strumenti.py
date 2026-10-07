import csv
from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self._responsabile=responsabile
        self.strumenti=[]
        self.prestiti=[]
        self.strumento_id_succ=1
        self.prestito_id_succ=1

    @property
    def responsabile(self):
       return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile=responsabile


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for riga in reader:
                if len(riga) == 5:
                    id_str, tipo, marca, anno, val = riga
                    strumento = Strumento(id_str, tipo, marca, anno, val)
                    self.strumenti.append(strumento)
                    try:
                        num_id = int(id_str[1])
                        if num_id >= self.strumento_id_succ:
                            self.strumento_id_succ = num_id + 1
                    except ValueError:
                        pass
                    except FileNotFoundError:
                        return None

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        nuovo_id = f"S{self.strumento_id_succ}"
        self.strumento_id_succ += 1

        nuovo_strumento = Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        #lista.sort(key=lambda x: x.attributo)
        ordinati=sorted(self.strumenti, key=lambda x: x.marca)
        #self.strumenti.sort(key=lambda x:x.marca)
        return ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        for s in self.strumenti:
         if s.id_strumento not in self.strumenti:
                raise Exception(f"Errore: Lo strumento non esiste nel deposito.")
        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                raise Exception(f"Errore: Lo strumento è già stato prestato.")
        nuovo_id_prestito = f"P{self.prestito_id_succ}"
        self.prestito_id_succ += 1
        prestito = Prestito(nuovo_id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito)
        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        prestito_da_rimuovere = None
        for p in self.prestiti:
            if p.id_prestito == id_prestito:
                prestito_da_rimuovere = p
                break
        if prestito_da_rimuovere is None:
            raise Exception(f"Errore: Non è stato trovato alcun prestito.")

        self.prestiti.remove(prestito_da_rimuovere)
