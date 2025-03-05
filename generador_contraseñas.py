import random
import string

numeros = string.digits
letras_minu = string.ascii_lowercase
letras_mayu = string.ascii_uppercase
caracteres = "!@#$%^&*()\-_=+.,"
letras_numeros = numeros + letras_minu + letras_mayu
todos_los_caracteres = numeros + letras_minu + letras_mayu + caracteres

while True:

    print("\n🔐 Escoje una opcion sobre que tipo de contraseña deseas 🎫")
    print("1. Solo letras y numeros en la contraseña")
    print("2. Incluir caracteres a la contraseña")

    opcion = input("\nEscoje una opcion: ")

    if opcion not in ['1', '2']:
         print("❌ Escoje una opcion valida")
         continue

    try:
        longitud_contra = int(input("Ingresa la longitud de la contraseña: "))
        if longitud_contra <= 0:
            print("❌ La longitud debe ser mayor a 0")
            continue

        cantidad_contraseñas = int(input("Ingresa cuantas contraseñas quieres: "))
        if cantidad_contraseñas <= 0:
            print("❌ La cantidad debe ser mayor a 0")
     
    except ValueError:
          print("❌ Ingresa un numero valido")
          continue

    contraseñas = []
    for _ in range(cantidad_contraseñas):
        if opcion == '1':
            contrasena = "".join(random.sample(letras_numeros, k= longitud_contra))
        else:
            contrasena = "".join(random.sample(todos_los_caracteres, k = longitud_contra))
        contraseñas.append(contrasena)

    print("\n🔑 Contraseñas generadas:")
    for i, c in enumerate(contraseñas, start=1):
        print(f"{i}. {c}")

    while True:
        print("\nSi no elijes una contraseña el sistema te dara una sugerida")
        seleccion = input("✏️ Escribe el número de la contraseña que deseas usar (o presiona Enter para salir): ")
        
        if seleccion == "":
            sugerida = random.choice(contraseñas)
            print(f"\nContraseña Sugerida: {sugerida}")
            print("👋🏽 Hasta luego, ¡vuelve pronto!")
            break

        if seleccion.isdigit() and 1 <= int(seleccion) <= cantidad_contraseñas:
            print(f"\n✅ Has seleccionado: **{contraseñas[int(seleccion)-1]}** 🔒")
            break
        else:
            print("❌ Número inválido, intenta de nuevo.")

    break
   