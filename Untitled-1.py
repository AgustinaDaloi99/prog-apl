def main():
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
                    gestion_clientes.agregarCliente(dni, nombre, apellido, dni)

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
                    marca_auto = input("Ingrese la marca del auto del grupo: ")
                    modelo_auto = input("Ingrese el modelo del auto del grupo: ")
                    anio_auto = input("Ingrese el año del auto del grupo: ")
                    precio_auto = input("Ingrese el precio del auto del grupo: ")
                    auto_grupo = gestion_autos.agregarAuto(marca_auto, modelo_auto, anio_auto, precio_auto)
                    gestion_grupos.agregar_grupo(auto_grupo)

                elif opcion_gestion_grupos == 'b':
                    # Modificar Grupo
                    id_grupo = input("Ingrese el ID del grupo a modificar: ")
                    marca_auto = input("Ingrese la nueva marca del auto del grupo: ")
                    modelo_auto = input("Ingrese el nuevo modelo del auto del grupo: ")
                    anio_auto = input("Ingrese el nuevo año del auto del grupo: ")
                    precio_auto = input("Ingrese el nuevo precio del auto del grupo: ")
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
                    marca_auto = input("Ingrese la marca del auto: ")
                    modelo_auto = input("Ingrese el modelo del auto: ")
                    anio_auto = input("Ingrese el año del auto: ")
                    precio_auto = input("Ingrese el precio del auto: ")
                    gestion_autos.agregarAuto(marca_auto, modelo_auto, anio_auto, precio_auto)

                elif opcion_gestion_autos == 'b':
                    # Modificar Auto
                    marca_auto = input("Ingrese la marca del auto a modificar: ")
                    modelo_auto = input("Ingrese el modelo del auto a modificar: ")
                    auto_a_modificar = gestion_autos.encontrar_auto_por_marca_y_modelo(marca_auto, modelo_auto)
                    if auto_a_modificar:
                        nueva_marca_auto = input("Ingrese la nueva marca del auto: ")
                        nuevo_modelo_auto = input("Ingrese el nuevo modelo del auto: ")
                        nuevo_anio_auto = input("Ingrese el nuevo año del auto: ")
                        nuevo_precio_auto = input("Ingrese el nuevo precio del auto: ")
                        auto_a_modificar.modificarAuto(nueva_marca_auto, nuevo_modelo_auto, nuevo_anio_auto, nuevo_precio_auto)
                    else:
                        print("Auto no encontrado.")

                elif opcion_gestion_autos == 'c':
                    # Eliminar Auto
                    marca_auto = input("Ingrese la marca del auto a eliminar: ")
                    modelo_auto = input("Ingrese el modelo del auto a eliminar: ")
                    gestion_autos.eliminarAuto(marca_auto, modelo_auto)

                elif opcion_gestion_autos == 'd':
                    # Listar Autos
                    gestion_autos.listarAutos()

                elif opcion_gestion_autos == 'e':
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