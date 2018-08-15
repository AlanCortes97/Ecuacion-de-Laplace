# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:24:10 2017
Ecuacion de Calor detras
@author: Alan Jesus Cortes
"""
from tabulate import tabulate
import matplotlib.pyplot as plt
import xlsxwriter
import numpy as np
plt.figure()
print("Ecuación de calor en 1 dimensión:diferencias por detras")
A=int(input("Tamaño de malla en X"))
B=int(input("Tamaño de malla en Y"))
alfa=float(input("Constante de Calor"))
a=float(1/A)
b=float(1/B)
tabla=[]
tabla1=[]
for i in range(B+1):
    tabla.append([0]*(A+1))
for i in range(B+1):
    tabla1.append([0]*(A+1))
print(tabulate(tabla))
print("para poner las condiciones ponga los numeros separados por espacios, o si es constante solo ponga 1 numero")
print("Condicion inferior y=0 x=x ")
condicion2=[float(x) for x in input().split()]
if len(condicion2)==(1):
    condicion2=([condicion2[0]]*(A+1))
print("Condicion izquierda y=y x=0, poner solo los ",(B), " terminos que faltan de arriba hacia abajo")  
condicion3=[float(x) for x in input().split()]
if len(condicion3)==(1):
    condicion3=([condicion3[0]]*(B))
print("Condicion derecha y=y x= ",A," , poner solo los ",(B), " terminos que faltan de arriba hacia abajo")
condicion4=[float(x) for x in input().split()]
if len(condicion4)==(1):
    condicion4=([condicion4[0]]*(B))
tabla[0]=condicion2
for x in range(1,B+1):
    tabla[x][0]=condicion3[x-1]
    tabla[x][A]=condicion4[x-1]
for z in range (1,500):
    for y in range(1,B+1):
        for x in range(1,A):
            tabla[y][x]=(1/(a**2+2*b*alfa))*(a**2*tabla[y-1][x]+b*alfa*(tabla[y][x+1]+tabla[y][x-1]))
for x in range(0,B+1):
    tabla1[x]=tabla[B-x]
print(tabulate(tabla1))
plt.autoscale(enable=True, axis='both', tight=False)
plt.imshow(tabla,cmap="coolwarm",origin='lower')
plt.colorbar()
plt.show()
workbook=xlsxwriter.Workbook('Ecuacion de calor por detrás ejercicio 1.xlsx')
worksheet=workbook.add_worksheet()
tabla1=np.array(tabla1)
"""for y in range(B+1):
    for x in range(A+1):
        worksheet.write(y,x,tabla1[y][x])
worksheet.conditional_format(0,0,B,A,{'type':'3_color_scale',
                                      'min_color':'#A8D8F1',
                                      'mid_color':'#FFFFFF',
                                      'max_color':'#F26161'})
workbook.close()"""

