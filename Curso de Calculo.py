import tkinter as tk
from tkinter import messagebox
import sympy as sp

class FormBtnsCalculo:
    def __init__(self):
        self.vMain = tk.Tk()
        self.vMain.title("Ventana Principal")
        self.vMain.geometry('700x550')
        self.vMain.iconbitmap("logo.ico")
        self.vMain.resizable(0, 0)
        self.vMain.config(bg="#f0f0f0")

        # Marco principal para centrar los contenidos
        marco_principal = tk.Frame(self.vMain, bg="#f0f0f0")
        marco_principal.pack(expand=True, fill='both', padx=20, pady=20)

        # Marco interno para los elementos
        marco_elementos = tk.Frame(marco_principal, bg="#f0f0f0")
        marco_elementos.pack(expand=True, fill='both')

        # Espaciador para empujar el botón hacia abajo
        marco_elementos.columnconfigure(0, weight=6)
        marco_elementos.rowconfigure(0, weight=1)

        estilo_btn = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 20, 'bold')}
        btn_ejercicio = tk.Button(marco_elementos, text="EJERCICIO", command=self.abrir_nueva_ventana, **estilo_btn)
        btn_ejercicio.grid(row=1, column=0, pady=(0, 20))

        # Centrar la ventana principal
        self.centrar_ventana(self.vMain, 700, 550)
        
        self.vMain.mainloop()

    def centrar_ventana(self, ventana, ancho_ventana, alto_ventana):
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2
        ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

    def abrir_nueva_ventana(self):
        self.vMain.destroy()  # Cierra la ventana principal

        self.vNuevaVentana = tk.Toplevel()
        self.vNuevaVentana.title("Ejercicio")
        self.vNuevaVentana.geometry('500x300')
        self.vNuevaVentana.iconbitmap("logo.ico")
        self.vNuevaVentana.resizable(0, 0)
        self.vNuevaVentana.config(bg="white")
        
        self.centrar_ventana(self.vNuevaVentana, 500, 300)

        label_problema = tk.Label(self.vNuevaVentana, text="Problema: Encuentra el punto en el que la función f(x)=3x2-12x+7 tiene un mínimo.", 
                                  bg="white", fg="black", font=("Arial", 15), wraplength=400, justify="center")
        label_problema.pack(pady=20)

        estilo_btn = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 13, 'bold')}
        btn_abrir_pizarra = tk.Button(self.vNuevaVentana, width=28, text="Abrir Pizarra Digital", command=self.abrir_pizarra, **estilo_btn)
        btn_abrir_pizarra.pack(pady=20)

    def abrir_pizarra(self):
        self.vNuevaVentana.destroy()
        root_pizarra = tk.Toplevel()
        pizarra = PizarraDigital(root_pizarra, self)
        root_pizarra.mainloop()

    def abrir_calculadora(self):
        self.vCalculadora = tk.Toplevel()
        self.vCalculadora.title("Curso de Cálculo")
        self.vCalculadora.geometry('700x570')
        self.vCalculadora.iconbitmap("logo.ico")
        self.vCalculadora.resizable(0, 0)
        self.vCalculadora.config(bg="#f0f0f0")
        
        self.centrar_ventana(self.vCalculadora, 700, 570)
        
        self.crear_widgets()
        self.vCalculadora.mainloop()

    def crear_widgets(self):
        # Marco principal
        marco_calculadora = tk.Frame(self.vCalculadora, bg="#f0f0f0")
        marco_calculadora.pack(expand=True, fill='both', padx=20, pady=20)

        # Etiqueta y entrada para la función
        tk.Label(marco_calculadora, text="Ingrese la función (use 'x' como variable):", bg="#f0f0f0", fg="#333", font=("Verdana", 12)).pack(pady=10)
        self.funcion_entry = tk.Entry(marco_calculadora, width=50, bd=2, relief="groove", font=("Arial", 12))  # Borde del campo de entrada
        self.funcion_entry.pack(pady=10)
        tk.Label(marco_calculadora, text="(Por ejemplo: f(x)=x2+3x−sin(x) Se expresara como: x**2 + 3*x - sin(x))", bg="#f0f0f0", fg="#669", font=("Arial", 10, "italic")).pack()

        # Marco para los botones
        marco_botones = tk.Frame(marco_calculadora, bg="#f0f0f0")
        marco_botones.pack(pady=10)

        # Botones para derivar, integrar y borrar todo
        derivar_btn = tk.Button(marco_botones, text="Derivar", command=self.derivar, bg="#9DC3E6", fg="black", bd=2, relief="raised", width=10, font=("Arial", 12))  # Botón azul pastel
        derivar_btn.grid(row=0, column=0, padx=5)
        integrar_btn = tk.Button(marco_botones, text="Integrar", command=self.integrar, bg="#DAC0E8", fg="black", bd=2, relief="raised", width=10, font=("Arial", 12))  # Botón azul pastel
        integrar_btn.grid(row=0, column=1, padx=5)
        borrar_btn = tk.Button(marco_botones, text="Borrar todo", command=self.borrar_todo, bg="#B7CE63", fg="black", bd=2, relief="raised", width=10, font=("Arial", 12))  # Botón verde pastel
        borrar_btn.grid(row=0, column=2, padx=5)


        # Text area para mostrar resultados
        self.resultado_text = tk.Text(marco_calculadora, height=15, width=80, bg="#D8BFD8", bd=2, relief="groove", font=("Arial", 12))
        self.resultado_text.pack(pady=20)

        # Define los tags para texto en rojo
        self.resultado_text.tag_configure("rojo", foreground="red")

    def derivar(self):
        funcion = self.funcion_entry.get()
        if not funcion:
            messagebox.showerror("Error", "Por favor ingrese una función.")
            return
        x = sp.symbols('x')
        try:
            funcion_sympy = sp.sympify(funcion)
            derivada = sp.diff(funcion_sympy, x)
            procedimiento = self.obtener_procedimiento_derivada(funcion_sympy)
            self.resultado_text.delete(1.0, tk.END)
            self.resultado_text.insert(tk.END, f"Función original: {funcion}\n\n")
            self.resultado_text.insert(tk.END, f"Derivada: {derivada}\n\n")
            self.resultado_text.insert(tk.END, f"Procedimiento de derivación:\n", "rojo")  # Inserta en rojo
            self.resultado_text.insert(tk.END, procedimiento)
        except Exception as e:
            messagebox.showerror("Error", f"Error al derivar la función: {e}")

    def integrar(self):
        funcion = self.funcion_entry.get()
        if not funcion:
            messagebox.showerror("Error", "Por favor ingrese una función.")
            return
        
        x = sp.symbols('x')
        try:
            funcion_sympy = sp.sympify(funcion)
            integral = sp.integrate(funcion_sympy, x)
            procedimiento = self.obtener_procedimiento_integral(funcion_sympy)
            # Modificar la presentación de la integral
            integral_formateada = f"Integral de ({funcion}) dx = {integral}\n\nProcedimiento:\n{procedimiento}"
            self.resultado_text.delete(1.0, tk.END)
            self.resultado_text.insert(tk.END, f"Integral de: ({funcion}) dx = {integral}\n\nProcedimiento:\n", "rojo")  # Inserta en rojo
            self.resultado_text.insert(tk.END, procedimiento)
        except Exception as e:
            messagebox.showerror("Error", f"Error al integrar la función: {e}")

    def borrar_todo(self):
        self.funcion_entry.delete(0, tk.END)
        self.resultado_text.delete(1.0, tk.END)

    def obtener_procedimiento_derivada(self, funcion):
        pasos = []
        derivada_anterior = funcion
        for _ in range(10):  
            derivada = sp.diff(derivada_anterior)
            paso = f"Derivada de: {sp.pretty(derivada_anterior)} = {sp.pretty(derivada)}"
            pasos.append(paso)
            if derivada == 0:
                break  # Detenerse si la derivada es cero
            derivada_anterior = derivada
        return "\n".join(pasos)

    def obtener_procedimiento_integral(self, funcion):
        try:
            pasos = []
            integral_anterior = funcion
            for _ in range(10):  # Supongamos que queremos 3 pasos
                integral = sp.integrate(integral_anterior)
                paso = f"Integral de: {sp.pretty(integral_anterior)} dx = {sp.pretty(integral)}"
                pasos.append(paso)
                integral_anterior = integral
            return "\n".join(pasos)
        except Exception as e:
            return f"Error al calcular el procedimiento: {e}"

class PizarraDigital:
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent
        self.root.title("Pizarrón Digital")

        ancho_ventana = 700
        alto_ventana = 600
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2
        self.root.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

        self.canvas = tk.Canvas(self.root, bg='white', width=700, height=570)
        self.canvas.pack()

        self.dibujando = False
        self.borrando = False

        self.canvas.bind("<B1-Motion>", self.dibujar_o_borrar)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.boton_borrar_todo = tk.Button(self.root, text="Borrar Todo", bg="#02CA2A", fg="white", font=("Arial", 10), command=self.borrar_todo)
        self.boton_borrar_todo.pack(side=tk.LEFT)

        self.boton_goma = tk.Button(self.root, text="Goma", bg="#5BBCBE", fg="white", font=("Arial", 10), command=self.activar_goma)
        self.boton_goma.pack(side=tk.LEFT)

        self.boton_lapiz = tk.Button(self.root, text="Lápiz", bg="#F8900B", fg="white", font=("Arial", 10), command=self.activar_lapiz)
        self.boton_lapiz.pack(side=tk.LEFT)

        self.boton_verificar = tk.Button(self.root, text="Verificar Respuesta", bg="#FE5151", fg="white", font=("Arial", 10), command=self.verificar_respuesta)
        self.boton_verificar.pack(side=tk.LEFT)

    def dibujar_o_borrar(self, event):
        if self.borrando:
            self.borrar(event)
        else:
            self.dibujar(event)

    def dibujar(self, event):
        if not self.dibujando:
            self.dibujando = True
            self.x1, self.y1 = event.x, event.y
        self.x2, self.y2 = event.x, event.y
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", width=2)
        self.x1, self.y1 = self.x2, self.y2

    def borrar(self, event):
        borrar_area = 12  # Tamaño de la goma
        items = self.canvas.find_overlapping(event.x - borrar_area, event.y - borrar_area,
                                             event.x + borrar_area, event.y + borrar_area)
        for item in items:
            self.canvas.delete(item)

    def reset(self, event):
        self.dibujando = False

    def borrar_todo(self):
        self.canvas.delete("all")

    def activar_goma(self):
        self.borrando = True

    def activar_lapiz(self):
        self.borrando = False

    def verificar_respuesta(self):
        self.root.destroy()
        self.parent.abrir_calculadora()

if __name__ == "__main__":
    FormBtnsCalculo()
