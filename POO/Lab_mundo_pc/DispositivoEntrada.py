class DispositivoEntrada():
    def __init__(self, marca, tipoEntrada):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Marca: {self._marca}  Tipo_entrada: {self._tipoEntrada}'
