from modulos.interfaz import iniciar_gui

if __name__ == "__main__":
    iniciar_gui()


# # sistema_matriculas_monolitico.py

# estudiantes = []
# cursos = []
# matriculas = []

# def agregar_estudiante():
#     nombre = input("Nombre del estudiante: ")
#     estudiante_id = len(estudiantes) + 1
#     estudiantes.append({"id": estudiante_id, "nombre": nombre})
#     print(f"Estudiante agregado con ID {estudiante_id}")

# def agregar_curso():
#     nombre = input("Nombre del curso: ")
#     curso_id = len(cursos) + 1
#     cursos.append({"id": curso_id, "nombre": nombre})
#     print(f"Curso agregado con ID {curso_id}")

# def matricular_estudiante():
#     estudiante_id = int(input("ID del estudiante: "))
#     curso_id = int(input("ID del curso: "))
#     matriculas.append({"estudiante_id": estudiante_id, "curso_id": curso_id})
#     print("Estudiante matriculado correctamente.")

# def mostrar_matriculas():
#     for m in matriculas:
#         estudiante = next(e for e in estudiantes if e["id"] == m["estudiante_id"])
#         curso = next(c for c in cursos if c["id"] == m["curso_id"])
#         print(f"{estudiante['nombre']} está matriculado en {curso['nombre']}")

# def menu():
#     while True:
#         print("\n1. Agregar estudiante\n2. Agregar curso\n3. Matricular estudiante\n4. Ver matrículas\n5. Salir")
#         opcion = input("Elige una opción: ")
#         if opcion == "1":
#             agregar_estudiante()
#         elif opcion == "2":
#             agregar_curso()
#         elif opcion == "3":
#             matricular_estudiante()
#         elif opcion == "4":
#             mostrar_matriculas()
#         elif opcion == "5":
#             break
#         else:
#             print("Opción inválida.")

# if __name__ == "__main__":
#     menu()
