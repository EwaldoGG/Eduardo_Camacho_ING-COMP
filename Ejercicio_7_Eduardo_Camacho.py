# Solicitar la calificación al usuario
calificacion = float(input("Ingresa una calificación (0-100): "))

# Verificar que la calificación esté en el rango permitido
if 0 <= calificacion <= 100:

    # Determinar la calificación correspondiente
    # Si la calificación está entre 90 y 100
    if 90 <= calificacion <= 100:
        letra = 'A'

    # Si la calificación está entre 80 y 89
    elif 80 <= calificacion < 90:
        letra = 'B'

    # Si la calificación está entre 70 y 79
    elif 70 <= calificacion < 80:
        letra = 'C'

    # Si la calificación está entre 60 y 69
    elif 60 <= calificacion < 70:
        letra = 'D'

        # Si la calificación está entre 0 y 59
    else:
        letra = 'F'

    # Mostrar el resultado de la calificación correspondiente
    print(f"La calificación correspondiente es: {letra}")
    
else:
    
    # Mensaje de error si la calificación no está en el rango válido
    print("Por favor, ingresa una calificación válida entre 0 y 100.")
