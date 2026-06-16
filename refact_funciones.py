# git pull origin main
# git add .
# git commit -m "..."
# git push
garantia = True
opc = 0
texto = ""
num = 0
cantidad = 0
lista_info_docs_para_facturas = []
lista_pacientes_historial = []
lista_trabajos = []
dic_trabajos = {
    "nombre_trabajo": lista_trabajos[opc],
    "piezas": cantidad,
    "color": texto,
    "monto": num,
    "cantidad": cantidad,
}
dic_paciente = {
    "nombre1": texto,
    "nombre2": texto,
    "apellido1": texto,
    "apellido2": texto,
    "clinica_atencion": texto,
    "nombre_doctor": texto,
    "trabajos_realizados": [],
}
dic_doctor = {
    "nombre1": texto,
    "nombre2": texto,
    "apellido1": texto,
    "apellido2": texto,
    "nombre_clinica": texto,
    "direccion_clinica": texto,
    "telefono": texto,
    "email": texto,
    "rut_empresa": num,
    "direccion_empresa": texto,
    "giro": texto,
    "comuna": texto,
}
lim_inf, lim_sup = 0, 0
mensajes_de_error = [
    "Inválido! ingresar un número",
    f"Inválido! Los limites de opciones van de {lim_inf} a {lim_sup}",
    f"Inválido! Los rangos aceptables son de {lim_inf} a {lim_sup}",
    "Inválido! El texto no debe contener dígitos",
]


def validar_int(
    msg_input: str, lim_inf: int, lim_sup: int, hay_lim_inf: bool, hay_lim_sup: bool
) -> int:
    while True:
        errores = False
        try:
            num = int(input(f"{msg_input}"))
        except ValueError:
            print(f"{mensajes_de_error[0]}")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! El valor debe estar entre {lim_inf} y {lim_sup}")
                    errores = True
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! El valor debe ser mayor que {lim_inf}")
                    errores = True
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! El valor debe ser menor que {lim_sup}")
                    errores = True
        if errores:
            continue
        else:
            return num


def validar_str(msg_input: str, digitos: bool, es_correo: bool, es_nombre: bool) -> str:
    while True:
        errores = False
        texto = input(msg_input).strip()
        if es_nombre:
            texto = texto.title()
        if digitos:
            return texto
        elif not digitos:
            if texto == "":
                print("Inválido! Este campo no puede estar vacío")
                continue
            for i in texto:
                if i.isdigit():
                    print("Inválido! Este campo no puede contener dígitos")
                    errores = True
                    break
        if es_correo:
            if "@" not in texto:
                print("Inválido! Este campo debe contener un correo electrónico")
                errores = True
        if errores:
            continue
        else:
            return texto


def agregar_doctor():
    print("--- AGREGAR DOCTOR ---\n")


def menu_1() -> None:
    pass


def menu_2() -> None:
    while True:
        opc = validar_int(
            "--- DOCTORES ---\n(1) AGREGAR DOCTOR\n(2) MODIFICAR DOCTOR\n(3) ELIMINAR DOCTOR\n(4) VER LISTA DOCTORES\n(5) BUSCAR DOCTOR\n(0) VOLVER\n",
            0,
            5,
            True,
            True,
        )
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


def menu_3() -> None:
    pass


def menu() -> None:
    while True:
        opc = validar_int(
            "==== MENU PRINCIPAL ====\n(1) HACER CUENTA\n(2) DOCTORES\n(3) TRABAJOS\n(0) SALIR\n",
            0,
            3,
            True,
            True,
        )
        if opc == 1:
            menu_1()
        elif opc == 2:
            menu_2()
        elif opc == 3:
            menu_3()
        elif opc == 0:
            break
