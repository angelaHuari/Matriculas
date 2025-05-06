from .datos import cursos

def agregar_curso(nombre):
    curso_id = len(cursos) + 1
    cursos.append({"id": curso_id, "nombre": nombre})
    return curso_id

def obtener_curso_por_id(curso_id):
    return next((c for c in cursos if c["id"] == curso_id), None)

def obtener_cursos():
    # Retorna una lista de nombres de cursos
    return [c["nombre"] for c in cursos]