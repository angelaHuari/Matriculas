import tkinter as tk
from tkinter import messagebox
from .estudiantes import agregar_estudiante, obtener_estudiantes
from .cursos import agregar_curso, obtener_cursos
from .matriculas import matricular, obtener_matriculas

def iniciar_gui():
    ventana = tk.Tk()
    ventana.title("Sistema de Matrículas")
    ventana.geometry("600x500")

    # Sección de estudiantes
    tk.Label(ventana, text="Nombre del estudiante").pack()
    entry_estudiante = tk.Entry(ventana)
    entry_estudiante.pack()

    def agregar_est():
        nombre = entry_estudiante.get()
        if nombre:
            agregar_estudiante(nombre)
            messagebox.showinfo("Éxito", "Estudiante agregado.")
            entry_estudiante.delete(0, tk.END)
            actualizar_listas()

    tk.Button(ventana, text="Agregar Estudiante", command=agregar_est).pack()

    # Lista de estudiantes
    tk.Label(ventana, text="Estudiantes agregados").pack()
    listbox_estudiantes = tk.Listbox(ventana, height=5)
    listbox_estudiantes.pack()

    # Sección de cursos
    tk.Label(ventana, text="Nombre del curso").pack()
    entry_curso = tk.Entry(ventana)
    entry_curso.pack()

    def agregar_cur():
        nombre = entry_curso.get()
        if nombre:
            agregar_curso(nombre)
            messagebox.showinfo("Éxito", "Curso agregado.")
            entry_curso.delete(0, tk.END)
            actualizar_listas()

    tk.Button(ventana, text="Agregar Curso", command=agregar_cur).pack()

    # Lista de cursos
    tk.Label(ventana, text="Cursos disponibles").pack()
    listbox_cursos = tk.Listbox(ventana, height=5)
    listbox_cursos.pack()

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
            actualizar_listas()
        except ValueError:
            messagebox.showerror("Error", "IDs inválidos.")

    tk.Button(ventana, text="Matricular Estudiante", command=matricular_gui).pack()

    # Lista de matrículas
    tk.Label(ventana, text="Matrículas registradas").pack()
    listbox_matriculas = tk.Listbox(ventana, height=5)
    listbox_matriculas.pack()

    # Ver matrículas
    def mostrar_matriculas_gui():
        lista = obtener_matriculas()
        messagebox.showinfo("Matrículas", "\n".join(lista) if lista else "No hay matrículas registradas.")

    tk.Button(ventana, text="Ver Matrículas", command=mostrar_matriculas_gui).pack()

    # Función para actualizar las listas
    def actualizar_listas():
        # Limpiar las listas
        listbox_estudiantes.delete(0, tk.END)
        listbox_cursos.delete(0, tk.END)
        listbox_matriculas.delete(0, tk.END)

        # Obtener y mostrar estudiantes
        estudiantes = obtener_estudiantes()
        for estudiante in estudiantes:
            listbox_estudiantes.insert(tk.END, estudiante)

        # Obtener y mostrar cursos
        cursos = obtener_cursos()
        for curso in cursos:
            listbox_cursos.insert(tk.END, curso)

        # Obtener y mostrar matrículas
        matriculas = obtener_matriculas()
        for matricula in matriculas:
            listbox_matriculas.insert(tk.END, matricula)

    # Inicializar las listas al iniciar la GUI
    actualizar_listas()

    ventana.mainloop()
