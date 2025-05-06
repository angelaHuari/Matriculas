import tkinter as tk
from tkinter import messagebox
from .estudiantes import agregar_estudiante
from .cursos import agregar_curso
from .matriculas import matricular, obtener_matriculas

def iniciar_gui():
    ventana = tk.Tk()
    ventana.title("Sistema de Matrículas")
    ventana.geometry("400x400")

    # Entrada estudiante
    tk.Label(ventana, text="Nombre del estudiante").pack()
    entry_estudiante = tk.Entry(ventana)
    entry_estudiante.pack()
    
    def agregar_est():
        nombre = entry_estudiante.get()
        if nombre:
            agregar_estudiante(nombre)
            messagebox.showinfo("Éxito", "Estudiante agregado.")
            entry_estudiante.delete(0, tk.END)

    tk.Button(ventana, text="Agregar Estudiante", command=agregar_est).pack()

    # Entrada curso
    tk.Label(ventana, text="Nombre del curso").pack()
    entry_curso = tk.Entry(ventana)
    entry_curso.pack()

    def agregar_cur():
        nombre = entry_curso.get()
        if nombre:
            agregar_curso(nombre)
            messagebox.showinfo("Éxito", "Curso agregado.")
            entry_curso.delete(0, tk.END)

    tk.Button(ventana, text="Agregar Curso", command=agregar_cur).pack()

    # Matrícula
    tk.Label(ventana, text="ID Estudiante").pack()
    entry_id_est = tk.Entry(ventana)
    entry_id_est.pack()

    tk.Label(ventana, text="ID Curso").pack()
    entry_id_curso = tk.Entry(ventana)
    entry_id_curso.pack()

    def matricular_gui():
        try:
            est_id = int(entry_id_est.get())
            cur_id = int(entry_id_curso.get())
            matricular(est_id, cur_id)
            messagebox.showinfo("Éxito", "Estudiante matriculado.")
            entry_id_est.delete(0, tk.END)
            entry_id_curso.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "IDs inválidos.")

    tk.Button(ventana, text="Matricular Estudiante", command=matricular_gui).pack()

    # Ver matrículas
    def mostrar_matriculas_gui():
        lista = obtener_matriculas()
        messagebox.showinfo("Matrículas", "\n".join(lista) if lista else "No hay matrículas registradas.")

    tk.Button(ventana, text="Ver Matrículas", command=mostrar_matriculas_gui).pack()

    ventana.mainloop()
