#Ejercicio 2 Eduardo Camacho

#Pedir al usuario que ingrese la base y la altura del rectángulo
b = float(input("Ingresa la base del rectángulo: "))
h = float(input("Ingresa la altura del rectángulo: "))

#Calcular el área del rectángulo
a = b * h

#Mostrar el área calculada
print(f"El área del rectángulo es: {a}")

#Verificar las condiciones y mostrar un mensaje personalizado si se cumplen
if a > 40 and h > 10:
    print("wow, has llegado lejos, pero te falta mucho por afrontar, anímate, esfuerzáte, no estás solo en esto")
else:
    print("El rectángulo no cumple con las condiciones para desbloquear el mensaje oculto")
