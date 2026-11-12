#EJERCICIO 3: PROFUNDIDAD DE COMENTARIOS

def maxima_profundidad(comentarios):

    #CASO BASE
    if len(comentarios) == 0:
        return 0

    #CASO RECURSIVO
    profundidad_maxima = 0

    for elemento in comentarios:

        
        if isinstance(elemento, list):
            profundidad = 1 + maxima_profundidad(elemento)

        
        else:
            profundidad = 1

        
        if profundidad > profundidad_maxima:
            profundidad_maxima = profundidad

    return profundidad_maxima



hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]


resultado = maxima_profundidad(hilo)


print("..PROFUNDIDAD DE COMENTARIOS..")
print("PROFUNDIDAD MAXIMA:", resultado)
