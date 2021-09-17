opcion =1

contactos=[]
while opcion !=0:
    print('-----------------------')
    print('Menu de contactos')
    print('1. crear contactos')
    print('2. listar contactos')
    print('3. actualizar contactos')
    print('4. eliminar contactos')
    print('0. salir')

    opcion = int(input())
    if opcion == 1:
        nombre = input ('ingresar nombre : ')
        apellido = input ('ingresar apellido : ')
        celular = input ('ingresar celular : ')
        correo = input ('ingresar correo : ')
        contactos.append({
            'nombre ': nombre,
            'apellido': apellido,
            'celular': celular,
            'correo': correo,
        })
        input('contacto guardado correctamente. presiona enter para continuar')
    elif opcion == 2:
        print(contactos)

