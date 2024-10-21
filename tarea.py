
def menu_principal():
    while True:
        print('Seleccione el proceso que desea aplicar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora')
        print('3: Finalizar')
        opcion = input('Introduzca un número del 1 al 3: ')

        if opcion.isdecimal():
            opcion = int(opcion)
            if opcion == 1:
                cargade_puntuacion_comentario()
            elif opcion == 2:
                mostrar_resultados()
            elif opcion == 3:
                print('Finalizando...')
                break
            else:
                print('Por favor, introduzca del 1 al 3.')
        else:
            print('Por favor, introduzca un número válido.')

def cargade_puntuacion_comentario():
    while True:
        point = input('Por favor, introduzca una puntuación en una escala de 1 a 5: ')
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                comment = input('Por favor, introduzca un comentario: ')
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'Punto: {point}, Comentario: {comment}\n')
                print('Puntuación y comentario guardados.')
                break
            else:
                print('Por favor, introduzca un valor entre el 1 y 5.')
        else:
            print('Por favor, introduzca la puntuación en números.')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", 'r') as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print('Aún no hay resultados guardados.')

menu_principal()

