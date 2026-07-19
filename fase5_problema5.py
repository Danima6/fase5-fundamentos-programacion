# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Solución al Problema 5: Control de Horas Semanales

def procesar_y_clasificar_jornada(matriz_datos):
    """
    Módulo (función) encargado de calcular la suma total de horas semanales
    por recurso y clasificar su jornada laboral según el umbral de 40 horas.
    """
    reporte_final = []
    UMBRAL_HORAS = 40
    
    for fila in matriz_datos:
        nombre = fila[0]
        # Sumamos los valores numéricos correspondientes a los días de la semana (Lunes a Viernes)
        total_horas = sum(fila[1:])
        
        # Lógica de negocio para clasificar la jornada laboral
        if total_horas > UBRAL_HORAS:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
            
        # Almacenamos el resultado formateado
        reporte_final.append({
            "nombre": nombre,
            "total_horas": total_horas,
            "clasificacion": clasificacion
        })
        
    return reporte_final


def main():
    # Matriz inicial con 4 recursos y las horas trabajadas por día (Lunes a Viernes)
    # Formato: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
    equipo_trabajo = [
        ["Andrés Pérez", 8, 8, 9, 8, 8],     # Total: 41 horas (Sobretiempo)
        ["Liliana Gómez", 8, 8, 8, 8, 7],    # Total: 39 horas (Horario Estándar)
        ["Carlos Mendoza", 9, 10, 9, 8, 9],  # Total: 45 horas (Sobretiempo)
        ["María Delgado", 8, 8, 8, 8, 8]     # Total: 40 horas (Horario Estándar)
    ]
    
    print("==================================================")
    print("      INFORME DE CONTROL DE HORAS SEMANALES       ")
    print("==================================================")
    
    # Llamado al módulo de procesamiento
    resultados = procesar_y_clasificar_jornada(equipo_trabajo)
    
    # Impresión de la salida solicitada
    for registro in resultados:
        print(f"Recurso: {registro['nombre']}")
        print(f"  - Total Horas Semanales: {registro['total_horas']} hrs")
        print(f"  - Clasificación Jornada: {registro['clasificacion']}")
        print("-" * 50)

# Punto de entrada del script
if __name__ == "__main__":
    main()