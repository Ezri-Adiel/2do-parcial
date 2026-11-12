#EJERCICIO 2: PROYECCION DE AHORRO

def calcular_saldo_final(depositos, tasa_interes):

    #CASO BASE
    if len(depositos) == 0:
        return 0.0

    #CASO RECURSIVO
    else:
        saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
        saldo_nuevo = (saldo_anterior + depositos[-1]) * (1 + tasa_interes)
        return saldo_nuevo



depositos = [1000, 2000, 1500]
tasa_interes = 0.05


resultado = calcular_saldo_final(depositos, tasa_interes)

print("..PROYECCION DE AHORRO..")
print(f"SALDO FINAL: ${resultado:.2f}")
