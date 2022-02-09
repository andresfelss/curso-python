from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, marcaR, tipoEntradaR):
        Raton.contadorRatones += 1
        self._id_raton = Raton.contadorRatones
        super().__init__(marcaR, tipoEntradaR)
        self._marcaR = marcaR
        self._tipoentradaR = tipoEntradaR

    def __str__(self):
        return f'Id: {self._id_raton} Marca: {self._marcaR} Tipo_entrada: {self._tipoentradaR}'
