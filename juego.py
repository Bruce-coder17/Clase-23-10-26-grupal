import random

def evaluar_temperatura(secreto, intento):
  """Calcula la distancia entre el número secreto y el intento

  y devuelve un mensaje de temperatura.
  """
  diferencia = abs(secreto - intento)

  if diferencia == 0:
    return "¡Ganaste! 🏆"
  elif diferencia <= 3:
    return "🔥 ¡Muy caliente! Estás súper cerca."
  elif diferencia <= 10:
    return "☀️ Caliente, vas por buen camino."
  elif diferencia <= 25:
    return "⛅ Tibio, aún te falta un poco."
  else:
    return "❄️ ¡Muy frío! Estás muy lejos."

def jugar():
    secreto = random.randint(1, 100)
    intentos = 0

    print("=========================================")
    print("🎮 ¡Adivina el número secreto (1 al 100)! 🎮")
    print("=========================================")

    while True:
        entrada = input("\nIntroduce tu número: ")

        # Validar que sea un número válido
        if not entrada.isdigit():
            print("⚠️ Por favor, ingresa solo números enteros.")
            continue

        intento = int(entrada)
        intentos += 1

        # Llamamos a la lógica del Integrante 1
        mensaje = evaluar_temperatura(secreto, intento)
        print(mensaje)

        if intento == secreto:
            print(f"✨ ¡Adivinaste en {intentos} intentos! ✨")
            break

# Ejecutar el juego
if __name__ == "__main__":
    jugar()