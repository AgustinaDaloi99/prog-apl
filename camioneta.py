from vehiculo import Vehiculo

class Camioneta(Vehiculo):

  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
    cant_pasajeros, carga, tolva):
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas, cant_pasajeros)
    self.carga = carga
    self.tolva = tolva

  def cargar(self, carga):
    # Implementar la lógica para cargar la camioneta
    pass