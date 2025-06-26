print("1 ingrese usuario ")
print("2 buscar usuario ")
print("3 eliminar usuario ")
print("4 salir ")
opc=input()
nombre={}
usuarios = [
    {"nombre": "lego", "sexo": "M", "clave":"12345656f"},
    {"nombre": "fabian", "sexo": "f", "clave":"6543212f"},
]

usuarios = [
    {"nombre": "Juan", "sexo": "M", "clave":"123456"},
    {"nombre": "Omar", "sexo": "M", "clave":"654321"},
]

def validar_clave(clave):
    if len(clave) < 8:
        return False
    if " " in clave:
        return False
    for c in clave:
        if c.isalpha():
            break
    else:
        return False
    for c in clave:
        if c.isdigit():
            break
    else:
        return False
    return True

def validar_nombre_unico(nombre):
    for u in usuarios:
        if u["nombre"] == nombre:
            return True
    else:
        return False

def consultar_usuario(nombre):
    for u in usuarios:
        if u["nombre"] == nombre:            
            print(u)
            break
    else:
        print("Usuario no encontrado, revise el nombre.")

def eliminar_usuario(nombre):
    for u in usuarios:
        if u["nombre"] == nombre:            
            usuarios.remove(u)
            print("Usuario eliminado correctamente!.")
            break
    else:
        print("Usuario no encontrado, revise el nombre.")


def registrar_usuario():
    while True:
        nombre = input("Ingresa tu nombre : ")
        if not validar_nombre_unico(nombre):
            break
        else:
            print("Error, este nombre ya está ocupado!.")
    while True:
        sexo = input("Ingresa tu sexo (F/M): ")
        if sexo in ["F", "f", "M", "m"]:
            break
        else:
            print("Error, Ingrese solo F o M!.")
    while True:
        clave = input("Ingresa tu clave: ")
        if validar_clave(clave):
            break
        else:
            print("Error, la clave debe contener minimo 8 caracteres, una letra, un numero")
    usuarios.append({
        "nombre":nombre, "sexo": sexo, "clave":clave
    })
    print("Usuario agregado exitosamente!.")


    
    while True:    
     opc = menu()
     if opc == "1":
        registrar_usuario()
     elif opc == "2":
        nombre = input("Ingresa el nombre : ")
        consultar_usuario(nombre)
     elif opc == "3":
        nombre = input("Ingresa el nombre : ")
        eliminar_usuario(nombre)
        print("el usuario a sido eliminado")
     elif opc =="4":
        print("has salido")
        break 
    
    else:
    print("Error, opción no válida")