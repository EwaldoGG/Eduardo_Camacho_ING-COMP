#Ejercicio 5 Eduardo Camacho

#Asignamos el salario anual
salario_anual = 2400

#Pedimos al usuario su puntuación final
puntuacion = float(input("Ingresa tu puntuación: "))


#Verificar que la calificación esté en el rango de valores correcto

#Si los puntos obtenidos son "0.0"

if 0.0 <= puntuacion <= 0.4:
        rendimiento = "Inaceptable"

    #Si los puntos obtenidos son "0.4"
elif  0.4 <= puntuacion <= 0.6:
        rendimiento = "Aceptable"

        #Si los puntos obtenidos son "0.6 o más"
elif  puntuacion >= 0.6 :
        rendimiento = "Meritorio"

else:
        #Se imprimirá un mensaje de error si la calificación no está en el rango de valores correctos
        print("Por favor, ingresa una calificación válida entre 0.0 y 1.0")

bonificacion = salario_anual*puntuacion

    #Se imprimirá el resultado de la calificación correspondiente
print(f"Tu nivel de rendimiento ha sido: {rendimiento}")
print(f"Tu bonificacion: {bonificacion}€")
    

