import os
import json
# FUNCIONES GENERALES
def guardar_datos(lista):
    with open("data/doctores.json", "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
def cargar_datos():
    if os.path.exists("data/doctores.json"):
        with open("data/doctores.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []
if not os.path.exists("data"):
    os.mkdir("data")
def clear():
    os.system("cls")
    
trabajos = []
while True:
        try:
            opc=int(input("(1) HACER CUENTA\n(2) DOCTORES\n(3) MODIFICAR TRABAJO\n(0) SALIR\n"))
        except ValueError:
            print("Inválido. Seleccione una opcion válida dentro del rango (1, 2 o 3)\nSi desea salir '0'") #error
        else:
            if opc < 0 or opc > 3:
                clear()
                print("Inválido. Seleccione una opcion válida dentro del rango (1, 2 o 3)\nSi desea salir '0'") #error
            else:
                if opc == 0:
                    break
                elif opc == 1:
                    while True:
                        ## Ir seleccionando de lista, preguntar doc/clinica, pedir tipo de trabajo, cantidad, sumar, guardar, salir al menu principal o emitir cuenta.
                        try:
                            tipo_producto = int(input("¿Qué producto? ('0' para terminar):\n"))
                        except ValueError:
                            print("Inválido! Debes ingresar el número de un producto.")
                        else:
                            if tipo_producto == 0:
                                break
                            elif tipo_producto >= 1: ########## condicional para preguntar cantidad¿?
                                pass
                elif opc == 2:
                    while True:
                        try:
                            menu_2=int(input("(1) NUEVO DOCTOR\n(2) MODIFICAR DOCTOR\n(3) VER LISTA DOCTORES\n(0) VOLVER\n"))
                        except ValueError:
                            print("Inválido. Si desea salir '0'") #error
                        else:
                            clear()
                            if menu_2 < 0 or menu_2 > 3:
                                print("Inválido. Seleccione una opcion válida dentro del rango (1, 2 o 3)\nSi desea salir '0'") #error
                            elif menu_2 == 1:
                                print("--- A continuacion deberá ingresar los datos del dr ---")
                                nombre_check = True
                                while nombre_check:
                                    nombre = input("Ingresa el nombre del Dr(a): ").strip().capitalize()
                                    if nombre == "":
                                        print("El nombre no puede estar vacío")
                                    elif len(nombre) < 3:
                                        print("El nombre es demasiado corto") #error
                                        while True:
                                            try:
                                                retry_name = int(input("El nombre es muy corto\n(1) Continuar de todas maneras.\n(2) Ingresar de nuevo el nombre.\n"))
                                            except ValueError:
                                                print("Inválido! Ingresa 1 o 2\n")
                                            else:
                                                if retry_name < 1 or retry_name > 2:
                                                    print("Inválido! Ingresa 1 o 2\n")
                                                else:
                                                    if retry_name == 1:
                                                        break
                                                    elif retry_name == 2:
                                                        continue
                                    elif not nombre.replace(" ", "").isalpha():
                                        print("El nombre solo puede contener letras.") #error
                                    for i in nombre:
                                        if i.isdigit():
                                            print("El nombre no puede contener números") #error
                                            break
                                        else:
                                            nombre_check = False
                                
                                                                
                                apellido=pedir_texto("Ingresa el apellido del dr: ")
                                contacto=pedir_texto("Ingresa el número de contacto: +56")
                                direccion=pedir_texto("Ingresa direccion: ")
                                tipo_empresa=pedir_texto("Ingresa tipo de empresa: ")
                                rut_empresa=pedir_texto("Ingresa rut de empresa: ")
                                giro=pedir_texto("Ingresa giro: ")
                                correo=pedir_texto("Ingresa correo electronico: ")
                                comuna=pedir_texto("Ingresa la comuna: ")
                                dic_doc = {
                                    "nombre": nombre, "apellido": apellido, "contacto": contacto, "direccion":direccion, "tipo_empresa": tipo_empresa, "rut_empresa": rut_empresa, "giro": giro, "correo": correo, "comuna": comuna
                                    }
                                lista_docs.append(dic_doc)
                                guardar_datos(lista_docs)
                            elif menu_2==2:
                                pass
                            elif menu_2==3:
                                pass
                            elif menu_2==0:    
                                break
                elif opc == 3:
                    pass