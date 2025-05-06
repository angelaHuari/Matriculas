from .datos import estudiantes

def agregar_estudiante(nombre):
    estudiante_id = len(estudiantes) + 1
    estudiantes.append({"id": estudiante_id, "nombre": nombre})
    return estudiante_id

def obtener_estudiante_por_id(estudiante_id):
    return next((e for e in estudiantes if e["id"] == estudiante_id), None)
