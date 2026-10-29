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