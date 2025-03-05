import re
import getpass
import random
import string

def evaluar_contraseña(contraseña):

    mejoras = []
    cumple_longitud = len(contraseña) >= 8
    tiene_mayuscula = bool(re.search(r'[A-Z]', contraseña))
    tiene_minuscula = bool(re.search(r'[a-z]', contraseña))
    tiene_numero = bool(re.search(r'\d', contraseña))
    tiene_especial = bool(re.search(r'[!@#$%^&*()\-_=+.,]', contraseña))

    if not cumple_longitud:
        mejoras.append("Debe tener almenos 8 caracteres")
    if not tiene_mayuscula:
        mejoras.append("Debe contener almenos una mayuscula")
    if not tiene_minuscula:
        mejoras.append("Debe contener almenos una minuscula")
    if not tiene_numero:
        mejoras.append("Debe contener almenos un numero")
    if not tiene_especial:
        mejoras.append("Debe contener almenos un caracter especial")

    criterio_cumplidos = sum([cumple_longitud, tiene_especial, tiene_mayuscula, tiene_minuscula, tiene_numero])

    if criterio_cumplidos == 5:
        return "✅ Fuerte", mejoras
    elif criterio_cumplidos == 4:
        return "🟡 Media", mejoras
    else:
        return "❌ Debil", mejoras
    
def contra_segura():
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()\-_=+.,"
    return "".join(random.sample(caracteres, 8))
    
while True:

    contraseña = getpass.getpass("\n🔐 Ingresa una contraseña \n")
    clasificacion, mejoras = evaluar_contraseña(contraseña)

    print(f"\nEvaluacion {clasificacion}")
    if mejoras:
        print("Recomendaciones")
        for mejora in mejoras:
            print(f" - {mejora}")

    if clasificacion == "✅ Fuerte":
        print("\nTu contraseña es segura")
    elif clasificacion == "🟡 Media":
        print("Intenta mejorar tu contraseña e intenta nuevamente")
        continue
    else:
        print("\n🔴 Tu contraseña es debil, intenta mejorarla")
        sugerencia = contra_segura()
        print(f"🔹 Sugerencia de contraseña segura: {sugerencia}")
        
    seleccion = input("\nQuieres ingresar otra contraseña (s/n): ").lower()
    if seleccion != 's':
        print("\n👋 ¡Hasta la próxima! 😊")
        break