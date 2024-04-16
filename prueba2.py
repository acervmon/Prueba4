def asignar_recursos(tipo_mision, reino_destino, dios_solicitante):
    if dios_solicitante == "Odín" or dios_solicitante == "Loki":
        prioridad = "alta"
    else:
        prioridad = "normal"
    
    if tipo_mision == "defensa":
        valkirias = 5
        unidades = 100
    elif tipo_mision == "exploración":
        valkirias = 3
        unidades = 50
    elif tipo_mision == "conquista":
        valkirias = 10
        unidades = 200
    else:
        valkirias = 0
        unidades = 0
    
    print(f"Recursos asignados para la misión: Valkirias: {valkirias}, Unidades: {unidades}, Prioridad: {prioridad}")

# Ejemplo de uso
tipo_mision = input("Ingrese el tipo de misión (defensa, exploración, conquista): ")
reino_destino = input("Ingrese el reino destino: ")
dios_solicitante = input("Ingrese el dios que solicitó la misión: ")

asignar_recursos(tipo_mision, reino_destino, dios_solicitante)
