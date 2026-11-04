class Alojamiento:
    def __init__(self, nombre, precio_por_noche, ciudad):
        self.nombre = nombre
        self.precio_por_noche = precio_por_noche
        self.ciudad = ciudad

    def calcular_precio(self, noches):
        return self.precio_por_noche * noches

    def __str__(self):
        return f'{self.nombre}, en {self.ciudad}'

class Hotel(Alojamineto):
    def __init__(self,nombre, precio_por_noche, ciudad, estrellas, desayuno_incluido):
        super().__init__(nombre, precio_por_noche, ciudad)
        self.estrellas = estrellas
        self.desayuno_incluido = desayuno_incluido

    def __str__ (self):
        return f'{self.nombre}, en {self.ciudad} (hotel de {self.estrellas} estrellas)'

class Camping(Alojamiento):
    def __init__(self, nombre, precio_por_noche, ciudad, num_caravanas, capacidad_caravanas, tiene_piscina):
        super().__init__(nombre, precio_por_noche, ciudad)
        self.num_caravanas = num_caravanas
        self.capacidad_caravanas = capacidad_caravanas
        self.tiene_psicina = tiene_piscina
