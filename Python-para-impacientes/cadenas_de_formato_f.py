# Apartir de Python 3.6 las cadenas f proporcionan una forma sencilla de integrar variables y expresiones 
# dentro de una cadena empleando una sintaxis muy reducida. A continuacion, se muestra su potencial con varios ejemplos:

# Una cadena "f" se suele presentar como un literal
# entrecomillado al que le precede el caracter "f" o "F":

f'cadena'

# El resultado de evaluar una cadenha "f" se puede 
# asignar a una variable:

cadenaf = f'cadena'

# Tambien, se puede extender a varias lineas utilizando las triples comillas:

cadenaf = f'''linea1
linea2
lineas3'''

# Dentro de una cadena "f" se pueden insertar
#  variables y expresiones escribiendolas entre
#  llaves {}

modelo = 'Orbea Alma'
precio = 650
ipuestos = precio * 21/100
print(f'Bicicleta {modelo}: {precio=impuestos} euros')
# Bicicleta Orbea Alma: 786.5 euros

# 