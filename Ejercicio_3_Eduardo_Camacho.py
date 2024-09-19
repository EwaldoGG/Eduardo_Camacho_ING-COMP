#Ejercicio 3 Eduardo Camacho

#El usuario ingresa y crea su contraseña
password = input ("Ingrese su contraseña")

#Mensaje informativo para mostrar que la contraseña fue guardada
print ("Su contraseña fue guardada")


#Pedir que ingrese su contraseña
print ("Ingrese nuevamente su contraseña")

#imprimir si la contraseña es la correcta, y dar acceso al usuario
if input () == password:
    print ("La contraseña es correcta, adelante.")

#Si la contraseña no es correcta, imprime un mensaje informativo
else:
    print ("La contraseña no es la correcta.")
