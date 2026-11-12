def limpiar_feed(publicaciones):
    
    if len(publicaciones) <= 1:
        return publicaciones

    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])

    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

publicaciones = ["Post A", "Post D", "Post D", "Post C", "Post B"]

print("PUBLICACIONES ORIGINALES")
print(publicaciones)

resultado = limpiar_feed(publicaciones)

print("PUBLICACIONES SIN DUPLICADOS")
print(resultado)