valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n%2 == 0]


temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [((grado_fahrenheit-32)*(5/9)) for grado_fahrenheit in temperatura_fahrenheit]


