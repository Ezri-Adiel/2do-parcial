from collections import deque
import time

cola_turnos = deque()

#Agregar clientes a la cola (ENColar)
cola_turnos.append("Turno A01 - ISIDRO ORTIZ RAMIREZ")
cola_turnos.append("Turno A02 - GUADALUPE PEREZ DIAZ")
cola_turnos.append("Turno A03 - JUANA LAZCANO RODRIGUEZ")

#Mostrar los turnos
print("Turnos emitidos en la fila del banco:")
for turno in cola_turnos:
    print("-", turno)

print("\nIniciando atención en ventanilla\n")

#El cajero procesa la cola, cliente por cliente
#Desencolar
while cola_turnos:
    turno_actual = cola_turnos.popleft()
    print(f"Llamando a ventanilla: {turno_actual}")
    
    time.sleep(1) 
    
    print(f"Atención finalizada: {turno_actual}")
    
    #muestra cuantos clientes hay en la cola
    print(f" (Clientes restantes en la fila: {len(cola_turnos)})")
    print() # Espacio en blanco para separar cada atención

print("Se han atendido todos los turnos. Fila vacía.")