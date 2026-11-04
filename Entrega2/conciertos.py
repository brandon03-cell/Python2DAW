class Entrada:
    def __init__(self, concierto):
        self.concierto = concierto

    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f'Entrada general para {self.concierto.artista} - {self.get_precio_total()} €'


class EntradaGrada(Entrada):
    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    def __str__(self):
        return f'Entrada de grada para {self.concierto.artista} - {self.get_precio_total()} €'


class EntradaPista(Entrada):
    def __init__(self, concierto, de_pie):
        super().__init__(concierto)
        self.de_pie = de_pie

    def get_precio_total(self):
        return super().get_precio_total() * 1.10

    def __str__(self):
        return f'Entrada de pista para {self.concierto.artista} - {self.get_precio_total()} €'


class EntradaVIP(Entrada):
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    def get_precio_total(self):
        if self.incluye_consumicion:
            return super().get_precio_total() * 1.20
        else:
            return super().get_precio_total() * 1.15

    def __str__(self):
        return f'Entrada VIP para {self.concierto.artista} - {self.get_precio_total()} €'


class Concierto:
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, entradas_vendidas, activo):
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = precio_base
        self.aforo_maximo = aforo_maximo
        self.entradas_vendidas = entradas_vendidas
        self.activo = activo

    def calcular_recaudacion(self):
        