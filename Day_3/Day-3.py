texto = input('ingresa un texto: ')
texto_minuscula = texto.lower()


letras = input('ingresa tres letras: ')
letras_minuscula = letras.lower()

print(f'la letra {letras_minuscula[0]} aparece {texto.count(letras_minuscula[0])} veces')
print(f'la letra {letras_minuscula[1]} aparece {texto.count(letras_minuscula[1])} veces')
print(f'la letra {letras_minuscula[2]} aparece {texto.count(letras_minuscula[2])} veces')

palabras = texto.split()
print(f'el texto tiene {len(palabras)} palabras')

print(f'la primera letra del texto es {texto[0]} y la ultima es {texto[-1]}')

texto_invertido = palabras[::-1]
texto_invertido = ' '.join(texto_invertido)
print(f'el texto invertido es {texto_invertido}')

exist = 'python' in texto_minuscula
resp = {True: 'si', False: 'no'}
print(f'la palabra "python" {resp[exist]} esta en el texto.')