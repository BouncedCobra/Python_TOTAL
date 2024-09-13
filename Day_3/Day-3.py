# name = 'Hola Mundo'
# print(name.index('l'))


# palabra = "ordenador"
# print(palabra[4])


# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
# print(frase.index('práctica'))


# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
# print(frase.rindex('práctica'))


# frase = "Controlar la complejidad es la esencia de la programación"
# fragmento = frase[:9]
# print(fragmento)


# frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
# fragmento = frase[8::3]
# print(fragmento)


# frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
# print(frase[::-1])


# frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
# print(frase.upper())


# lista_palabras = ["La","legibilidad","cuenta."]
# union = " ".join(lista_palabras)
# print(union)


frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
change = frase.replace('difícil','fácil')
change = change.replace('mala','buena')
print(change)