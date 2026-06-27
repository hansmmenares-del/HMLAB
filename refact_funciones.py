# git pull origin main
# git add .
# git commit -m "..."
# git push
lista_info_doctores = []
lista_pacientes_historial = []
lista_trabajos = []
#dic_trabajo = {
#   "nombre_trabajo": nombre_trabajo,
#   "tipo_trabajo": tipo_trabajo,
#   "piezas": piezas,
#   "color": color,
#   "monto": monto,
# }
#dic_paciente = {
#   "nombre1": nombre1,
#    "nombre2": nombre2,
#    "apellido1": apellido1,
#    "apellido2": apellido2,
#    "clinica_atencion": clinica_atencion,
#    "nombre_doctor": nombre_doctor,
#    "trabajos_realizados": trabajos_realizados,
#}

def validar_int(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: int, lim_sup: int) -> int:
    while True:
        try:
            num = int(input(f"{msg_input}"))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! El valor debe estar entre {lim_inf} y {lim_sup}")
                    continue
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! El valor debe ser mayor que {lim_inf}")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! El valor debe ser menor que {lim_sup}")
                    continue
            return num
def validar_float(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: float, lim_sup: float) -> float:
    while True:
        try:
            num = float(input(f"{msg_input}"))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! El valor debe estar entre {lim_inf} y {lim_sup}")
                    continue
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! El valor debe ser mayor que {lim_inf}")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! El valor debe ser menor que {lim_sup}")
                    continue
            return num
def validar_str(msg_input: str, hay_digitos: bool, es_correo: bool) -> str|int|None:
    while True:
        errores = False
        texto_a_validar = input(msg_input).strip().title()
        if hay_digitos:
            return texto_a_validar
        elif not hay_digitos:
            if texto_a_validar == "":
                print("Inválido! Este campo no puede estar vacío")
                continue
            for i in texto_a_validar:
                if i.isdigit():
                    print("Inválido! Este campo no puede contener dígitos")
                    errores = True
                    break
        if es_correo:
            if "@" not in texto_a_validar:
                print("Inválido! Este campo debe contener un correo electrónico")
                errores = True
        if errores:
            continue
        return texto_a_validar
def confirmar_accion(msg_input: str) -> bool:
    while True:
        confirmar = input(f"{msg_input}¿Confirmar? (s/n): ").strip().lower()
        if confirmar == "s":
            return True
        elif confirmar == "n":
            return False
        else:
            print("Inválido! Debes ingresar 's' para sí o 'n' para no")
def agregar_doctor():
    print("--- AGREGAR DOCTOR ---\nA continuacion deberás ingresar la información del doctor.\n")
    while True:
        nombre1 = validar_str("Ingresa el primer nombre del doctor: ", False, False)
        if not confirmar_accion(f"\nNombre 1: {nombre1}\n"):
            print("Acción cancelada. No se ha agregado el doctor.")
            return
        nombre2 = validar_str("Ingresa el segundo nombre del doctor: ", False, False)
        apellido1 = validar_str("Ingresa el apellido1: ", False, False)
        apellido2 = validar_str("Ingresa el apellido2: ", False, False)
        nombre_clinica = validar_str("Ingresa el nombre_clinica: ", False, False)
        direccion_clinica = validar_str("Ingresa el direccion_clinica: ", False, False)
        telefono = validar_str("Ingresa el telefono: ", False, False)
        email = validar_str("Ingresa el email: ", False, False)
        rut_empresa = validar_str("Ingresa el rut_empresa: ", False, False)
        direccion_empresa = validar_str("Ingresa el direccion_empresa: ", False, False)
        giro = validar_str("Ingresa el giro: ", False, False)
        comuna = validar_str("Ingresa el comuna: ", False, False)
        
        dic_doctor = {
        "nombre1": nombre1,
        "nombre2": nombre2,
        "apellido1": apellido1,
        "apellido2": apellido2,
        "nombre_clinica": nombre_clinica,
        "direccion_clinica": direccion_clinica,
        "telefono": telefono,
        "email": email,
        "rut_empresa": rut_empresa,
        "direccion_empresa": direccion_empresa,
        "giro": giro,
        "comuna": comuna,
    }    
def modificar_doctor():
    pass
def eliminar_doctor():
    pass
def ver_lista_doctores():
    pass
def buscar_doctor():
    pass
def menu_1_cuentas() -> None:
    pass
def menu_2_doctores() -> None:
    while True:
        opc = validar_int("--- DOCTORES ---\n(1) AGREGAR DOCTOR\n(2) MODIFICAR DOCTOR\n(3) ELIMINAR DOCTOR\n(4) VER LISTA DOCTORES\n(5) BUSCAR DOCTOR\n(0) VOLVER\n", 0, 5, True, True)
        if opc == 1:
            agregar_doctor()
        elif opc == 2:
            modificar_doctor()
        elif opc == 3:
            eliminar_doctor()
        elif opc == 4:
            ver_lista_doctores()
        elif opc == 5:
            buscar_doctor()
        elif opc == 0:
            break
def 
def menu_3_trabajos_submenu_añadir_trabajo() -> None:
    print("--- AÑADIR TRABAJO ---\nA continuación deberás ingresar la información del trabajo.\n")
    while True:
        nombre_trabajo = validar_str("Ingresa el nombre del trabajo: ", False, False)
        tipo_trabajo = validar_str("Ingresa el tipo de trabajo: ", False, False)
        monto = validar_float("Ingresa el monto del trabajo: ", True, True, 0.01, 1000000.00)
        dic_trabajo_añadir = {
            "nombre_trabajo": nombre_trabajo,
            "tipo_trabajo": tipo_trabajo,
            "monto": monto,
        }
        if confirmar_accion(f"\nNombre del trabajo: {nombre_trabajo}\nTipo de trabajo: {tipo_trabajo}\nMonto: {monto}\n"):
            lista_trabajos.append(dic_trabajo_añadir)
            print("Trabajo agregado exitosamente.")
            break
        else:
            print("Acción cancelada. No se ha agregado el trabajo.")
def menu_3_trabajos_submenu_modificar_trabajo() -> None:
    print("--- MODIFICAR TRABAJO ---\nA continuación deberás ingresar la información del trabajo a modificar.\n")
    while True:
        nombre_trabajo = validar_str("Ingresa el nombre del trabajo a modificar: ", False, False)
        # Buscar el trabajo en la lista
        trabajo_encontrado = None
        for trabajo in lista_trabajos:
            if trabajo["nombre_trabajo"].lower() == nombre_trabajo.lower():
                trabajo_encontrado = trabajo
                break
        if trabajo_encontrado is None:
            print("Trabajo no encontrado. Intenta nuevamente.")
            continue
        # Mostrar información actual del trabajo
        print(f"\nInformación actual del trabajo:\nNombre: {trabajo_encontrado['nombre_trabajo']}\nTipo: {trabajo_encontrado['tipo_trabajo']}\nMonto: {trabajo_encontrado['monto']}\n")
        # Solicitar nueva información
        nuevo_nombre = validar_str("Ingresa el nuevo nombre del trabajo (dejar vacío para no cambiar): ", False, False)
        nuevo_tipo = validar_str("Ingresa el nuevo tipo de trabajo (dejar vacío para no cambiar): ", False, False)
        nuevo_monto = input("Ingresa el nuevo monto del trabajo (dejar vacío para no cambiar): ").strip()
        if nuevo_monto:
            try:
                nuevo_monto = float(nuevo_monto)
                if nuevo_monto <= 0:
                    print("Monto inválido. Debe ser mayor que 0.")
                    continue
            except ValueError:
                print("Monto inválido. Debe ser un número.")
                continue
        # Confirmar cambios
        if confirmar_accion("¿Deseas guardar los cambios?"):
            if nuevo_nombre:
                trabajo_encontrado["nombre_trabajo"] = nuevo_nombre
            if nuevo_tipo:
                trabajo_encontrado["tipo_trabajo"] = nuevo_tipo
            if nuevo_monto:
                trabajo_encontrado["monto"] = nuevo_monto
            print("Trabajo modificado exitosamente.")
            break
        else:
            print("Acción cancelada. No se han realizado cambios.")
def menu_3_trabajos() -> None:
    #Añadir tipo de trabajo
    #Modificar trabajo
    #Eliminar trabajo
    #Ver lista de trabajos
    while True:
        opc = validar_int("--- TRABAJOS ---\n(1) AÑADIR TRABAJO\n(2) MODIFICAR TRABAJO\n(3) ELIMINAR TRABAJO\n(4) VER LISTA DE TRABAJOS\n(0) VOLVER\n", True, True, 1, 0)
        if opc == 1:
            menu_3_trabajos_submenu_añadir_trabajo()
        elif opc == 2:
            menu_3_trabajos_submenu_modificar_trabajo()
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 0:
            break

def menu() -> None:
    while True:
        opc = validar_int("==== MENU PRINCIPAL ====\n(1) CUENTAS\n(2) DOCTORES\n(3) TRABAJOS\n(0) SALIR\n", True, True, 0, 3)
        if opc == 1:
            menu_1_cuentas()
        elif opc == 2:
            menu_2_doctores()
        elif opc == 3:
            menu_3_trabajos()
        elif opc == 0:
            break
menu()