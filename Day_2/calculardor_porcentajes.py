# nombre = 'Tony Soprano'
# edad = 51


# nombre = 'Julia'
# apellido = 'Roberts'
# nombrecompleto = nombre + ' ' + apellido


# curso = 'Python'
# print('Estás tomando un curso de ' + curso)


# num_entero = 5
# print(type(num_entero))


# num_decimal = 5.5
# print(type(num_decimal))


# num1 = 7.5
# num2 = 2.5
# suma = num1+num2
# print(type(suma))


# num1 = 7.5
# num1 = int(num1)
# print(type(num1))


# num2 = 10
# num2 = float(num2)
# print(type(num2))


# num1 = "7.5"
# num2 = "10"
# print(float(num1) + int(num2))


# nombre_asociado = "Jesse Pinkman"
# numero_asociado = 399058
# print(f'Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}')


# puntos_nuevos = 350
# puntos_totales = 1225
# print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos')


# puntos_anteriores = 875
# puntos_nuevos = 350
# print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_nuevos + puntos_anteriores} puntos')

# y = 2
# z = 7
# print(f'{z} dividido por {y} es igual a {z/y}')
# print(f'{z} dividido redondeado por {y} es igual a {z//y}')
# print(f'{z} modulo de {y} es igual a {z%y}')
# print(f'{z} elevado a la {y} es igual a {z**y}')
# print(f'La raíz cuadrada de {z} es igual a {z**0.5}')


# print(int(874/27))
# print(456%33)
# print(783**.5)


# division = 10/3
# print(round(division, 2))

# valor = 10.676767
# print(round(valor))


# raiz = 5**0.5
# print(round(raiz, 4))


# num1 = 13.87
# print(round(num1))
# print(int(num1))

# num1 = round(13/2,0)
# print(type(num1))

# Proyecto del dia 2

name = input('Ingrese su nombre: ')
money = float(input('Ingrese la cantidad de ventas del mes: '))

porcentaje = money * (13/100)
print(f'Ok {name}, este mes ganaste ${money+porcentaje}')