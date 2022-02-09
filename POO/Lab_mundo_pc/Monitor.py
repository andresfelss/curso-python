class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamano):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marcam = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marcam

    @marca.setter
    def marca(self, marca):
        self._marcam = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'Id: {self._idMonitor} Marca: {self._marcam} Tamaño: {self._tamano}'