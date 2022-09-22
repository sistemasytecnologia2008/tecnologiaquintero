# -*- coding: utf-8 -*-
"""clase_8_8 SEPTIEMBRE 2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17WQSS1SbP2BK3Zamn84a7r_PYfxoeNbk

<center>

#**COLEGIO SIGLO XXI - EL SOCORRO**
#**PRESENTADO A: ING PAOLA ANDREA QUINTERO**
#**PRESENTADO POR: XLSLKDSD**
#**GRADO DÉCIMO**
#**8 SEPTIEMBRE 2022**

#**¿Qué es Python?**
# Es un le
#Fecha de lanzamiento:
#Creadores:

#Recuperado de:
"""

print("Esto es una suma")
numero_uno = 2
numero_dos = 4
resultado = numero_uno + numero_dos
print(resultado)

print("Esto es una resta")
numero_uno = 7
numero_dos = 4
resultado = numero_uno - numero_dos
print(resultado)

print("Esto es una multiplicacion")
numero_uno = 5
numero_dos = 9
resultado = numero_uno * numero_dos
print(resultado)

print("Esto es una division")
numero_uno = 198
numero_dos = 48
resultado = numero_uno / numero_dos
print(resultado)

"""#Ejercicios de Tipos de Datos Simples

## Ejercicio 1

Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))

"""## Ejercicio 2

Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase `Tu índice de masa corporal es <imc>` donde `<imc>` es el índice de masa corporal calculado redondeado con dos decimales. 
"""

peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))

"""# **LIBRERÍAS EN PYTHON**

Concepto

#***Librería Panda***

Concepto

# Ejercicio 

Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:


| Mes     | Ventas | Gastos |
| ------- | -----: | -----: |
| Enero   |  30500 |  22000 |
| Febrero |  35600 |  23400 |
| Marzo   |  28300 |  18100 |
| Abril   |  33900 |  20700 |
"""

import pandas as pd

datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
contabilidad = pd.DataFrame(datos)
print(contabilidad)

"""# ***Librería  Matplotlib***

Concepto

# Ejercicio

Gráfico torta
"""

import matplotlib.pyplot as plt    #Colores los da la librería 

l = ('Python', 'C++', 'Ruby', 'Java')
sizes = [200, 130, 600, 210]

e = (0.1, 0, 0, 0)  # explode 1st slice
 
plt.pie(sizes, explode=e, labels=l)

plt.show()

"""<center>

#**©Copyright - Tecnología e informática - Colegio Siglo XXI - El Socorro**
"""