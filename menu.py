from cliente import Cliente
from vehiculo import Vehiculo
from grupo import Grupo

lista_personas = []
lista_vehiculos = []

def mostrar_menu():
  print("¡Bienvenido al Plan de Ahorro de Autos!")
  print("Por favor, seleccione una opción:")
  print("a. Gestionar Clientes")
  print("b. Gestionar Grupos de Clientes")
  print("c. Agregar pago de cuotas de los clientes")
  print("d. Registrar una adjudicación")
  print("e. Gestionar vehículos")
  print("q. Salir")


def limpiar_pantalla():
  os.system('clear' if os.name == 'posix' else 'cls')


def gestionar_clientes(lista_personas):
  print("Gestionando Clientes...")
  dni = input("Ingrese DNI del cliente: ")
  nombre = input("Ingrese nombre del cliente: ")
  apellido = input("Ingrese apellido del cliente: ")
  domicilio = input("Ingrese domicilio del cliente: ")
  nro_cliente = input("Ingrese número de cliente: ")

  cliente = Cliente(dni, nombre, apellido, domicilio, nro_cliente)
  cliente.agregar_persona(lista_personas)

  print("Cliente agregado con éxito.")


def gestionar_grupos():
  print("Gestionando Grupos de Clientes...")
  # Implementar lógica para gestionar grupos
  pass


def agregar_pago_cuotas():
  print("Agregando pago de cuotas de los clientes...")
  # Implementar lógica para agregar pagos de cuotas
  pass


def registrar_adjudicacion():
  print("Registrando una adjudicación...")
  # Implementar lógica para registrar una adjudicación
  pass


def gestionar_vehiculos():
  print("Gestionando vehículos...")
  # Implementar lógica para gestionar vehículos
  pass


while True:
  #limpiar_pantalla()
  mostrar_menu()
  opcion = input("Seleccione una opción: ").lower()

  if opcion == 'a':
    gestionar_clientes(lista_personas)
  elif opcion == 'b':
    gestionar_grupos()
  elif opcion == 'c':
    agregar_pago_cuotas()
  elif opcion == 'd':
    registrar_adjudicacion()
  elif opcion == 'e':
    gestionar_vehiculos()
  elif opcion == 'q':
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")



def menu_gestionar_clientes():
    print("\n--- Menú Gestionar Clientes ---")
    print("a. Agregar Cliente")
    print("b. Modificar Cliente")
    print("c. Eliminar Cliente")
    print("d. Mostrar Clientes")
    print("e. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion

def menu_gestionar_grupos():
    print("\n--- Menú Gestionar Grupos de Clientes ---")
    print("a. Agregar Grupo")
    print("b. Modificar Grupo")
    print("c. Eliminar Grupo")
    print("d. Agregar Cliente a Grupo")
    print("e. Listar Grupos")
    print("f. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion

def menu_gestionar_autos():
    print("\n--- Menú Gestionar Autos ---")
    print("a. Agregar Auto")
    print("b. Eliminar Auto")
    print("c. Listar Autos")
    print("d. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion


#menu principal
def main():
  gestion_clientes = Cliente()
  gestion_grupos = Grupo()
  gestion_autos = Vehiculo()

  while True:
    print("\n--- Menú Principal ---")
    print("1. Gestionar Clientes")
    print("2. Gestionar Grupos de Clientes")
    print("3. Gestionar Autos")
    print("4. Salir")

    opcion_principal = input("Seleccione una opción: ")

    if opcion_principal == '1':
      while True:
        opcion_gestion_clientes = menu_gestionar_clientes()

        if opcion_gestion_clientes == 'a':
          # Agregar Cliente
          dni = input("Ingrese DNI del cliente: ")
          nombre = input("Ingrese el nombre del cliente: ")
          apellido = input("Ingrese el apellido del cliente: ")
          domicilio = input("Ingrese domicilio del cliente: ")
          nro_cliente = input("Ingrese número de cliente: ")
          gestion_clientes.agregarCliente(dni, nombre, apellido, dni, domicilio, nro_cliente)

        elif opcion_gestion_clientes == 'b':
          # Modificar Cliente
          dni = input("Ingrese el DNI del cliente a modificar: ")
          nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
          nuevo_apellido = input("Ingrese el nuevo apellido del cliente: ")
          cliente = gestion_clientes.encontrar_cliente_por_dni(dni)
          if cliente:
            cliente.modificarCliente(nuevo_nombre, nuevo_apellido)
          else:
            print("Cliente no encontrado.")

        elif opcion_gestion_clientes == 'c':
          # Eliminar Cliente
          dni = input("Ingrese el DNI del cliente a eliminar: ")
          gestion_clientes.eliminarCliente(dni)

        elif opcion_gestion_clientes == 'd':
          # Mostrar Clientes
          gestion_clientes.mostrarClientes()

        elif opcion_gestion_clientes == 'e':
          # Volver al Menú Principal
          break

        else:
          print("Opción inválida. Intente nuevamente.")

    elif opcion_principal == '2':
      while True:
        opcion_gestion_grupos = menu_gestionar_grupos()

        if opcion_gestion_grupos == 'a':
          # Agregar Grupo
          id_grupo = input("Ingrese el ID del grupo: ")
          nombre_grupo = input("Ingrese el nombre del grupo: ")
          id_auto_grupo = input("Ingrese el id del auto que será del grupo: ")
          auto_grupo = gestion_autos.agregarAuto(marca_auto, modelo_auto, anio_auto, precio_auto)
          gestion_grupos.agregar_grupo(auto_grupo)

        elif opcion_gestion_grupos == 'b':
          # Modificar Grupo
          id_grupo = input("Ingrese el ID del grupo a modificar: ")
          marca_auto = input("Ingrese la nueva marca del auto del grupo: ")
          auto_grupo = gestion_autos.agregarAuto(marca_auto, modelo_auto, anio_auto, precio_auto)
          gestion_grupos.modificar_grupo(id_grupo, auto_grupo)

        elif opcion_gestion_grupos == 'c':
          # Eliminar Grupo
          id_grupo = input("Ingrese el ID del grupo a eliminar: ")
          gestion_grupos.eliminar_grupo(id_grupo)

        elif opcion_gestion_grupos == 'd':
          # Agregar Cliente a Grupo
          id_grupo = input("Ingrese el ID del grupo al que desea agregar un cliente: ")
          dni_cliente = input("Ingrese el DNI del cliente a agregar: ")
          cliente_a_agregar = gestion_clientes.encontrar_cliente_por_dni(dni_cliente)
          if cliente_a_agregar:
            gestion_grupos.agregarCliente_a_grupo(id_grupo, cliente_a_agregar)
          else:
            print("Cliente no encontrado.")

        elif opcion_gestion_grupos == 'e':
          # Listar Grupos
          gestion_grupos.listar_grupos()

        elif opcion_gestion_grupos == 'f':
          # Volver al Menú Principal
          break

        else:
          print("Opción inválida. Intente nuevamente.")

    elif opcion_principal == '3':
      while True:
        opcion_gestion_autos = menu_gestionar_autos()

        if opcion_gestion_autos == 'a':
          # Agregar Auto
          marca = input("Ingrese la marca del vehículo: ")
          modelo = input("Ingrese el modelo del vehículo: ")
          color = input("Ingrese el color del vehículo: ")
          cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
          cant_pasajeros = int(input("Ingrese la cantidad de pasajeros del vehículo: "))
          precio = int(input("Ingrese el precio del vehículo: "))
          gestion_autos.agregar_vehiculo()

        elif opcion_gestion_autos == 'b':
          # Eliminar Auto
          marca_auto = input("Ingrese la marca del auto a eliminar: ")
          modelo_auto = input("Ingrese el modelo del auto a eliminar: ")
          gestion_autos.eliminarAuto(marca_auto, modelo_auto)

        elif opcion_gestion_autos == 'c':
          # Listar Autos
          gestion_autos.listarAutos()

        elif opcion_gestion_autos == 'd':
          # Volver al Menú Principal
          break

        else:
          print("Opción inválida. Intente nuevamente.")

    elif opcion_principal == '4':
      # Salir
      print("¡Hasta luego!")
      break

    else:
      print("Opción inválida. Intente nuevamente.")