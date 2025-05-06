from .datos import matriculas
from .estudiantes import obtener_estudiante_por_id
from .cursos import obtener_curso_por_id

def matricular(estudiante_id, curso_id):
    matriculas.append({"estudiante_id": estudiante_id, "curso_id": curso_id})

def obtener_matriculas():
    lista = []
    for m in matriculas:
        estudiante = obtener_estudiante_por_id(m["estudiante_id"])
        curso = obtener_curso_por_id(m["curso_id"])
        if estudiante and curso:
            lista.append(f"{estudiante['nombre']} está matriculado en {curso['nombre']}")
    return lista
