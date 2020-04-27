# Formateo con %
# --------------

# El formato basado en % sólo es válido para los tipos de 
# datos str, int y float:

nombre = 'Claudia'
edad = 35
altura = 1.82

print('Tiene %i años' %edad)  # Tiene 35 años
print('%s tiene %i años y mide %f m.' %(nombre, edad, altura))
# Claudia tiene 35 años y mide 1.820000 m.

# Un objeto datetime (una hora o fecha) y otro tipo de
# objetos no pueden imprimirse sin hacer previamente una 
# conversión del tipo de dato. 


# Formateo con str.format()
# -------------------------

# El formato con str.format() permite fijar la longitud de
# una cadena, aplicar formatos numéricos, establecer la 
# alineación, tabular datos y rellenar espacios con un 
# determinado caracter:

# Aplica formatos numéricos ajustando la precisión:

valor1 = 8.56767  # asigna flotante
valor2 = 9.45548  # asigna flotante
print('{0:.3} {1:.4}'.format(valor1, valor2))  # 8.57 9.455

# Alinea y rellena con caracteres:

for alin, txt in zip('<^>', ['izquierda', 'centro', 'derecha']):
    print('{0:{fill}{align}30}'.format(txt, 
          fill="*", 
          align=alin))

# izquierda*********************
# ************centro************
# ***********************derecha

# Rellena con guiones bajos:

print('{0:_^30}'.format('Python para impacientes'))
# ___Python para impacientes____

# Tiene el inconveniente de la falta de concisión cuando
# se insertan valores en una cadena:

vel = 120
print('Velocidad permitida: {vel} Km/h.'.format(vel=vel))
# Velocidad permitida: 120 Km/h.

# Incluso en su forma abreviada es algo enrevesado:

print('Velocidad permitida: {} Km/h.'.format(vel))
# Velocidad permitida: 120 Km/h.


# Formateo con string.Template
# ----------------------------

# Con string.Template también se pueden insertar los 
# valores de variables y/o expresiones en una cadena,
# aunque la brevedad brilla por su ausencia:

from string import Template
import datetime
perfil = Template('$nom es $pro con un salario de $sal e.')
print(perfil.substitute(nom='Carmen', 
                        pro='programadora',
                        sal=1900))
# Carmen es programadora con un salario de 1900 e.

fecha = datetime.date(2017, 2, 10)
contrato = Template('Su contrato se hizo el dia $dia')
print(contrato.substitute(dia=fecha.day))

# Se expresa con bastante claridad pero también con
# demasiada verbosidad.