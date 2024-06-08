def calculadora():
    while True:
        print("\n--------------")
        print("Opciones")
        print("--------------\n")
        print()
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        print()

        opcion = input("-Elige una opción:")

        if opcion == '5':
            print("¡Hasta luego, bro!")
            break

        num1 = float(input("Ingresar el primer número: "))
        num2 = float(input("Ingresar el segundo número: "))

        # Opciones
        if opcion == '1':  # suma
            print("\n|Resultado:", num1 + num2)
        elif opcion == '2':  # resta
            print("\n|Resultado:", num1 - num2)
        elif opcion == '3':  # multiplicación
            print("\n|Resultado:", num1 * num2)
        elif opcion == '4':  # división
            if num2 != 0:
                print("\n|Resultado:", num1 / num2)
            else:
                print("\n|No se puede dividir por cero.")
        else:
            print("\n|Opción inválida")

calculadora()
