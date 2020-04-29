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

# A partir de python 3.8 un signo igual '=' tras el 
# nombre de una variable inserta tanto el nombre de 
# la variable como su valor:

importe = 1300
descuento = 15
print(f'Informacion de la cpmpra: {importe=} €, {descuentos=} %')
# Información de la compra: importe=1300 €, descuento=15 %

# las dobles llaves se utilizan para expresar el 
# nombres de una variable o mostrar literalmente una 
# expresion y no el valorresultante de su evaluacion:

arbol = 'secuoya'
alt = 115
print(f'Una {arbol}' 'mide 'f'{alt } metros')
# La secuoya mide hasta 115 metros

print(f'Una { arbol }'+' mide '+f'{alt} metros')
# La secuoya mide hasta 115 metros


# En la declaración de una cadena el carácter "f" 
# se puede combinar con el carácter "r" de las
# cadenas row (crudas) para que no se interpreten
# las secuencias de escape (caracteres especiales 
# precedidos de la barra invertida "\"):
# "\n" (salto de línea), "\t" (tabulador), etc. 
# Sin embargo, "f" no se puede combinar con "b" o
# "u" que se utilizan para representar cadenas de
# Bytes o caracteres Unicode, respectivamente:

cadenacruda = fr'la línea finaliza con \n'
print(cadenacruda)  # la línea finaliza con \n

# Las secuencias de escape no se pueden incluir
# en una expresión:

print(f'Esta cadena genera un {\"error\"}')
print(f'Esta cadena no genera un {"error"}')

# Después de cada expresión se puede indicar un
# especificador para establecer algún tipo de
# conversión. Las conversiones permitidas se expresan
# con '!s' , '!r' y '!a' que son equivalentes a las
# funciones str(), repr() y ascii(), respectivamente:

novela = 'En busca del unicornio'
cadena = f'La novela se llama {novela!r}'
print(cadena) 

# La novela se llama 'En busca del unicornio'

# Los especificadores de formato permiten fijar 
# el espacio reservado para la parte entera de 
# una expresión numérica y su precisión decimal:

ancho = 10
precision = 5
numpi = 3.14159265358979323846
print(f"Número PI: {numpi:{ancho}.{precision}}")
# Número PI:     3.1416

# Los especificadores que se utilizan para
# formatear fechas y horas se pueden utilizar
# en una cadena "f":

from datetime import datetime
fecha = datetime.now()
print(f'El partido de tenis se jugará el día {fecha:%d}')
# El partido de tenis se jugará el día 10

# Una expresión de una cadena "f" puede incluir
# llamadas a funciones:

def suma(a,b):
    return a+b
    
a = 10
b = a * 12  
rtdo = f'La suma total es {suma(a,b)}'
print(rtdo)  # La suma total es 130

# ...Y la función Lambda es una función más:

b = 10
h = 5
print(f'Área triángulo: {(lambda b,h: b*h/2)(b,h)}')
# Área triángulo: 25.0