while True:
    print("----MENU-----")
    print("1. personas \n 2. vehiculo \n 3. Universidades \n 4. Notas \n 5. Salir")
    opcion= int(input ("eliga una opcion entre 1 y 5: "))
    if opcion == 1:
        print("Hola, has presionado la opción Personas")
    elif opcion == 2:
        print("Hola, has presionado la opción Vehiculos")
    elif opcion == 3:
        print("Hola, has presionado la opción Universidades")
    elif opcion == 4:
        print("Hola, has presionado la opción Notas")
    elif opcion == 5:
        print("cerrando menu...")
        break
    if opcion < 1 or opcion > 5:
        print ("\n su opcion es erronea, por favor engrese un numero de 1 a 5\n")