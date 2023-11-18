class Grupo:
  def __init__(self, nro_grupo, fecha_inicio, fecha_cierre):
    self.nro_grupo = nro_grupo
    self.fecha_inicio = fecha_inicio
    self.fecha_cierre = fecha_cierre
    self.clientes = []
    self.vehiculos = []

  def agregar_cliente(self, cliente):
    if len(self.clientes) < 5:
        self.clientes.append(cliente)
    else:
        print("No se puede agregar más clientes a este grupo. Límite alcanzado.")

  def agregar_vehiculo(self, vehiculo):
    self.vehiculos.append(vehiculo)

  def modificar_grupo(self):
    # Implementar la lógica para modificar un grupo
    pass

  def cerrar_grupo(self):
    # Implementar la lógica para cerrar un grupo
    pass
