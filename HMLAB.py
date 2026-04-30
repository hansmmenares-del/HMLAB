import os
import json

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
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Campo obligatorio. Intenta nuevamente.")
        else:
            return texto

nohayarroba=True
main_is_running=True
lista_docs=cargar_datos()

while main_is_running:
    try:
        opc=int(input("(1) HACER CUENTA\n(2) DOCTORES\n(3) MODIFICAR TRABAJO\n(0) SALIR\n"))
    except ValueError:
        print("Inválido. Si desea salir '0'")
    else:
        clear()
        if opc==0:
            main_is_running=False
        elif opc==2:
            menu_2_is_running=True
            while menu_2_is_running==True:
                try:
                    menu_2=int(input("(1) NUEVO DOCTOR\n(2) MODIFICAR DOCTOR\n(3) VER LISTA DOCTORES\n(0) VOLVER\n"))
                except ValueError:
                    print("Inválido. Si desea salir '0'")
                else:
                    clear()
                    if menu_2==1:
                        print("--- A continuacion deberá ingresar los datos del dr ---")
                        nombre=pedir_texto("Ingresa el nombre del dr: ")
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
                        menu_2_is_running=False
                        
                        