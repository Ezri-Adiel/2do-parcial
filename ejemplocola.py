from collections import deque
import time

cola_turnos = deque()

#AGREGAR CLIENTES A LA COLA (ENColar)
cola_turnos.append("Turno A01 - ISIDRO ORTIZ RAMIREZ")
cola_turnos.append("Turno A02 - GUADALUPE PEREZ DIAZ")
cola_turnos.append("Turno A03 - JUANA LAZCANO RODRIGUEZ")

#MOSTRAR LOS TURNOS EN ESPERA
print("Turnos emitidos en la fila del banco:")
for turno in cola_turnos:
    print("-", turno)

print("\nIniciando atención en ventanilla\n")

#EL CAJERO PROCESA LA COLA, CLIENTE POR CLIENTE
#DESENCOLAR
while cola_turnos:
    turno_actual = cola_turnos.popleft()
    print(f"Llamando a ventanilla: {turno_actual}")
    
    time.sleep(1) #SIMULA EL TIEMPO DE ATENCION EN VENTANILLA
    
    print(f"Atención finalizada: {turno_actual}")
    
    #MUESTRA CUANTOS CLIENTES QUEDAN EN LA COLA
    print(f" (Clientes restantes en la fila: {len(cola_turnos)})")
    print() # Espacio en blanco para separar cada atención

print("Se han atendido todos los turnos. Fila vacía.")