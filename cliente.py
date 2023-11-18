from persona import Persona

class Cliente(Persona):
  def __init__(self, dni=None, nombre=None, apellido=None, domicilio=None, nro_cliente=None):
    if dni is not None and nombre is not None and apellido is not None and domicilio is not None and apellido is not None and nro_cliente is not None:
      super().__init__(dni, nombre, apellido, domicilio)
      self.nro_cliente = nro_cliente
      self.cuotas_pagadas = 0  # Nuevo atributo para llevar registro de cuotas pagadas

  def registrar_pago_cuota(self):
    if self.cuotas_pagadas < 8:  # Verificar que el cliente no haya pagado todas las cuotas
      self.cuotas_pagadas += 1
      print(f"Se registró el pago de la cuota {self.cuotas_pagadas}.")
    if self.cuotas_pagadas == 8:  # Si se completan las 8 cuotas, gestionar adjudicación
      self.gestionar_adjudicacion()

  def gestionar_adjudicacion(self):
    print("¡Felicidades! Usted ha completado el pago de todas las cuotas.")
    print("Seleccione el método de adjudicación:")
    print("1. Sorteo mensual")
    print("2. Pago completo de cuotas")
    print("3. Licitación")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
      if self.sorteo_mensual():
        print("¡Felicidades! Usted ha sido adjudicado por sorteo.")
        self.registrar_pago_cuota()  # Registrar el pago de una cuota
      else:
        print("Lo sentimos, no fue seleccionado en el sorteo.")
    elif opcion == '2':
      self.pago_completo_cuotas()
    elif opcion == '3':
      self.licitacion()
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")