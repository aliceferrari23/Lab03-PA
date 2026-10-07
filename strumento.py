class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.codice = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.codice} {self.tipo} {self.marca} {self.anno} {self.valore:}"