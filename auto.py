from vehiculo import Vehiculo

class Auto(Vehiculo):

  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas, cant_pasajeros, tipo):
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas, cant_pasajeros)
    self.tipo = tipo