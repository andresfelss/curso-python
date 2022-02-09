from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, marcaT, tipoEntrada):
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
        super().__init__(marcaT, tipoEntrada)
        self._marcaT = marcaT
        self._tipoEntradaT = tipoEntrada

    def __str__(self):
        return f'Id: {self._idTeclado} Marca: {self._marcaT} Tipo_entrada: {self._tipoEntradaT}'
