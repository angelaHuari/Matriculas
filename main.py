# from modulos.interfaz import iniciar_gui

# if __name__ == "__main__":
#     iniciar_gui()


# # sistema_matriculas_monolitico.py

import tkinter as tk
from tkinter import messagebox

# Listas de datos
estudiantes = []
cursos = []
matriculas = []

# Funciones
def agregar_estudiante_gui():
    nombre = entry_nombre_estudiante.get()
    if not nombre:
        messagebox.showwarning("Error", "Ingresa un nombre.")
        return
    estudiante_id = len(estudiantes) + 1
    estudiantes.append({"id": estudiante_id, "nombre": nombre})
    entry_nombre_estudiante.delete(0, tk.END)
    messagebox.showinfo("Éxito", f"Estudiante agregado con ID {estudiante_id}")

def agregar_curso_gui():
    nombre = entry_nombre_curso.get()
    if not nombre:
        messagebox.showwarning("Error", "Ingresa un nombre.")
        return
    curso_id = len(cursos) + 1
    cursos.append({"id": curso_id, "nombre": nombre})
    entry_nombre_curso.delete(0, tk.END)
    messagebox.showinfo("Éxito", f"Curso agregado con ID {curso_id}")

def matricular_estudiante_gui():
    try:
        estudiante_id = int(entry_id_estudiante.get())
        curso_id = int(entry_id_curso.get())
    except ValueError:
        messagebox.showwarning("Error", "IDs deben ser números.")
        return
    if not any(e["id"] == estudiante_id for e in estudiantes):
        messagebox.showerror("Error", "Estudiante no encontrado.")
        return
    if not any(c["id"] == curso_id for c in cursos):
        messagebox.showerror("Error", "Curso no encontrado.")
        return
    matriculas.append({"estudiante_id": estudiante_id, "curso_id": curso_id})
    entry_id_estudiante.delete(0, tk.END)
    entry_id_curso.delete(0, tk.END)
    messagebox.showinfo("Éxito", "Estudiante matriculado correctamente.")

def mostrar_matriculas_gui():
    texto = ""
    for m in matriculas:
        estudiante = next(e for e in estudiantes if e["id"] == m["estudiante_id"])
        curso = next(c for c in cursos if c["id"] == m["curso_id"])
        texto += f"{estudiante['nombre']} está matriculado en {curso['nombre']}\n"
    if texto == "":
        texto = "No hay matrículas registradas."
    messagebox.showinfo("Matrículas", texto)

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Matrículas")

# Sección Agregar Estudiante
tk.Label(root, text="Agregar Estudiante").grid(row=0, column=0, pady=5)
entry_nombre_estudiante = tk.Entry(root)
entry_nombre_estudiante.grid(row=0, column=1)
tk.Button(root, text="Agregar", command=agregar_estudiante_gui).grid(row=0, column=2)

# Sección Agregar Curso
tk.Label(root, text="Agregar Curso").grid(row=1, column=0, pady=5)
entry_nombre_curso = tk.Entry(root)
entry_nombre_curso.grid(row=1, column=1)
tk.Button(root, text="Agregar", command=agregar_curso_gui).grid(row=1, column=2)

# Sección Matricular Estudiante
tk.Label(root, text="ID Estudiante").grid(row=2, column=0, pady=5)
entry_id_estudiante = tk.Entry(root)
entry_id_estudiante.grid(row=2, column=1)

tk.Label(root, text="ID Curso").grid(row=3, column=0, pady=5)
entry_id_curso = tk.Entry(root)
entry_id_curso.grid(row=3, column=1)

tk.Button(root, text="Matricular", command=matricular_estudiante_gui).grid(row=3, column=2)

# Botón para mostrar matrículas
tk.Button(root, text="Mostrar Matrículas", command=mostrar_matriculas_gui).grid(row=4, column=0, columnspan=3, pady=10)

# Ejecutar interfaz
root.mainloop()
