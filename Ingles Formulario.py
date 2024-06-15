import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

class QuizApp:
    def __init__(self):
        self.vMain = tk.Tk()
        self.vMain.title("Ventana Principal")
        self.vMain.geometry('700x570')
        try:
            self.vMain.iconbitmap("logo.ico")
        except:
            pass  # Manejo del error si no se encuentra el icono
        self.vMain.resizable(0, 0)
        self.vMain.config(bg="#f0f0f0")

        # Marco principal
        marco_principal = tk.Frame(self.vMain, bg="#f0f0f0")
        marco_principal.pack(expand=True, fill='both', padx=20, pady=(20, 0))

       

        # Contenedor para el texto y el botón
        frame_texto_boton = tk.Frame(marco_principal, bg="#f0f0f0")
        frame_texto_boton.pack(side=tk.BOTTOM, pady=(0, 70))

        # Comentario
        comentario = tk.Label(frame_texto_boton, text="Very good, once you understand the course it is time to do an exercise\nPlease press the following button!", bg="#f0f0f0", fg="gray", font=("Arial", 12))
        comentario.pack(pady=(0, 10))

        # Botón "EXERCISE" al fondo de la pantalla
        estilo_btn = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 20, 'bold')}
        btn_ejercicio = tk.Button(frame_texto_boton, text="EXERCISE", command=self.abrir_quiz, **estilo_btn)
        btn_ejercicio.pack(pady=(0, 20))

        # Centrar la ventana principal
        self.centrar_ventana(self.vMain, 700, 570)

        self.vMain.mainloop()

    def centrar_ventana(self, ventana, ancho_ventana, alto_ventana):
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2
        ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

    def abrir_quiz(self):
        # Cerrar la ventana principal
        self.vMain.withdraw()

        # Creamos la ventana del formulario de preguntas
        self.vQuiz = tk.Toplevel(self.vMain)
        self.vQuiz.title("Simple past form")
        try:
            self.vQuiz.iconbitmap("logo.ico")
        except:
            pass  # Manejo del error si no se encuentra el icono
        self.vQuiz.resizable(False, False)

        # Dimensiones de la ventana del quiz
        ancho_ventana = 480
        alto_ventana = 620

        # Dimensiones de la pantalla
        ancho_pantalla = self.vQuiz.winfo_screenwidth()
        alto_pantalla = self.vQuiz.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establece la geometría de la ventana para que esté centrada
        self.vQuiz.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

        # Marco principal para centrar los contenidos
        marco_principal = tk.Frame(self.vQuiz, bg="#E0E0E0", padx=0, pady=0)
        marco_principal.pack(expand=True, fill='both')

        # Estilo de etiquetas
        estilo_label = {"bg": "#E0E0E0", "font": ("Arial", 9)}

        # Preguntas y respuestas
        preguntas_y_respuestas = [
            ("1. What is the basic structure of the Present Simple in English?", ["Subject + infinitive verb + complement", "Subject + auxiliary verb + infinitive main verb + complement", "Subject + verb in the third person singular + complement"]),
            ("2. How is the third person singular formed in affirmative in the Present Simple?", ["Adding \"-ing\" to the end of the verb", "Adding \"-ed\" to the end of the verb", "Adding \"-s\" or \"-es\" to the end of the verb"]),
            ("3. What types of verbs usually use the Present Simple?", ["Action verbs describing ongoing actions", "Modal verbs expressing possibility or necessity", "Verbs describing routines, general facts, or states"]),
            ("4. When do we use the Present Simple to talk about habits and routines?", ["To describe actions in progress at the present moment", "To talk about actions that happened in the past", "To express regular activities or daily habits"]),
            ("5. What is the difference between the Present Simple and the Present Continuous?", ["Temporary actions vs. Permanent actions", "Actions happening now vs. Actions occurring regularly", "Habits and permanent situations vs. Actions happening now"]),
        ]

        # Variables para almacenar respuestas
        self.respuestas = []
        self.labels_respuestas = []

        # Crear preguntas dinámicamente
        for idx, (pregunta, opciones) in enumerate(preguntas_y_respuestas):
            lbl_pregunta = tk.Label(marco_principal, text=pregunta, **estilo_label)
            lbl_pregunta.pack(anchor=tk.W)

            var_respuesta = tk.StringVar()
            self.respuestas.append(var_respuesta)

            frame_opciones = tk.Frame(marco_principal, bg="#E0E0E0")
            frame_opciones.pack(anchor=tk.W)

            opciones_revueltas = opciones[:]
            random.shuffle(opciones_revueltas)

            for opcion in opciones_revueltas:
                rb = tk.Radiobutton(frame_opciones, text=opcion, variable=var_respuesta, value=opcion, **estilo_label)
                rb.pack(anchor=tk.W)

            # Guardar referencia a los labels de respuesta
            lbl_respuesta = tk.Label(marco_principal, text="", **estilo_label)
            self.labels_respuestas.append(lbl_respuesta)
            lbl_respuesta.pack(anchor=tk.W, padx=0, pady=0)  # Ajustar el espacio entre respuestas

        # Botón de enviar
        btn_enviar = tk.Button(marco_principal, text="Submit", command=self.submit_answers, bg="#4CAF50", fg="white", font=("Arial", 12))
        btn_enviar.pack(fill='x', pady=(0, 5), ipady=0)  # Ajustar el botón a lo largo del marco principal

    def submit_answers(self):
        respuestas_correctas = [
            "Subject + verb in the third person singular + complement", 
            "Adding \"-s\" or \"-es\" to the end of the verb", 
            "Verbs describing routines, general facts, or states", 
            "To express regular activities or daily habits", 
            "Habits and permanent situations vs. Actions happening now"
        ]
        respuestas_usuario = [respuesta.get() for respuesta in self.respuestas]

        # Verificar respuestas y mostrar resultado
        preguntas_incorrectas = []
        for idx, (respuesta_usuario, respuesta_correcta) in enumerate(zip(respuestas_usuario, respuestas_correctas)):
            label_respuesta = self.labels_respuestas[idx]

            if respuesta_usuario == respuesta_correcta:
                label_respuesta.config(text=f"Answer: {respuesta_usuario} (Correct)", bg="green")
            else:
                label_respuesta.config(text=f"Answer: {respuesta_usuario} (Incorrect)", bg="red")
                preguntas_incorrectas.append(idx + 1)  # Guardar número de pregunta incorrecta

        # Calcular calificación
        num_respuestas_correctas = sum(1 for ru, rc in zip(respuestas_usuario, respuestas_correctas) if ru == rc)
        calificacion = (num_respuestas_correctas / len(respuestas_correctas)) * 10

        # Mostrar resultados en un messagebox
        if preguntas_incorrectas:
            messagebox.showinfo("Results", f"Score: {calificacion:.2f}\nOops! Maybe you should review the questions: {', '.join(map(str, preguntas_incorrectas))}")
        else:
            messagebox.showinfo("Results", f"Score: {calificacion:.2f}\nAll the answers are correct!")
            # Si todas las respuestas son correctas, cerrar la ventana del quiz
            self.vQuiz.destroy()  # Cierra la ventana del quiz

# Instanciar y ejecutar la aplicación
if __name__ == "__main__":
    app = QuizApp()
