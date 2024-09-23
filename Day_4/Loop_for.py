for i in range(0, 10):
    print(i)
    print('*'*i)


alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for nombre in alumnos_clase:
    print(f'Hola {nombre}')


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for num in lista_numeros:
    suma_numeros += num


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num%2 == 0:
        suma_pares += num
    else:
        suma_impares += num


