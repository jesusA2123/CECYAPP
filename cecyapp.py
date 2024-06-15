mport tkinteri as tk
from tkinter import *
from tkinter import messagebox, END, Button

import cv2
from time import sleep

from PIL import ImageTk, Image

from DataPropietario import *

class Inicio:
    def __init__(self):
        self.ventanaI = tk.Tk()
        self.ventanaI.title("Inicio")  # Título de ventana
        self.ventanaI.geometry('390x570')  # Dimensiones de la ventana
        self.ventanaI.iconbitmap("logo.ico")  # Icono de la ventana
        self.ventanaI.resizable(0, 0)
        self.ventanaI.config(bg="white")
        # Calcula el tamaño de la pantalla
        ancho_ventanaI = 390
        alto_ventanaI = 570
        ancho_pantallaI = self.ventanaI.winfo_screenwidth()
        alto_pantallaI = self.ventanaI.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        posicion_x = (ancho_pantallaI - ancho_ventanaI) // 2
        posicion_y = (alto_pantallaI - alto_ventanaI) // 2

        # Establece la geometría de la ventana para que esté centrada
        self.ventanaI.geometry(f'{ancho_ventanaI}x{alto_ventanaI}+{posicion_x}+{posicion_y}')

    # Imagen de logo
        image = Image.open("logo.jpg")
        image = image.resize((140, 140))
        imgI = ImageTk.PhotoImage(image)
        lbl_imgI = Label(self.ventanaI, image=imgI, bg="white")
        lbl_imgI.place(x=30, y=20)

    # Imagen de cursos
        image = Image.open("inicio.jpg")
        image = image.resize((240, 170))
        imgC = ImageTk.PhotoImage(image)
        lbl_imgC = Label(self.ventanaI, image=imgC, bg="white")
        lbl_imgC.place(x=85, y=210)
        nApp = Label(self.ventanaI, text="CECYAPP", bg="white", font=("Arial", 20, "bold"), fg="#308935")
        nApp.place(x=200, y=70)

        indicaciones = Label(self.ventanaI, text="Seleccione el modo en que desea usar la App", bg="white", font=("Arial",12), fg="black")
        indicaciones.place(x=40, y=410)
        #Botón para modalidad docente
        btnDocente = tk.Button(self.ventanaI, bg="#9AD99D", text="Docente" , command= self.abrir_ventanaRegistros,font=("Arial", 12, "bold"), fg="black",
                          width=13)
        btnDocente.place(x=40, y=445)
        #Botón para modalidad Estudiante
        btnEstudiante = tk.Button(self.ventanaI, bg="#9AD99D", text="Estudiante" , command= self.abrir_ventanaRegistros, font=("Arial", 12, "bold"), fg="black",
                          width=13)
        btnEstudiante.place(x=218, y=445)

        self.ventanaI.mainloop()


    def abrir_ventanaRegistros(self):
        self.ventanaI.destroy()
        FormRegistro()


class FormCursos:
    #global txtnombre
    #txtnombre = None

    #global txtCurso1
    ##txtCurso1 = None

    #global txtCurso2
    #txtCurso2 = None

    #global txtCurso3
    #txtCurso3 = None

    #global txtCurso4
    #txtCurso4 = None

    #global txtCurso5
    #txtCurso5 = None

    #global txtCurso6
    #txtCurso6 = None

    #global nombre
    #nombre = None

    def __init__(self):

        #global nombre
        #global txtnombre
        #global txtCurso1
        #global txtCurso2
        #global txtCurso3
        #global txtCurso4
        #global txtCurso5
        #global txtCurso6

        self.ventanaCursos = tk.Tk()
        self.ventanaCursos.title("Perfil")  # Título de ventana
        self.ventanaCursos.geometry('390x570')  # Dimensiones de la ventana
        self.ventanaCursos.iconbitmap("logo.ico")  # Icono de la ventana
        self.ventanaCursos.resizable(0, 0)
        self.ventanaCursos.config(bg="white")

        # Calcula el tamaño de la pantalla
        ancho_ventana = 390
        alto_ventana = 570
        ancho_pantalla = self.ventanaCursos.winfo_screenwidth()
        alto_pantalla = self.ventanaCursos.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establece la geometría de la ventana para que esté centrada
        self.ventanaCursos.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

        # Nombre del usuario
        usuario = Label(self.ventanaCursos, text=f"{nombre}", bg="white", font=("Arial", 12, "italic"), fg="#424949")
        usuario.place(x=100, y=20)

        # Imagen de usuario
        image = Image.open("usuario.png")
        image = image.resize((50, 50))
        imgUsuario = ImageTk.PhotoImage(image)
        lbl_img = Label(self.ventanaCursos, image=imgUsuario, bg="white")
        lbl_img.place(x=30, y=20)

        # Imagen del rango del usuario (estrellas)
        image2 = Image.open("rango.jpg")
        image2 = image2.resize((80, 30))
        imgRango = ImageTk.PhotoImage(image2)
        lbl_imgr = Label(self.ventanaCursos, image=imgRango, bg="white")
        lbl_imgr.place(x=100, y=40)

        # Imagen de notificaciones
        notis = Image.open("notificaciones.png")
        notis = notis.resize((25, 25))
        imgNotificaciones = ImageTk.PhotoImage(notis)
        lbl_imgn = Label(self.ventanaCursos, image=imgNotificaciones, bg="white")
        lbl_imgn.place(x=250, y=20)

        # Cursos del usuario
        cursos = Label(self.ventanaCursos, text="Cursos:", bg="white", font=("Arial", 12, "bold"), fg="black")
        cursos.place(x=30, y=110)

        curso1 = Label(self.ventanaCursos, text="1.-", bg="white", font=("Arial", 11), fg="black")
        curso1.place(x=70, y=140)

        txtCurso1 = Entry(self.ventanaCursos,font=("Arial", 10))
        txtCurso1.place(x=100, y=140)

        curso2 = Label(self.ventanaCursos, text="2.-", bg="white", font=("Arial", 11), fg="black")
        curso2.place(x=70, y=165)

        txtCurso2 = Entry(self.ventanaCursos, font=("Arial", 10))
        txtCurso2.place(x=100, y=165)

        curso3 = Label(self.ventanaCursos, text="3.-", bg="white", font=("Arial", 11), fg="black")
        curso3.place(x=70, y=190)

        txtCurso3 = Entry(self.ventanaCursos, font=("Arial", 10))
        txtCurso3.place(x=100, y=190)

        curso4 = Label(self.ventanaCursos, text="4.-", bg="white", font=("Arial", 11), fg="black")
        curso4.place(x=70, y=215)

        txtCurso4 = Entry(self.ventanaCursos, font=("Arial", 10))
        txtCurso4.place(x=100, y=215)

        curso5 = Label(self.ventanaCursos, text="5.-", bg="white", font=("Arial", 11), fg="black")
        curso5.place(x=70, y=240)

        txtCurso5 = Entry(self.ventanaCursos, font=("Arial", 10))
        txtCurso5.place(x=100, y=240)

        curso6 = Label(self.ventanaCursos, text="6.-", bg="white", font=("Arial", 11), fg="black")
        curso6.place(x=70, y=265)

        txtCurso6 = Entry(self.ventanaCursos, font=("Arial", 10))
        txtCurso6.place(x=100, y=265)

        # Botones con conexion a BD
        btnAgregar = Button(self.ventanaCursos, bg="white", text=" Agregar curso ", font=("Arial", 8, "bold"),
                            fg="#2495FF")
        btnAgregar.place(x=24, y=330)

        btnMostrar = Button(self.ventanaCursos, bg="white", text=" Mostrar cursos ", font=("Arial", 8, "bold"),
                            fg="#FA54FF")
        btnMostrar.place(x=136, y=330)

        btnEliminar = Button(self.ventanaCursos, bg="white", text=" Eliminar curso ", font=("Arial", 9, "bold"),
                             fg="#FF3121")
        btnEliminar.place(x=256, y=329)
        # Imagen de cursos
        cimage = Image.open("cursos.png")
        cimage = cimage.resize((200, 150))
        imgCursos = ImageTk.PhotoImage(cimage)
        lbl_imgc = Label(self.ventanaCursos, image=imgCursos, bg="white")
        lbl_imgc.place(x=85, y=380)

        btnBack= Button(self.ventanaCursos, bg="white", text="  Extra  ", font=("Arial", 9, "bold"), fg="#333399")
        btnBack.place(x=145, y=530)

        self.ventanaCursos.mainloop()


    



class FormRegistro:
    global txtnombre
    txtnombre = None

    global txtcorreo
    txtcorreo = None

    global txtcontra
    txtcontra = None

    global nombre
    nombre = None

    global correo
    correo = None

    global contraseña
    contraseña = None

    global vRegistros
    vRegistros = None

    def __init__(self):
        global nombre
        global correo 
        global contraseña
        global txtnombre
        global txtcorreo
        global txtcontra
        global vRegistros

        self.vRegistros = tk.Tk()
        self.vRegistros.title("Login")  # Título de ventana
        self.vRegistros.geometry('390x570')  # Dimensiones de la ventana
        self.vRegistros.iconbitmap("logo.ico")  # Icono de la ventana
        self.vRegistros.resizable(0, 0)
        self.vRegistros.config(bg="white")

        # Calcula el tamaño de la pantalla
        ancho_ventana = 390
        alto_ventana = 570
        ancho_pantalla = self.vRegistros.winfo_screenwidth()
        alto_pantalla = self.vRegistros.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establece la geometría de la ventana para que esté centrada
        self.vRegistros.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')
        
        # Titulo de acceso
        acceso = Label(self.vRegistros, text="ACCESO", bg="white", font=("Arial", 25, "bold"), fg="#8D3DCB")
        acceso.place(x=118, y=20)

        # Imagen de login
        image = Image.open("user.png")
        image = image.resize((165, 165))
        imgUser = ImageTk.PhotoImage(image)
        lbl_img = Label(self.vRegistros, image=imgUser, bg="white")
        lbl_img.place(x=105, y=58)

        # Nombre de usuario
        nombre = Label(self.vRegistros, text="Nombre de usuario", bg="white", font=("Arial", 11), fg="black")
        nombre.place(x=60, y=270)
        txtnombre = Entry(self.vRegistros, font=("Arial", 10), width=36)
        txtnombre.place(x=60, y=300)

        # Correo
        correo = Label(self.vRegistros, text="Correo", bg="white", font=("Arial", 11), fg="black")
        correo.place(x=60, y=330)
        txtcorreo = Entry(self.vRegistros, font=("Arial", 10), width=36)
        txtcorreo.place(x=60, y=360)

         # Validación de entrada para la contraseña
        vcmd = (self.vRegistros.register(self.validar_contraseña), '%P')

        # Contraseña
        contraseña = Label(self.vRegistros, text="Contraseña", bg="white", font=("Arial", 10), fg="black")
        contraseña.place(x=60, y=390)
        txtcontra = Entry(self.vRegistros, font=("Arial", 12), width=28, show='●', validate='key', validatecommand=vcmd)
        txtcontra.place(x=60, y=420)

        # Boton para registrarse
        btnRegistro = Button(self.vRegistros, bg="#AF6DCE", text="Registrarse", font=("Arial", 10, "bold"), command=self.guardarRegistros, fg="white", width=18)
        btnRegistro.place(x=30, y=485)

        # Boton para iniciar sesión
        btnIsesion = Button(self.vRegistros, bg="#AF6DCE", text="Iniciar Sesión", font=("Arial", 10, "bold"), fg="white", width=18, command=self.iniciarSesion)
        btnIsesion.place(x=210, y=485)

        # Boton para continuar el programa
        btnRegresar = Button(self.vRegistros, bg="#AF6DCE", text="Regresar al inicio",command=self.abrir_ventanaInicio, font=("Arial", 10, "bold"), fg="white", width=18)
        btnRegresar.place(x=114, y=520)
        
        self.vRegistros.mainloop()

    def validar_contraseña(self, P):
        if len(P) <= 8 and P.isdigit():
            return True
        else:
            return False

    def guardarRegistros(self):
        global txtnombre, txtcorreo, txtcontra, nombre, correo, contraseña

        try:
            # Verificar si los widgets están inicializados
            if txtnombre is None or txtcorreo is None or txtcontra is None:
                print("Los widgets no están inicializados")
                return

            # Guardar los datos recibidos en pantalla en estas variables
            nombre = txtnombre.get()
            correo = txtcorreo.get()
            contraseña = txtcontra.get()

            # Importar de la clase 'Consultas', la función para guardar los registros
            Consultas.registrarUsuario(nombre, correo, contraseña)  # Esta función se aplica a estas variables
            messagebox.showinfo("Información", "Usuario registrado")
            self.abrir_ventanaMenu()

            # Limpiar los campos
            txtnombre.delete(0, tk.END)
            txtcorreo.delete(0, tk.END)
            txtcontra.delete(0, tk.END)

        except ValueError as error:
            print(f"Error al ingresar los datos: {error}")

    def iniciarSesion(self):
        global txtnombre, txtcorreo, txtcontra, nombre, correo, contraseña

        try:
            # Verificar si los widgets están inicializados
            if txtnombre is None or txtcorreo is None or txtcontra is None:
                print("Los widgets no están inicializados")
                return

            # Guardar los datos recibidos en pantalla en estas variables
            nombre = txtnombre.get()
            correo = txtcorreo.get()
            contraseña = txtcontra.get()

            # Importar de la clase 'Consultas', la función para iniciar sesión
            usuario_encontrado = Consultas.inicioSesion(nombre, correo, contraseña)  # Esta función se aplica a estas variables

            if usuario_encontrado:
                messagebox.showinfo("Información", f"¡Bienvenido, {nombre}!")
                self.abrir_ventanaMenu()

            else:
                messagebox.showwarning("Advertencia", "Cuenta no registrada")

            # Limpiar los campos
            txtnombre.delete(0, END)
            txtcorreo.delete(0, END)
            txtcontra.delete(0, END)

        except ValueError as error:
            print(f"Datos no registrados en la BD: {error}") 

    def abrir_ventanaMenu(self):
        self.vRegistros.destroy()
        FormBtnsCursos()

    def abrir_ventanaInicio(self):
        self.vRegistros.destroy()
        Inicio()

class FormBtnsCursos:
    def __init__(self):
        self.vBtnsCursos = tk.Tk()
        self.vBtnsCursos.title("Menú de cursos")  # Título de ventana
        self.vBtnsCursos.geometry('390x570')  # Dimensiones de la ventana
        self.vBtnsCursos.iconbitmap("logo.ico")  # Icono de la ventana
        self.vBtnsCursos.resizable(0, 0)
        self.vBtnsCursos.config(bg="white")

        # Calcula el tamaño de la pantalla
        ancho_ventana = 390
        alto_ventana = 570
        ancho_pantalla = self.vBtnsCursos.winfo_screenwidth()
        alto_pantalla = self.vBtnsCursos.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establece la geometría de la ventana para que esté centrada
        self.vBtnsCursos.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

        # Imagen de usuario
        imageu = Image.open("usuario.png")
        imageu = imageu.resize((43, 43))
        imgUser = ImageTk.PhotoImage(imageu)
        lbl_imgU = Label(self.vBtnsCursos, image=imgUser, bg="white")
        lbl_imgU.place(x=30, y=20)

        # Nombre del usuario
        titulo1 = Label(self.vBtnsCursos, text=f"{nombre}", bg="white", font=("Arial", 12, "italic"), fg="#424949")
        titulo1.place(x=100, y=20)

        # Imagen de notificaciones
        notis = Image.open("notificaciones.png")
        notis = notis.resize((25, 25))
        imgNotificaciones = ImageTk.PhotoImage(notis)
        lbl_imgn = Label(self.vBtnsCursos, image=imgNotificaciones, bg="white")
        lbl_imgn.place(x=250, y=20)

        # Imagen de cursos
        cimage = Image.open("CU.png")
        cimage = cimage.resize((230, 190))
        imgCursos = ImageTk.PhotoImage(cimage)
        lbl_imgc = Label(self.vBtnsCursos, image=imgCursos, bg="white")
        lbl_imgc.place(x=69, y=80)

        # Título
        Menu = Label(self.vBtnsCursos, text="Menú de cursos", bg="white", font=("Arial", 18, "bold"), fg="#FF8FE1")
        Menu.place(x=90, y=300)
        self.vBtnsCursos.mainloop()


class VentanaRapida:
    def __init__(self):
        self.ventanaRapida = tk.Tk()
        self.ventanaRapida.title("CECYAP.version 0.1")  # Título de ventana
        self.ventanaRapida.geometry('390x570')  # Dimensiones de la ventana
        self.ventanaRapida.iconbitmap("logo.ico")  # Icono de la ventana
        self.ventanaRapida.resizable(0, 0)
        self.ventanaRapida.config(bg="black")

        # Calcula el tamaño de la pantalla
        ancho_ventana = 390
        alto_ventana = 570
        ancho_pantalla = self.ventanaRapida.winfo_screenwidth()
        alto_pantalla = self.ventanaRapida.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establece la geometría de la ventana para que esté centrada
        self.ventanaRapida.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')
        # Imagen de cecyto veloz
        image = Image.open("cecytoVeloz.jpg")
        image = image.resize((230, 380))
        imgC = ImageTk.PhotoImage(image)
        lbl_imgC = Label(self.ventanaRapida, image=imgC, bg="black")
        lbl_imgC.place(x=110, y=110)

    # Ejecutar la función de cierre de ventana después de 5000 milisegundos (5 segundos)
        self.ventanaRapida.after(5000, self.cerrar_ventana)

        self.ventanaRapida.mainloop()

    # Función para cerrar la ventana después de 5 segundos
    def cerrar_ventana(self):
        self.ventanaRapida.destroy()

class prueba:
    def __init__(self):
        self.vprueba = tk.Tk()
        self.vprueba.title("CECYAP.version 0.1")  # Título de ventana
        self.vprueba.geometry('390x570')  # Dimensiones de la ventana
        self.vprueba.iconbitmap("logo.ico")  # Icono de la ventana
        self.vprueba.resizable(0, 0)
        self.vprueba.config(bg="black")

        # Calcula el tamaño de la pantalla
        ancho_ventana = 390
        alto_ventana = 570
        ancho_pantalla = self.vprueba.winfo_screenwidth()
        alto_pantalla = self.vprueba.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2

        cap=cv2.VideoCapture("videoplayback.mp4")

        while cap.isOpened():
            ret, im = cap.read()
            if ret == False:
                break
            cv2.imshow('imagen', im)

            if cv2.waitKey(1) == 27:
                break

            sleep(1/30)
       self.vprueba.mainloop()
            



        


VentanaRapida()
Inicio()
FormCursos() 