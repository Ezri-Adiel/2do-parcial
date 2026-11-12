A = [[10,15],[20,5]]
B = [[5,12],[15,8]]

suma = [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("..TOTAL DE VENTAS..")
print(suma)

precio = 50
ingresos = [[suma[i][j]*precio for j in range(len(suma[0]))] for i in range(len(suma))]

print("..INGRESOS TOTALES..")
print(ingresos)
