import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class VentanaPrincipal:
    def __init__(self):
        self.app = QApplication([])
        self.root = tk.Tk()
        self.configurar_ventana()
        self.crear_interfaz()

    def configurar_ventana(self):
        self.root.title("Biología Actividad Interactiva")
        self.root.geometry('700x570')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(0, 0)
        self.root.config(bg="#f0f0f0")

    def abrir_video(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Video")
        self.top.geometry('700x570')
        self.top.resizable(False, False)
        self.top.config(bg="#000000")  # Fondo negro para mejorar la visualización del video

        browser = QWebEngineView()
        browser.setUrl(QUrl("https://youtu.be/H5v3kku4y6Q?si=jfe1Lf7I37EriJ1Q"))
        browser.show()

        self.top.wait_window(browser)  # Esperar hasta que el navegador cierre

        self.top.destroy()  # Cierra la ventana del video
        self.root.deiconify()  # Hacer visible nuevamente la ventana principal



    def centrar_ventana(self, ventana, ancho_ventana, alto_ventana):
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2
        ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

    def crear_interfaz(self):
        marco_principal = tk.Frame(self.root, bg="#f0f0f0")
        marco_principal.pack(expand=True, fill='both', padx=20, pady=(20, 0))

        frame_central = tk.Frame(marco_principal, bg="#f0f0f0")
        frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        estilo_btn = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 20, 'bold')}
        btn_video = tk.Button(marco_principal, text="Ver Video", command=self.abrir_video, **estilo_btn)
        btn_video.pack(pady=(20, 50))  # Ajusta la posición según sea necesario

        self.comentario = tk.Label(frame_central, text="Muy bien, una vez comprendiste el curso es la hora de realizar un ejercicio\n¡Por favor presiona el siguiente botón!", bg="#f0f0f0", fg="gray", font=("Arial", 15))
        self.comentario.pack(pady=(0, 10))

        btn_ejercicio = tk.Button(marco_principal, text="EJERCICIO", command=self.abrir_ventana_ejercicio, **estilo_btn)
        btn_ejercicio.pack(side=tk.BOTTOM, pady=(20, 50))
    # Código existente...

        self.centrar_ventana(self.root, 700, 570)
        self.root.mainloop()

    def abrir_ventana_ejercicio(self):
        self.root.withdraw()
        ventana_ejercicio = VentanaEjercicio(self.root, "logo.ico", self.actualizar_comentario)
        self.root.wait_window(ventana_ejercicio.top)
        self.root.deiconify()

    def actualizar_comentario(self, tema):
        self.comentario.config(text=f"Selecciona la imagen relacionada con: {tema}")


class VentanaEjercicio:
    def __init__(self, parent, icono, callback_actualizar_comentario):
        self.parent = parent
        self.top = tk.Toplevel(parent)
        self.configurar_ventana(icono)
        self.callback_actualizar_comentario = callback_actualizar_comentario
        self.inicializar_variables()

    def configurar_ventana(self, icono):
        self.top.title("Ejercicio")
        self.top.geometry('700x570')
        self.top.iconbitmap(icono)
        self.top.resizable(0, 0)
        self.top.config(bg="white")  # Cambiar el fondo a blanco

    def inicializar_variables(self):
        self.selecciones_realizadas = 0
        self.temas_seleccionados = []
        self.temas_biologia = [
            "Biología celular",
            "Genética",
            "Evolución",
            "Ecología"
        ]
        self.explicaciones = {
            "Biología celular": "La biología celular estudia las células, unidades fundamentales de la vida.",
            "Genética": "La genética investiga la herencia y la variación de los organismos.",
            "Evolución": "La teoría de la evolución explica cómo cambian las especies a lo largo del tiempo.",
            "Ecología": "La ecología estudia las interacciones entre los organismos y su entorno."
        }
        self.crear_interfaz_ejercicio()

    def crear_interfaz_ejercicio(self):
        self.label_comentario = tk.Label(self.top, text="Selecciona la imagen relacionada con:", bg="white", font=("Arial", 12))
        self.label_comentario.pack(pady=10)

        self.tema_actual = tk.StringVar()
        self.actualizar_tema()

        self.label_tema = tk.Label(self.top, textvariable=self.tema_actual, bg="white", font=("Arial", 14, "bold"))
        self.label_tema.pack(pady=10)

        self.frame_arriba = tk.Frame(self.top, bg="white")
        self.frame_arriba.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.frame_abajo = tk.Frame(self.top, bg="white")
        self.frame_abajo.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.cargar_imagenes()
        self.centrar_ventana(self.top, 700, 570)
        self.top.protocol("WM_DELETE_WINDOW", self.cerrar_ventanas)

    def centrar_ventana(self, ventana, ancho_ventana, alto_ventana):
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2
        ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

    def cerrar_ventanas(self):
        self.top.destroy()
        self.parent.destroy()

    def actualizar_tema(self):
        tema_random = random.choice(self.temas_biologia)
        while tema_random in self.temas_seleccionados:
            tema_random = random.choice(self.temas_biologia)
        self.tema_actual.set(tema_random)
        self.callback_actualizar_comentario(tema_random)

    def cargar_imagenes(self):
        self.imagen_paths = ['Imagen1.png', 'Imagen2.png', 'Imagen3.png', 'Imagen4.png']
        self.imagenes = []
        self.labels_imagenes = []

        for i, path in enumerate(self.imagen_paths):
            try:
                imagen = Image.open(path)
                imagen = imagen.resize((150, 150), Image.LANCZOS)
                imagen = ImageTk.PhotoImage(imagen)
                self.imagenes.append(imagen)

                if i < 2:
                    frame = self.frame_arriba
                else:
                    frame = self.frame_abajo

                label_imagen = tk.Label(frame, image=imagen, bg="white", padx=10, pady=10)
                label_imagen.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
                label_imagen.bind("<Button-1>", lambda event, index=i: self.imagen_seleccionada(event, index))
                self.labels_imagenes.append(label_imagen)

            except Exception as e:
                print(f"Error loading image {path}: {e}")
                self.imagenes.append(None)

    def imagen_seleccionada(self, event, index):
        tema_actual = self.tema_actual.get()
        tema_correcto_index = self.temas_biologia.index(tema_actual)

        if index == tema_correcto_index:
            mensaje_correcto = f"La imagen {index+1} es correcta para el tema {tema_actual}. "
            mensaje_correcto += self.explicaciones[tema_actual]
            messagebox.showinfo("¡Correcto!", mensaje_correcto)
            self.selecciones_realizadas += 1
            self.temas_seleccionados.append(tema_actual)
            if self.selecciones_realizadas < 4:
                self.actualizar_tema()
            else:
                messagebox.showinfo("Actividad completada", "Excelente completaste la actividad.")
                self.cerrar_ventanas()
        else:
            mensaje_incorrecto = f"La imagen {index+1} no es correcta para el tema {tema_actual}. "
            mensaje_incorrecto += self.explicaciones[tema_actual]
            messagebox.showerror("Incorrecto", mensaje_incorrecto)

if __name__ == "__main__":
    ventana = VentanaPrincipal()