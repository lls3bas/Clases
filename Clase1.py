###Calculadora simple

num1 = float(input("Bienvenido a la calculadora simple. Dame un numero: "))
num2 = float(input("Dame otro numero: "))
operacion = input("Dame la operacion (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2

print(f"El resultado es: {resultado}")

### Area de un triangulo

base = float(input("Dame la base del triangulo: "))
altura = float(input("Dame la altura del triangulo: "))
area = (base * altura) / 2
print(f"El area del triangulo es: {area}")


### Celcius a Farenheit


temp = float(input("Dame la temperatura en grados Celcius: "))
faren = (temp * 9/5) + 32
print(f"La temperatura en grados Farenheit es: {faren}")

### Numero par o impar 


valor = int(input("Para saber si es par o impar, dame un numero: "))
if valor % 2 == 0:
    print(f"El numero {valor} es par.")
else:
    print(f"El numero {valor} es impar.")

###  Mayor que

print("Vamos a comparar dos numeros a ver cual es mayor que el otro.")
valor1 = float(input("Dame un numero: "))
valor2 = float(input("Dame otro numero: "))
if valor1 > valor2:
    print(f"El numero {valor1} es mayor que {valor2}.")
elif valor2 > valor1:
    print(f"El numero {valor2} es mayor que {valor1}.")
else:
    print(f"Los numeros {valor1} y {valor2} son iguales.")

### Año bisiesto 
print("Vamos a ver si un año es bisiesto o no.")
año = int(input("Dame un año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

### Calculadora de descuento 

print("Vamos a calcular el precio final con descuento.")
precio_produc = float(input("Dame el precio: "))
descuento = float(input("Dame el descuento: "))
precio_final = precio_produc - (precio_produc * descuento / 100)
print(f"El precio final con descuento es: {precio_final}")


### IMC

print("Vamos a calcular tu porcentaje de grasa corporal (IMC).")
peso = float(input("Dame tu peso en kg: "))
altura = float(input("Dame tu altura en metros: "))
IMC = peso / (altura ** 2)
print(f"Tu IMC es: {IMC}")

### Promedio de notas 
print("Ahora vamos a ver tu promedio de notas")
nota1 = float(input("Dame tres notas, aqui la primera: "))
nota2 = float(input("Segunda: "))
nota3 = float(input("Tercera: "))
promedio = (nota1 + nota2 + nota3)/ 3
print(f"Tu promedio es de: {promedio}")

### Duracion en segundos

print("Ahora calcularemos la duracion de una hora en segundos.")
duracion = float(input("Dame un tiempo (horas, minutos o segundos): "))
duracion_tipo = input("¿Que tipo es?(h, m, s): ")
if duracion_tipo == "h":
    print(f"El total en segundos es de: {duracion * 3600}")
elif duracion_tipo == "m":
    print(f"El total en segundos es: {duracion * 60}")
elif duracion_tipo == "s":
    print(f"El resultado en segundos es: {duracion}")
else:
    print("No hay un valor aceptado")