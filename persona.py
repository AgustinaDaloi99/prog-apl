class Persona:
  def __init__(self, dni, nombre, apellido, domicilio):
    self._dni = dni
    self._nombre = nombre
    self._apellido = apellido
    self._domicilio = domicilio
  
  @property
  def dni(self):
    return self._dni
  
  @dni.setter
  def dni(self, nuevo_dni):
    self._dni = nuevo_dni

  @property
  def nombre(self):
    return self._nombre
  
  @nombre.setter
  def nombre(self, nuevo_nombre):
    self._nombre = nuevo_nombre

  @property
  def apellido(self):
    return self._apellido
  
  @apellido.setter
  def apellido(self, nuevo_apellido):
    self._apellido = nuevo_apellido
  
  @property
  def domicilio(self):
    return self._domicilio
  
  @domicilio.setter
  def domicilio(self, nuevo_domicilio):
    self._domicilio =nuevo_domicilio

  def agregar_persona(self, lista_personas):
    lista_personas.append(self)

  def modificar_persona(self, atributo, nuevo_valor):
    if atributo == 'dni':
      self.dni = nuevo_valor
    elif atributo == 'nombre':
      self.nombre = nuevo_valor
    elif atributo == 'apellido':
      self.apellido = nuevo_valor
    elif atributo == 'domicilio':
      self.domicilio = nuevo_valor
    else:
      print(
        "Atributo no válido. Los atributos válidos son: dni, nombre, apellido, domicilio"
      )

  def eliminar_persona(self, lista_personas):
    dni_eliminar = input("Ingrese el DNI de la persona que desea eliminar: ")

    # Buscar la persona por su DNI en la lista
    persona_encontrada = None
    for persona in lista_personas:
      if persona.dni == dni_eliminar:
        persona_encontrada = persona
        break

    if persona_encontrada:
      confirmacion = input(
          f"¿Está seguro de eliminar a {persona_encontrada.nombre} {persona_encontrada.apellido}? (s/n): "
      )
      if confirmacion.lower() == 's':
        lista_personas.remove(persona_encontrada)
        print(
            f"La persona {persona_encontrada.nombre} {persona_encontrada.apellido} ha sido eliminada."
        )
      else:
        print("Operación cancelada.")
    else:
      print(f"No se encontró ninguna persona con DNI {dni_eliminar}.")
  
  def mostrarPersonas(self, lista_personas):
    for persona in lista_personas:
      print(f"nombre: {persona.nombre} apellido: {persona.apellido} dni: {persona.dni}")

