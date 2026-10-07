class Strumenti
    def __init__(self, codice, tipo, marca, anno, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno = anno
        self.valore = valore

    def __str__(self):
        return f"{self.codice} {self.tipo} {self.marca} {self.anno_acquisto} {self.valore:}"