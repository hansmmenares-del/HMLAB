info_doctores = []
## Menu_1 == Hacer cuenta.
def menu_general():
    while True:
        try:
            opc=int(input("(1) HACER CUENTA\n(2) DOCTORES\n(3) MODIFICAR TRABAJO\n(0) SALIR\n"))
        except ValueError:
            print("Inválido. Seleccione una opcion válida dentro del rango (1, 2 o 3)\nSi desea salir '0'")
        else:
            if opc < 0 or opc > 3:
                print("Inválido. Seleccione una opcion válida dentro del rango (1, 2 o 3)\nSi desea salir '0'")
            else:
                if opc == 0:
                    break
                elif opc == 1:
                    menu_1()
                elif opc == 2:
                    menu_2()
                elif opc == 3:
                    menu_3()
def menu_1():
    while True:
        try:
            tipo_producto = int(input("¿Qué producto? ('0' para terminar):\n"))
        except ValueError:
            print("Inválido! Debes ingresar el número de un producto.")
        else:
            if tipo_producto == 0:
                break
            elif tipo_producto >= 1:
                pass
    return tipo_producto
def menu_2():
    while True:
        try:
            opc = int(input("(1) NUEVO DOCTOR\n(2) MODIFICAR DOCTOR\n(3) VER LISTA DOCTORES\n(0) VOLVER\n"))
        except ValueError:
            print("Inválido. Si desea salir '0'")
        else:
            if opc < 0 or opc > 3:
                print("Inválido. Seleccione una opcion válida dentro del rango (1, 2 o 3)\nSi desea volver al menú principal '0'")
            elif opc == 0:
                break
            elif opc == 1:
                menu_2_1()
            elif opc == 2:
                menu_2_2()
            elif opc == 3:
                menu_2_3()
def menu_2_1():
    nombre_uncheck = True
    while nombre_uncheck:
        nombre = input("Ingresa el nombre del Dr(a): ").strip().capitalize()
        if nombre == "":
            print("El nombre no puede estar vacío")
        elif len(nombre) < 3:
            print("El nombre es muy corto")
        elif not nombre.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras.")
        elif nombre in info_doctores:
            print("Este doctor ya existe!")
            while True:
                try:
                    opc = int(input("(1) Agregar de todos modos\n(0) Volver al menú principal\n"))
                except ValueError:
                    print("Inválido! Ingresa 1 o 0")
                else:
                    if opc < 0 or opc > 1:
                        print("Inválido! Ingresa 1 o 0")
                    elif opc == 0 or opc == 1:
                        break
            if opc == 0:
                break
        for i in nombre:
            if i.isdigit():
                print("El nombre no puede contener números")
                break
            else:
                nombre_uncheck = False
    apellidos_uncheck = True
    while apellidos_uncheck:        
        apellidos = input("Ingresa los apellidos del dr: ").strip().title()
        if apellidos == "":
            print("El apellidos no puede estar vacío")
        elif len(apellidos) < 3:
            while True:
                try:
                    retry_name = int(input("El apellidos es muy corto\n(1) Continuar de todas maneras.\n(2) Ingresar de nuevo los apellidos.\n"))
                except ValueError:
                    print("Inválido! Ingresa 1 o 2\n")
                else:
                    if retry_name < 1 or retry_name > 2:
                        print("Inválido! Ingresa 1 o 2\n")
                    else:
                        if retry_name == 1 or retry_name == 2:
                            break
            if retry_name ==2:
                continue
        elif not apellidos.replace(" ","").isalpha():
            print("El apellido solo puede contener letras.")
        for i in apellidos:
            if i.isdigit():
                print("El apellido no puede contener números")
                break
            else:
                apellidos_uncheck = False    
    contacto_check = True
    while contacto_check:
        try:
            contacto = int(input("Ingresa el número de contacto: +56"))
        except ValueError:
            print("Número inválido! Debes ingresar los digitos desde el 9 en adelante (ej: 93212345)")
        else:
            if len(str(contacto)) != 9 :
                print("Número inválido! Debes ingresar los digitos desde le 9 en adelante (ej: 93212345)")
            elif str(contacto)[0] != 9:
                print("Número inválido! Debes ingresar los digitos desde le 9 en adelante (ej: 93212345)")
            else:
                contacto_check = False
    direccion_uncheck = True
    while direccion_uncheck:
        try:
            direccion = int(input("Ingresa la direccion:\n"))
        except ValueError:
            print("")
        else:
            if direccion:
                pass
            else:
                direccion_uncheck = False
    tipo_empresa_uncheck = True
    while tipo_empresa_uncheck:
        try:    
            tipo_empresa = int(input("Ingresa la tipo_empresa:\n"))
        except ValueError:
            print("")
        else:
            if tipo_empresa:
                pass
            else:
                tipo_empresa_uncheck = False
    rut_empresa_uncheck = True
    while rut_empresa_uncheck:
        try:    
            rut_empresa = int(input("Ingresa la rut_empresa:\n"))
        except ValueError:
            print("")
        else:
            if rut_empresa:
                pass
            else:
                rut_empresa_uncheck = False
    giro_uncheck = True
    while giro_uncheck:
        try:    
            giro = int(input("Ingresa la giro:\n"))
        except ValueError:
            print("")
        else:
            if giro:
                pass
            else:
                giro_uncheck = False
    correo_uncheck = True
    while correo_uncheck:
        try:    
            correo = int(input("Ingresa la correo:\n"))
        except ValueError:
            print("")
        else:
            if correo:
                pass
            else:
                correo_uncheck = False
    comuna_uncheck = True
    while comuna_uncheck:
        try:    
            comuna = int(input("Ingresa la comuna:\n"))
        except ValueError:
            print("")
        else:
            if comuna:
                pass
            else:
                comuna_uncheck = False
    dic_doc_uncheck = True
    while dic_doc_uncheck:
        try:    
            dic_doc = int(input("Ingresa la dic_doc:\n"))
        except ValueError:
            print("")
        else:
            if dic_doc:
                pass
            else:
                dic_doc_uncheck = False
    return nombre, apellidos, contacto, direccion, direccion, tipo_empresa, rut_empresa, giro, correo, comuna, dic_doc
def menu_2_2():
    pass
def menu_2_3():
    pass
def menu_3():
    pass