from tabulate import tabulate
import matplotlib.pyplot as plt
import xlsxwriter
import numpy as np

plt.figure()
print("Ecuación de laplace 2 dimensiones")
A=int(input("Cordenada x maxima"))
B=int(input("Coordenada y maxima "))
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
print("Condicion superior y= ", B ,"x=x ")
condicion1=[float(x) for x in input().split()]
if len(condicion1)==(1):
    condicion1=([condicion1[0]]*(A+1))
print("Condicion inferior y=0 x=x ")
condicion2=[float(x) for x in input().split()]
if len(condicion2)==(1):
    condicion2=([condicion2[0]]*(A+1))
print("Condicion izquierda y=y x=0, poner solo los ",(B-1), " terminos que faltan de arriba hacia abajo")  
condicion3=[float(x) for x in input().split()]
if len(condicion3)==(1):
    condicion3=([condicion3[0]]*(B-1))
print("Condicion derecha y=y x= ",A," , poner solo los ",(B-1), " terminos que faltan de arriba hacia abajo")
condicion4=[float(x) for x in input().split()]
if len(condicion4)==(1):
    condicion4=([condicion4[0]]*(B-1))
tabla[0]=condicion1
tabla[B]=condicion2
for x in range(B-1):
    tabla[x+1][0]=condicion3[x]
    tabla[x+1][A]=condicion4[x]
print(tabulate(tabla))
for z in range (1,500):
    for y in range(1,B):
        for x in range(1,A):
            tabla[y][x]=(1/((1/a**2)+(1/b**2)))*((1/(2*(a**2)))*(tabla[y][x+1]+tabla[y][x-1])+(1/(2*(b**2)))*(tabla[y+1][x]+tabla[y-1][x]))
for x in range(0,B+1):
    tabla1[x]=tabla[B-x]
print(tabulate(tabla))
plt.imshow(tabla1,cmap="coolwarm",origin='lower')
plt.colorbar()
plt.show()
workbook=xlsxwriter.Workbook('Ecuacion de laplace EJERCICIO 6.xlsx')
worksheet=workbook.add_worksheet()
"""
for y in range(B+1):
    for x in range(A+1):
        worksheet.write(y,x,tabla[y][x])
worksheet.conditional_format(0,0,B,A,{'type':'3_color_scale',
                                      'min_color':'#A8D8F1',
                                      'mid_color':'#FFFFFF',
                                      'max_color':'#F26161'})
workbook.close()
h=input()
"""
tabla1=np.array(tabla1)