def factorial(n):
    # 1. Caso base: si n es 1 o 0, el factorial es 1
    if n == 0 or n == 1:
        return 1
    
    # 2. Caso recursivo: n multiplicado por el factorial de n - 1
    return n * factorial(n - 1)

# Probamos la función
resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")  # Salida: 120
