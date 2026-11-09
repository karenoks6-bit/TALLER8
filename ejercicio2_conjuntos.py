def main():
    # Conjuntos iniciales de estudiantes inscritos
    curso_A = {"Ana", "Carlos", "Laura", "Pedro", "Sofia", "Andres", "Camila"}
    curso_B = {"Laura", "Pedro", "Daniel", "Sofia", "Mateo", "Valentina"}

    print("=" * 65)
    print("      ANÁLISIS DE PARTICIPACIÓN EN CURSOS (SET OPERATIONS)")
    print("=" * 65)

    # 1. Mostrar inscritos en cada curso
    print("\n1. ESTUDIANTES INSCRITOS POR CURSO:")
    print(f" - Curso A (Programación): {curso_A}")
    print(f" - Curso B (Bases de Datos): {curso_B}")

    # 2. Total de estudiantes diferentes inscritos (Unión)
    todos_estudiantes = curso_A | curso_B
    print(f"\n2. TOTAL DE ESTUDIANTES DIFERENTES ({len(todos_estudiantes)}):")
    print(f"   {todos_estudiantes}")

    # 3. Estudiantes en ambos cursos (Intersección)
    ambos_cursos = curso_A & curso_B
    print(f"\n3. ESTUDIANTES INSCRITOS EN AMBOS CURSOS ({len(ambos_cursos)}):")
    print(f"   {ambos_cursos}")

    # 4. Estudiantes únicamente en el Curso A (Diferencia A - B)
    solo_A = curso_A - curso_B
    print(f"\n4. ESTUDIANTES ÚNICAMENTE EN CURSO A ({len(solo_A)}):")
    print(f"   {solo_A}")

    # 5. Estudiantes únicamente en el Curso B (Diferencia B - A)
    solo_B = curso_B - curso_A
    print(f"\n5. ESTUDIANTES ÚNICAMENTE EN CURSO B ({len(solo_B)}):")
    print(f"   {solo_B}")

    # 6. Estudiantes en exactamente uno de los cursos (Diferencia Simétrica)
    exactamente_uno = curso_A ^ curso_B
    print(f"\n6. ESTUDIANTES EN EXACTAMENTE UN CURSO ({len(exactamente_uno)}):")
    print(f"   {exactamente_uno}")

    # 7. Evaluar si todos los del Curso A están en el Curso B (Subconjunto)
    es_subconjunto = curso_A.issubset(curso_B)
    print(f"\n7. ¿TODOS LOS ESTUDIANTES DEL CURSO A ESTÁN EN EL CURSO B?: {es_subconjunto}")

    # 8. Agregar un nuevo estudiante de forma dinámica
    print("\n" + "=" * 65)
    print("8. AGREGAR NUEVO ESTUDIANTE")
    print("=" * 65)
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ").strip()
    opcion_curso = input("¿A qué curso desea agregarlo? (A/B/Ambos): ").strip().upper()

    if opcion_curso == "A":
        curso_A.add(nuevo_estudiante)
    elif opcion_curso == "B":
        curso_B.add(nuevo_estudiante)
    elif opcion_curso == "AMBOS":
        curso_A.add(nuevo_estudiante)
        curso_B.add(nuevo_estudiante)
    else:
        print("[X] Opción inválida. No se realizaron cambios.")

    print("\n[✓] RESULTADOS ACTUALIZADOS TRAS LA INSERCIÓN:")
    print(f" - Curso A actualizado: {curso_A}")
    print(f" - Curso B actualizado: {curso_B}")
    print(f" - Nueva Intersección (Ambos): {curso_A & curso_B}")

if __name__ == "__main__":
    main()
