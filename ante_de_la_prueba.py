import os
menu = ['Ver usuarios', 'Agregar usuario', 'Eliminar usuario', 'Salir']

agenda = {'geison': {'Edad' :  21, 'Direccion': 'jose pepe pepe', 'Telefono': 933544103}}

while True:
    for ind, alternativa in enumerate(menu):
        print(f'{ind + 1}. {alternativa}')
    opcion = input('Elija una opcion\n')
    if opcion == '1':
        os.system('cls')
        for usuario, info in agenda.items():
            print(f'{usuario}/{info['Edad']}/{info['Direccion']}/{info['Telefono']}')
            print()
    elif opcion == '2':
        os.system('cls')
        nombre = input('Ingrese nombre del usuario\n')

        while True:
            try:
                edad = int(input('Ingrese edad del usuario\n'))
                break
            except:
                print('La edad solo puede contener numeros')

        direccion = input('Ingrese direccion del usuario\n')
        while True:
            try:
                telefono = int(input('Ingrese telefono del usuario\n'))
                break
            except:
                print('Error solo deve contener numeros')

        print(f'El usiario {nombre} seguardo exitosamente')
        agenda[nombre] = {'Edad': edad, 'Direccion': direccion, 'Telefono': telefono}

    elif opcion == '3':
        os.system('cls')
        nombre_eliminar =input('ingrese el nombre del usuario a eliminar')

        if nombre_eliminar in agenda:
            del agenda[nombre_eliminar]
            print('Usuario eliminado con exito')
        else:
            print('Usuario no encontrado')

    elif opcion == '4':
        os.system('cls')
        exit('!Muchas gracias, hasta pronto.')

    else:
        os.system('cls')
        print('Error, opcion no valida')
    
