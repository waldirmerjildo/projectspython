

def par_impar():
    num = int(input("Elige un numero entre 1 y 1000:  "))
    if num % 2 == 0:
        print(f'El numero {num} es PAR! ¿Puedes añadir otro?')
        pregunta()
    else:
        print(f'El numero {num} es IMPAR! ¿Puedes añadir otro?')
        pregunta()
    
def pregunta():
    letra = input("Eige s si deseas continuar o n para salir: ")
    if letra == 's':
        par_impar()
    elif letra == 'n':
        print("Hasta luego!")
    else:
        print("Letra incorrecta")
        pregunta()

par_impar()