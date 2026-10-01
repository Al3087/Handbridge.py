import webbrowser
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
 
 
 #Adjust size of the window
Window.size = (400, 600)
 
#Custom dark theme colors
backgroundColor = (0.45, 0.71, 0.85, 1.0) #Pretty blue
ColorWhite = (1, 1, 1, 1) #White text
MainButonColor = (0.42, 0.88, 0.64, 1.0) #Green principal
AlertButonColor = (1, 0.4, 0.4, 1) #Red for the botton out
SecondButonColor = (0.5, 0.5, 0.5, 1) #Gray for black
Colorblack = (0, 0, 0, 1)
verde_hoja = (0.114, 0.62, 0.455, 1)
amarillo_pastel = (1.0, 0.953, 0.69, 1)
azul_gris = (0.204, 0.337, 0.471, 1) #blue full
ColorCeleste = (0.678, 0.847, 0.902, 1)  # Celeste claro
ColorTexto = (0, 0, 0, 1)                # Negro
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
 
 #Users
usuarios = {
    "Alejandra Aviles": "Al3095",
    "superate": "adoc"
}
 
 
def redondear_boton(boton, color):
    with boton.canvas.before:
        Color(*color)
        boton.bg_rect = RoundedRectangle(size=boton.size, pos=boton.pos, radius=[15])
    boton.bind(size=lambda *x: setattr(boton.bg_rect, 'size', boton.size))
    boton.bind(pos=lambda *x: setattr(boton.bg_rect, 'pos', boton.pos))
    boton.background_normal = ''
    boton.background_down = ''
    boton.background_color = (0, 0, 0, 0)
 
 # Wellcome screen
class BienvenidaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
         #Dark background custom
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
 
        try:
            layout.add_widget(Image(source='logo.png', size_hint=(1, 0.6), allow_stretch=True))
        except:
            layout.add_widget(Label(text="()", size_hint=(1, 0.6), color=ColorWhite))
 
        layout.add_widget(Label(text="Bienvenido a HandBrigde", font_size=24, size_hint=(1, 0.1), color=ColorWhite))
 
        btn_ingresar = Button(
            text="Ingresar",
            size_hint=(1, 0.1),
            font_size=20,
            color=ColorWhite
        )
        redondear_boton(btn_ingresar, Colorblack)
        btn_ingresar.bind(on_press=self.ir_a_login)
 
        layout.add_widget(btn_ingresar)
        self.add_widget(layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def ir_a_login(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'login'
 
 #Screen for Login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.layout.add_widget(Label(text="Inicia sesión", font_size=26, size_hint=(1, 0.2), color=ColorWhite))
 
        self.usuario = TextInput(hint_text="Usuario", multiline=False, size_hint=(1, 0.1), font_size=18,
                                 foreground_color=Colorblack, background_color=(1, 1, 1, 1),
                                 cursor_color=Colorblack)
        self.clave = TextInput(hint_text="Contraseña", password=True, multiline=False, size_hint=(1, 0.1),
                               font_size=18, foreground_color=Colorblack, background_color= (1, 1, 1, 1),
                               cursor_color=Colorblack)
 
        self.layout.add_widget(self.usuario)
        self.layout.add_widget(self.clave)
 
 
        btn_ingresar = Button(
            text="Ingresar",
            size_hint=(1, 0.14),
            font_size=20,
            color=Colorblack
            )
        redondear_boton(btn_ingresar, MainButonColor)
        btn_ingresar.bind(on_press=self.validar_login)
 
        btn_registrar = Button(
            text="Registrar",
            size_hint=(1, 0.10),
            font_size=18,
            color=Colorblack
            )
       
        redondear_boton(btn_registrar, amarillo_pastel)
        btn_registrar.bind(on_press=self.ir_registrar)
 
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 0.1),
            font_size=16,
            color=Colorblack
            )
        redondear_boton(btn_volver, SecondButonColor)
        btn_volver.bind(on_press=self.volver)
 
        self.layout.add_widget(btn_ingresar)
        self.layout.add_widget(btn_registrar)
        self.layout.add_widget(btn_volver)
 
        self.add_widget(self.layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def validar_login(self, instance):
        user = self.usuario.text.strip()
        pwd = self.clave.text.strip()
        if user in usuarios and usuarios[user] == pwd:
            self.manager.get_screen('usuario').usuario = user
            self.manager.transition.direction = 'left'
            self.manager.current = 'usuario'
            self.usuario.text = ''
            self.clave.text = ''
        else:
            popup = Popup(title="Error",
                          content=Label(text="Usuario o contraseña incorrectos.", color=(1, 1, 1, 1)),
                          size_hint=(0.6, 0.3))
            popup.open()
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'bienvenida'
 
    def ir_registrar(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'registrar'
       
 
class RegistrarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.layout.add_widget(Label(text="¡Regístrate aquí!", font_size=24, color=ColorWhite))
 
        self.new_usuario = TextInput(hint_text="Ingresar usuario", multiline=False, size_hint=(1, 0.2), font_size=18,
                                     foreground_color=Colorblack, background_color=(1, 1, 1, 1),
                                     cursor_color=Colorblack)
 
        self.new_clave = TextInput(hint_text="Ingresar contraseña", password=True, multiline=False, size_hint=(1, 0.2),
                                   font_size=18, foreground_color=Colorblack, background_color=(1, 1, 1, 1),
                                   cursor_color=Colorblack)
        self.layout.add_widget(self.new_usuario)
        self.layout.add_widget(self.new_clave)
 
        btn_guardar = Button(text="Guardar", size_hint=(1, 0.20), font_size=18, color=ColorWhite)
        redondear_boton(btn_guardar, MainButonColor)
        btn_guardar.bind(on_press=self.guardar_usuario)
 
        btn_volver = Button(text="Volver", size_hint=(1, 0.20), font_size=16, color=Colorblack)
        redondear_boton(btn_volver, SecondButonColor)
        btn_volver.bind(on_press=self.volver)
 
        self.layout.add_widget(btn_guardar)
        self.layout.add_widget(btn_volver)
 
        self.add_widget(self.layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def guardar_usuario(self, instance):
        user = self.new_usuario.text.strip()
        pwd = self.new_clave.text.strip()
 
        if not user or not pwd:
            self.mostrar_popup("Error", "Completa todos los campos.")
        elif user in usuarios:
            self.mostrar_popup("Error", "Este usuario ya existe.")
        else:
            usuarios[user] = pwd
            self.mostrar_popup("Éxito", "Usuario registrado con éxito.")
            self.new_usuario.text = ''
            self.new_clave.text = ''
            self.manager.transition.direction = 'right'
            self.manager.current = 'login'
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'
 
    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje, color=(1, 1, 1, 1)),
                      size_hint=(0.6, 0.3))
        popup.open()
   
 #Screen logged user
class UsuarioScreen(Screen):
    usuario = StringProperty('')
 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.saludo = Label(text="", font_size=24, size_hint=(1, 0.2), markup=True, color=azul_gris)
        self.descripcion = Label(text="Voluntariados que puedes seleccionar",
                                 font_size=16, size_hint=(1, 0.2), color=ColorWhite)
 
        btn_limpieza = Button(
            text="Limpieza",
            size_hint=(1, 0.15),
            font_size=18,
            color=ColorWhite
            )
        redondear_boton(btn_limpieza, azul_gris)
        btn_limpieza.bind(on_press=self.ir_limpieza)
 
        btn_hogardeniños = Button(
            text="Hogar de niños",
            size_hint=(1, 0.15),
            font_size=18,
            color=ColorWhite
            )
        redondear_boton(btn_hogardeniños, azul_gris)
        btn_hogardeniños.bind(on_press=self.ir_Hogardeniños)
 
        btn_Visitadeasilos = Button(
            text="Visita de asilos",
            size_hint=(1, 0.15),
            font_size=18,
            color=ColorWhite
            )
        redondear_boton(btn_Visitadeasilos, azul_gris)
        btn_Visitadeasilos.bind(on_press=self.ir_Visitadeasilos)
 
        btn_refugios = Button(
            text="Refugios",
            size_hint=(1, 0.15),
            font_size=18,
            color=ColorWhite
            )
        redondear_boton(btn_refugios, azul_gris)
        btn_refugios.bind(on_press=self.ir_refugios)

        btn_salir = Button(
            text="Cerrar sesión",
            size_hint=(1, 0.15),
            font_size=18,
            color=Colorblack
            )
        redondear_boton(btn_salir,amarillo_pastel)
        btn_salir.bind(on_press=self.cerrar_sesion)
 
        self.layout.add_widget(self.saludo)
        self.layout.add_widget(self.descripcion)
        self.layout.add_widget(btn_limpieza)
        self.layout.add_widget(btn_hogardeniños)
        self.layout.add_widget(btn_Visitadeasilos)#boton visita de asilos
        self.layout.add_widget(btn_refugios)
        self.layout.add_widget(btn_salir)
 
        self.add_widget(self.layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def on_usuario(self, instance, value):
        self.saludo.text = f"¡Bienvenido, {value}!"
 
    def ir_limpieza(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'limpieza'
 
    def ir_Hogardeniños(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Hogardeniños'
 
    def ir_Visitadeasilos(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Visitadeasilos'
 
    def ir_refugios(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'refugios'

    def recomendation(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Recomendaciones'
 
    def cerrar_sesion(self, instance):
        login_screen = self.manager.get_screen('login')
        login_screen.usuario.text = ''
        login_screen.clave.text = ''

        self.manager.transition.direction = 'right'
        self.manager.current = 'bienvenida'
# Screen "Integrantes del equipo"
class EquipoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Fondo
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Layout principal
        main_layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=15
        )

        # Título
        titulo = Label(
            text="INTEGRANTES DEL EQUIPO",
            font_size=24,
            size_hint=(1, 0.15),
            color=ColorWhite,
            bold=True
        )

        main_layout.add_widget(titulo)

        # ScrollView por si hay muchos integrantes
        scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True
        )

        integrantes_layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=10,
            size_hint_y=None
        )

        integrantes_layout.bind(
            minimum_height=integrantes_layout.setter('height')
        )

        # ==========================================
        # INTEGRANTES
        # Cambia estos nombres por los de tu equipo
        # ==========================================

        integrantes = [
            {
                "nombre": "Alejandra Aviles",
                "rol": "Desarrolladora"
            },
            {
                "nombre": "Lucía García",
                "rol": "Diseñadora"
            },
            {
                "nombre": "Gabriel Ortega",
                "rol": "Desarrollador"
            },
            {
                "nombre": "Yusseli Melara",
                "rol": "Documentación"
            }
        ]

        for integrante in integrantes:

            tarjeta = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=100,
                padding=15,
                spacing=5
            )

            # Fondo de la tarjeta
            with tarjeta.canvas.before:
                Color(1, 1, 1, 1)
                tarjeta.rect = RoundedRectangle(
                    size=tarjeta.size,
                    pos=tarjeta.pos,
                    radius=[15]
                )

            tarjeta.bind(
                size=lambda instance, value, t=tarjeta:
                setattr(t.rect, 'size', value)
            )

            tarjeta.bind(
                pos=lambda instance, value, t=tarjeta:
                setattr(t.rect, 'pos', value)
            )

            nombre = Label(
                text=f"[b]{integrante['nombre']}[/b]",
                markup=True,
                font_size=19,
                color=Colorblack,
                size_hint_y=0.55
            )

            rol = Label(
                text=integrante["rol"],
                font_size=15,
                color=azul_gris,
                size_hint_y=0.45
            )

            tarjeta.add_widget(nombre)
            tarjeta.add_widget(rol)

            integrantes_layout.add_widget(tarjeta)

        scroll.add_widget(integrantes_layout)
        main_layout.add_widget(scroll)

        # Botón volver
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 0.12),
            font_size=17,
            color=ColorWhite
        )

        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)

        main_layout.add_widget(btn_volver)

        self.add_widget(main_layout)

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.rect.pos

class LimpiezaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        main_layout = BoxLayout(orientation='vertical')
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        self.content_layout = BoxLayout(orientation='vertical', padding=[40, 40, 40, 40], spacing=20, size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        label = Label(text="PRÓXIMOS VOLUNTARIADOS", font_size=24, color=ColorWhite, size_hint_y=None, height=50)
        self.content_layout.add_widget(label)

        actividades = [
            {"titulo": "Limpieza de Playa", "descripciones": ["Lugar: Playa San Diego", "Organizador: FUNZEL", "Día: Sábado, 18 de Octubre del 2025", "Hora: 8 am", "Participa con tan solo: $5 USD"], "imagen": "playa1.png"},
            {"titulo": "Limpieza de Playa", "descripciones": ["Lugar: Playa Los Almendros", "Organizador: MARN", "Día: Sabado, 20 de Septiembre del 2025", "Hora: 8 am", "Participa con tan solo: $2.50 USD"], "imagen": "playa2.png"},
            {"titulo": "Limpieza de playa", "descripciones": ["Lugar: Río Sapo", "Organizador: TECHO", "Día: Domingo, 22 de Noviembre del 2025", "Hora: 7:30 am", "Participa con tan solo: $2.50 USD"], "imagen": "playa3.png"}
        ]

        for actividad in actividades:
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=250, padding=10, spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(text=f"[b]{actividad['titulo']}[/b]", markup=True, color=(0, 0, 0, 1), font_size=18))
            for desc in actividad["descripciones"]:
                box.add_widget(Label(text=desc, color=(0.2, 0.2, 0.2, 1), font_size=14))
            box.add_widget(Image(source=actividad["imagen"], size_hint_y=None, height=60))

            organizador = actividad["descripciones"][1].lower()
            if "funzel" in organizador:
                pantalla_destino = 'funzel'
            elif "marn" in organizador:
                pantalla_destino = 'marn'
            elif "techo" in organizador:
                pantalla_destino = 'techo'
            else:
                pantalla_destino = 'funzel'

            ver_mas_btn = self.crear_ver_mas_btn(pantalla_destino)
            box.add_widget(ver_mas_btn)

            self.content_layout.add_widget(box)

        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        self.scrollview.add_widget(self.content_layout)
        main_layout.add_widget(self.scrollview)

        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])

        btn_recomendaciones = Button(text="Recomendaciones", size_hint=(1, 1), font_size=16, color=ColorWhite)
        redondear_boton(btn_recomendaciones, azul_gris)
        btn_recomendaciones.bind(on_press=self.recomendation)
        button_container.add_widget(btn_recomendaciones)

        btn_volver = Button(text="Volver", size_hint=(1, 1), font_size=16, color=ColorWhite)
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        button_container.add_widget(btn_volver)

        main_layout.add_widget(button_container)
        self.add_widget(main_layout)

    def crear_ver_mas_btn(self, destino):
        btn = Button(text="Ver más", size_hint=(None, None), size=(100, 30), font_size=12, color=ColorWhite)
        redondear_boton(btn, azul_gris)
        btn.bind(on_press=lambda instance: self.ir_a(destino))
        return btn

    def ir_a(self, destino):
        self.manager.transition.direction = 'left'
        self.manager.current = destino

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

    def recomendation(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'recomendaciones'

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class FunzelScreen(Screen): # aqui se encuentra la pantalla 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*ColorCeleste)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        root_layout = FloatLayout()

        scroll = ScrollView(size_hint=(0.9, 0.85), pos_hint={"center_x": 0.5, "top": 0.95})
        layout = BoxLayout(orientation='vertical', spacing=18, padding=24, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        try:
            layout.add_widget(Image(source='funzel.jpeg', size_hint=(1, None), height=180, allow_stretch=True))
        except:
            layout.add_widget(Label(text="[Aquí va tu imagen]", font_size=16, size_hint=(1, None), height=180, color=ColorTexto))

        info_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        info_layout.bind(minimum_height=info_layout.setter('height'))

        cuadro1 = Label(
            text="[b]¿Qué es FUNZEL?[/b]\nFUNZEL es una fundación dedicada a la rehabilitación de fauna silvestre en El Salvador. Trabajan en el rescate, recuperación y liberación de animales afectados por tráfico ilegal, maltrato o pérdida de hábitat.",
            font_size=14,
            markup=True,
            size_hint_y=None,
            text_size=(280, None),
            halign='left',
            valign='top',
            color=ColorTexto
        )
        cuadro1.bind(texture_size=cuadro1.setter('size'))

        cuadro2 = Label(
            text="[b]Misión[/b]\nProteger y conservar la biodiversidad mediante educación, rescate y liberación de especies.",
            font_size=14,
            markup=True,
            size_hint_y=None,
            text_size=(280, None),
            halign='left',
            valign='top',
            color=ColorTexto
        )
        cuadro2.bind(texture_size=cuadro2.setter('size'))

        link_button = Button(
            text="Visita: https://funzel.org.sv/es/index",
            font_size=14,
            size_hint_y=None,
            height=40,
            background_normal='',
            background_color=(0.8, 0.9, 1, 1),
            color=(0, 0, 1, 1)
        )
        link_button.bind(on_release=lambda x: webbrowser.open("https://funzel.org.sv/es/index"))

        info_layout.add_widget(cuadro1)
        info_layout.add_widget(cuadro2)
        info_layout.add_widget(link_button)

        layout.add_widget(info_layout)
        scroll.add_widget(layout)
        root_layout.add_widget(scroll)

        volver_button = Button(
            text="Volver",
            size_hint=(0.5, 0.07),
            pos_hint={"center_x": 0.5, "y": 0.02},
            background_normal='',
            background_color=(0.431, 0.905, 0.718, 1),
            color=(0, 0, 0, 1),
            font_size=14
        )
        redondear_boton(volver_button, azul_gris)
        volver_button.bind(on_press=self.volver)
        with volver_button.canvas.before:
            Color(0.431, 0.905, 0.718, 1)
            volver_button.rect = RoundedRectangle(size=volver_button.size, pos=volver_button.pos, radius=[15])
        volver_button.bind(pos=lambda instance, value: setattr(instance.rect, 'pos', value))
        volver_button.bind(size=lambda instance, value: setattr(instance.rect, 'size', value))

        root_layout.add_widget(volver_button)
        self.add_widget(root_layout)

    def volver(self, instance):
        self.manager.current = 'limpieza'

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class MarnScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*ColorCeleste)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        root_layout = FloatLayout()
        scroll = ScrollView(size_hint=(0.9, 0.85), pos_hint={"center_x": 0.5, "top": 0.95})
        layout = BoxLayout(orientation='vertical', spacing=18, padding=24, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Label(text="MARN", font_size=32, size_hint=(1, None), height=40, color=ColorTexto))

        try:
            layout.add_widget(Image(source='marn.jpeg', size_hint=(1, None), height=180, allow_stretch=True))
        except:
            layout.add_widget(Label(text="[Aquí va tu imagen]", font_size=16, size_hint=(1, None), height=180, color=ColorTexto))

        info_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        info_layout.bind(minimum_height=info_layout.setter('height'))

        cuadro1 = Label(
            text="[b]¿Qué es MARN?[/b]\nEl Ministerio de Medio Ambiente y Recursos Naturales (MARN) es la institución encargada de proteger, conservar y restaurar el medio ambiente en El Salvador.",
            font_size=14,
            markup=True,
            size_hint_y=None,
            text_size=(280, None),
            halign='left',
            valign='top',
            color=ColorTexto
        )
        cuadro1.bind(texture_size=cuadro1.setter('size'))

        cuadro2 = Label(
            text="[b]Misión[/b]\nGarantizar el derecho de la población a un medio ambiente sano, promoviendo el uso sostenible de los recursos naturales y la adaptación al cambio climático.",
            font_size=14,
            markup=True,
            size_hint_y=None,
            text_size=(280, None),
            halign='left',
            valign='top',
            color=ColorTexto
        )
        cuadro2.bind(texture_size=cuadro2.setter('size'))

        link_button = Button(
            text="Visita: https://marn.gob.sv/",
            font_size=14,
            size_hint_y=None,
            height=40,
            background_normal='',
            background_color=(0.8, 0.9, 1, 1),
            color=(0, 0, 1, 1)
        )
        link_button.bind(on_release=lambda x: webbrowser.open("https://marn.gob.sv/"))

        info_layout.add_widget(cuadro1)
        info_layout.add_widget(cuadro2)
        info_layout.add_widget(link_button)

        layout.add_widget(info_layout)
        scroll.add_widget(layout)
        root_layout.add_widget(scroll)

        volver_button = Button(
            text="Volver",
            size_hint=(0.5, 0.07),
            pos_hint={"center_x": 0.5, "y": 0.02},
            background_normal='',
            background_color=(0.431, 0.905, 0.718, 1),
            color=(0, 0, 0, 1),
            font_size=14
        )

        with volver_button.canvas.before:
            Color(0.431, 0.905, 0.718, 1)
            volver_button.rect = RoundedRectangle(size=volver_button.size, pos=volver_button.pos, radius=[15])
        volver_button.bind(pos=lambda instance, value: setattr(instance.rect, 'pos', value))
        volver_button.bind(size=lambda instance, value: setattr(instance.rect, 'size', value))

        redondear_boton(volver_button, azul_gris)
        volver_button.bind(on_press=self.volver)

        root_layout.add_widget(volver_button)
        self.add_widget(root_layout)

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'limpieza'

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class TechoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*ColorCeleste)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        root_layout = FloatLayout()
        scroll = ScrollView(size_hint=(0.9, 0.85), pos_hint={"center_x": 0.5, "top": 0.95})
        layout = BoxLayout(orientation='vertical', spacing=18, padding=24, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        try:
            layout.add_widget(Image(source='techo.jpg', size_hint=(1, None), height=180, allow_stretch=True))
        except:
            layout.add_widget(Label(text="[Aquí va tu imagen]", font_size=16, size_hint=(1, None), height=180, color=ColorTexto))

        info_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        info_layout.bind(minimum_height=info_layout.setter('height'))

        cuadro1 = Label(
            text="[b]¿Qué es TECHO?[/b]\nTECHO es una fundación que trabaja junto a comunidades en situación de pobreza en El Salvador, promoviendo el desarrollo comunitario y la construcción de viviendas dignas.",
            font_size=14,
            markup=True,
            size_hint_y=None,
            text_size=(280, None),
            halign='left',
            valign='top',
            color=ColorTexto
        )
        cuadro1.bind(texture_size=cuadro1.setter('size'))

        cuadro2 = Label(
            text="[b]Misión[/b]\nSuperar la pobreza en asentamientos precarios a través de la acción conjunta de sus habitantes y jóvenes voluntarios.",
            font_size=14,
            markup=True,
            size_hint_y=None,
            text_size=(280, None),
            halign='left',
            valign='top',
            color=ColorTexto
        )
        cuadro2.bind(texture_size=cuadro2.setter('size'))

        cuadro3 = Label(
            text="[b]Beneficio[/b]\nA beneficio de TECHO para seguir construyendo viviendas dignas en El Salvador.",
            font_size=14,
            markup=True,
            size_hint_y=None,
            text_size=(280, None),
            halign='left',
            valign='top',
            color=ColorTexto
        )
        cuadro3.bind(texture_size=cuadro3.setter('size'))

        link_button = Button(
            text="[b]Visita[/b]\nhttps://www.techo.org/paises/el-salvador/",
            font_size=14,
            markup=True,
            size_hint=(1, None),
            height=40,
            background_normal='',
            background_color=(0.8, 0.9, 1, 1),
            color=(0, 0, 1, 1)
        )
        link_button.bind(on_release=lambda x: webbrowser.open("https://www.techo.org/paises/el-salvador/"))

        info_layout.add_widget(cuadro1)
        info_layout.add_widget(cuadro2)
        info_layout.add_widget(cuadro3)
        info_layout.add_widget(link_button)

        layout.add_widget(info_layout)
        scroll.add_widget(layout)
        root_layout.add_widget(scroll)

        volver_button = Button(
            text="Volver",
            size_hint=(0.5, 0.07),
            pos_hint={"center_x": 0.5, "y": 0.02},
            background_normal='',
            background_color=(0.431, 0.905, 0.718, 1),
            color=(0, 0, 0, 1),
            font_size=14
        )

        with volver_button.canvas.before:
            Color(0.431, 0.905, 0.718, 1)
            volver_button.rect = RoundedRectangle(size=volver_button.size, pos=volver_button.pos, radius=[15])
        volver_button.bind(pos=lambda instance, value: setattr(instance.rect, 'pos', value))
        volver_button.bind(size=lambda instance, value: setattr(instance.rect, 'size', value))

        redondear_boton(volver_button, azul_gris)
        volver_button.bind(on_press=self.volver)

        root_layout.add_widget(volver_button)
        self.add_widget(root_layout)

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'limpieza'

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
 #Screen "Hogar de niños"
class HogardeniñosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Contenedor principal (ahora es BoxLayout)
        main_layout = BoxLayout(orientation='vertical')
        
        # ScrollView para el contenido
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        # Layout que contendrá todo el contenido desplazable
        self.content_layout = BoxLayout(orientation='vertical', 
                                      padding=[40, 40, 40, 40], 
                                      spacing=20,
                                      size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Título de la pantalla
        label = Label(text="PRÓXIMOS VOLUNTARIADOS", 
                     font_size=24, 
                     color=ColorWhite, 
                     size_hint_y=None, 
                     height=50)
        self.content_layout.add_widget(label)

        actividades = [
            {
                "titulo": "Hogar de niños San Vicente de Paúl",
                "descripciones": [
                    "Dia: Sabado, 11 de Octubre del 2025",
                    "Hora: 8 am",
                    "Participa con tan solo: $5 USD"
                ],
                "imagen": "niños1.png"
            },
            {
                "titulo": "Hogar Padre Vito Guarato",
                "descripciones": [
                    "Dia: Sabado, 01 de Noviembre del 2025",
                    "Hora: 8 am",
                    "Participa con tan solo: $2.50 USD"
                ],
                "imagen": "niños2.png"
            },
        ]

        # Agregar cada actividad
        for actividad in actividades:
            box = BoxLayout(orientation='vertical', 
                          size_hint_y=None, 
                          height=200, 
                          padding=10, 
                          spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(
                text=f"[b]{actividad['titulo']}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=18
            ))

            for desc in actividad["descripciones"]:
                box.add_widget(Label(
                    text=desc,
                    color=(0.2, 0.2, 0.2, 1),
                    font_size=14
                ))

            box.add_widget(Image(source=actividad["imagen"], 
                               size_hint_y=None, 
                               height=60))
            self.content_layout.add_widget(box)

        # Añadir espacio al final antes del botón
        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        
        # Añadir el contenido al ScrollView
        self.scrollview.add_widget(self.content_layout)
        
        # Añadir ScrollView al layout principal
        main_layout.add_widget(self.scrollview)
        
        # Crear contenedor para el botón (fuera del ScrollView)
        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])
        
        #Boton de recomendaciones 
        btn_recomendaciones = Button(
            text="Recomendaciones",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
            )
        redondear_boton(btn_recomendaciones, azul_gris)
        btn_recomendaciones.bind(on_press=self.recomendation)

        #self.layout.add_widget
        button_container.add_widget(btn_recomendaciones)

        # Botón Volver (versión funcional)
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
        )
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        
        button_container.add_widget(btn_volver)
        main_layout.add_widget(button_container)
        
        self.add_widget(main_layout)

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

    def recomendation(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'recomendaciones'
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
 #Screeen de visita de asilos
class VisitadeasilosScreen(Screen):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Contenedor principal (ahora es BoxLayout)
        main_layout = BoxLayout(orientation='vertical')
        
        # ScrollView para el contenido
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        # Layout que contendrá todo el contenido desplazable
        self.content_layout = BoxLayout(orientation='vertical', 
                                      padding=[40, 40, 40, 40], 
                                      spacing=20,
                                      size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Título de la pantalla
        label = Label(text="PRÓXIMOS VOLUNTARIADOS", 
                     font_size=24, 
                     color=ColorWhite, 
                     size_hint_y=None, 
                     height=50)
        self.content_layout.add_widget(label)

        actividades = [
            {
                "titulo": "Hogar de Ancianos Santa Tecla ",
                "descripciones": [
                    "Dia: Domingo, 6 de Octubre del 2026",
                    "Hora: 9 am",
                    "Participa con tan solo: $6 USD"
                ],
                "imagen": "asilos1.png"
            },
            {
                "titulo": "Hogar de Ancianos San Vicente de Paul ",
                "descripciones": [
                    "Dia: Sabado, 23 de Septiembre del 2026",
                    "Hora: 8 am",
                    "Participa con tan solo: $2.50 USD"
                ],
                "imagen": "asilos2.png"
            },
            {
                "titulo": "Visita FUSATE",
                "descripciones": [
                    "Día:  Sabado, 30 de Octubre del 2026",
                    "Hora: 8 am",
                    "Participa con tan solo: $5 USD"
                ],
                "imagen": "asilos3.png"
            }
        ]

        # Agregar cada actividad
        for actividad in actividades:
            box = BoxLayout(orientation='vertical', 
                          size_hint_y=None, 
                          height=200, 
                          padding=10, 
                          spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(
                text=f"[b]{actividad['titulo']}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=18
            ))

            for desc in actividad["descripciones"]:
                box.add_widget(Label(
                    text=desc,
                    color=(0.2, 0.2, 0.2, 1),
                    font_size=14
                ))

            box.add_widget(Image(source=actividad["imagen"], 
                               size_hint_y=None, 
                               height=60))
            self.content_layout.add_widget(box)

        # Añadir espacio al final antes del botón
        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        
        # Añadir el contenido al ScrollView
        self.scrollview.add_widget(self.content_layout)
        
        # Añadir ScrollView al layout principal
        main_layout.add_widget(self.scrollview)
        
        # Crear contenedor para el botón (fuera del ScrollView)
        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])

                #Boton de recomendaciones 
        btn_recomendaciones = Button(
            text="Recomendaciones",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
            )
        redondear_boton(btn_recomendaciones, azul_gris)
        btn_recomendaciones.bind(on_press=self.recomendation)

        #self.layout.add_widget
        button_container.add_widget(btn_recomendaciones)
        
        # Botón Volver (versión funcional)
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 1),
            font_size=16,
            color=Colorblack
        )
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        
        button_container.add_widget(btn_volver)
        main_layout.add_widget(button_container)
        
        self.add_widget(main_layout)

     def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

     def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

     def recomendation(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Recomendaciones3'
    

 #Screen "Refugios"
class RefugiosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Contenedor principal (ahora es BoxLayout)
        main_layout = BoxLayout(orientation='vertical')
        
        # ScrollView para el contenido
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        # Layout que contendrá todo el contenido desplazable
        self.content_layout = BoxLayout(orientation='vertical', 
                                      padding=[40, 40, 40, 40], 
                                      spacing=20,
                                      size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Título de la pantalla
        label = Label(text="PRÓXIMOS VOLUNTARIADOS", 
                     font_size=24, 
                     color=ColorWhite, 
                     size_hint_y=None, 
                     height=50)
        self.content_layout.add_widget(label)

        actividades = [
            {
                "titulo": "Échame una pata",
                "descripciones": [
                    "Día: Sábado, 22 de Marzo",
                    "Hora: 6 am",
                    "Participa con tan solo: $5 USD"
                ],
                "imagen": "refugios1.png"
            },
            {
                "titulo": "Fundación Catgod",
                "descripciones": [
                    "Día: Sabado, 12 de Septiembre",
                    "Hora: 8 am",
                    "Participa con tan solo: $2.50 USD"
                ],
                "imagen": "refugios2.png"
            },
            {
                "titulo": "Asociación Milagros de amor",
                "descripciones": [
                    "Día: Domingo, 22 de Noviembre del 2025",
                    "Hora: 7:30 am",
                    "Participa con tan solo: $2.50 USD"
                ],
                "imagen": "refugios3.png"
            }
        ]

        # Agregar cada actividad
        for actividad in actividades:
            box = BoxLayout(orientation='vertical', 
                          size_hint_y=None, 
                          height=200, 
                          padding=10, 
                          spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(
                text=f"[b]{actividad['titulo']}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=18
            ))

            for desc in actividad["descripciones"]:
                box.add_widget(Label(
                    text=desc,
                    color=(0.2, 0.2, 0.2, 1),
                    font_size=14
                ))

            box.add_widget(Image(source=actividad["imagen"], 
                               size_hint_y=None, 
                               height=60))
            self.content_layout.add_widget(box)

        # Añadir espacio al final antes del botón
        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        
        # Añadir el contenido al ScrollView
        self.scrollview.add_widget(self.content_layout)
        
        # Añadir ScrollView al layout principal
        main_layout.add_widget(self.scrollview)
        
        # Crear contenedor para el botón (fuera del ScrollView)
        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])

       #Boton de recomendaciones 
        btn_recomendaciones = Button(
            text="Recomendaciones",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
            )
        redondear_boton(btn_recomendaciones, azul_gris)
        btn_recomendaciones.bind(on_press=self.recomendation)

        #self.layout.add_widget
        button_container.add_widget(btn_recomendaciones)
        
        # Botón Volver (versión funcional)
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 1),
            font_size=16,
            color=Colorblack
        )
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        
        button_container.add_widget(btn_volver)
        main_layout.add_widget(button_container)
        
        self.add_widget(main_layout)

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

    def recomendation(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Recomendaciones4'
    
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
    
  #Screen "Recomendaciones"
class RecomendPlayaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Contenedor principal (ahora es BoxLayout)
        main_layout = BoxLayout(orientation='vertical')
        
        # ScrollView para el contenido
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        # Layout que contendrá todo el contenido desplazable
        self.content_layout = BoxLayout(orientation='vertical', 
                                      padding=[40, 40, 40, 40], 
                                      spacing=20,
                                      size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Título de la pantalla
        label = Label(text="RECOMENDACIONES", 
                     font_size=24, 
                     color=ColorWhite, 
                     size_hint_y=None, 
                     height=50)
        self.content_layout.add_widget(label)
 
        actividades = [
            {
                "imagen": "bloq.png",
                "titulo": "Porta tu bloqueador personal"
            },
            {
                "imagen": "agua.png",
                "titulo": "Lleva tu botella de agua"
            },
            {
                "imagen": "agua.png",
                "titulo": "Ropa comoda"
            },
            {
                "imagen": "agua.png",
                "titulo": "Gorra o sombrero"
            }
        ]
 # Agregar cada actividad
        for actividad in actividades:
            box = BoxLayout(orientation='vertical', 
                          size_hint_y=None, 
                          height=200, 
                          padding=10, 
                          spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(
                text=f"[b]{actividad['titulo']}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=18
            ))

            box.add_widget(Image(source=actividad["imagen"], 
                               size_hint_y=None, 
                               height=60))
            self.content_layout.add_widget(box)

        # Añadir espacio al final antes del botón
        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        
        # Añadir el contenido al ScrollView
        self.scrollview.add_widget(self.content_layout)
        
        # Añadir ScrollView al layout principal
        main_layout.add_widget(self.scrollview)
        
        # Crear contenedor para el botón (fuera del ScrollView)
        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])

        # Botón Volver (versión funcional)
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
        )
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        
        button_container.add_widget(btn_volver)
        main_layout.add_widget(button_container)
        
        self.add_widget(main_layout)
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


 #Screen "Recomendaciones"
class RecomendhogarniñosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Contenedor principal (ahora es BoxLayout)
        main_layout = BoxLayout(orientation='vertical')
        
        # ScrollView para el contenido
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        # Layout que contendrá todo el contenido desplazable
        self.content_layout = BoxLayout(orientation='vertical', 
                                      padding=[40, 40, 40, 40], 
                                      spacing=20,
                                      size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Título de la pantalla
        label = Label(text="RECOMENDACIONES", 
                     font_size=24, 
                     color=ColorWhite, 
                     size_hint_y=None, 
                     height=50)
        self.content_layout.add_widget(label)

        actividades = [
            {
                "imagen": "nosohort.png",
                "titulo": "      Vestir ropa decente\n"
                "              NO shorts\n"
                "              NO faldas\n"
                "NO camisas sin mangas\n"
                "           NO chanclas"
            },
            {
                "imagen": "empatia.webp",
                "titulo": 
                "Se empatico/a con los niños\n"
                "     ellos esperan tu visita"
            },
            {
                "imagen": "agua.png",
                "titulo": 
                "                        Por favor\n"
                "    NO mencionar temas sencibles\n"
                "                  Ejemplo: Familia"
            },
            {
                "imagen": ".png",
                "titulo": "No olvides una buena actitud"
            }
        ]
 
 # Agregar cada actividad
        for actividad in actividades:
            box = BoxLayout(orientation='vertical', 
                          size_hint_y=None, 
                          height=200, 
                          padding=10, 
                          spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(
                text=f"[b]{actividad['titulo']}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=18
            ))

            box.add_widget(Image(source=actividad["imagen"], 
                               size_hint_y=None, 
                               height=60))
            self.content_layout.add_widget(box)

        # Añadir espacio al final antes del botón
        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        
        # Añadir el contenido al ScrollView
        self.scrollview.add_widget(self.content_layout)
        
        # Añadir ScrollView al layout principal
        main_layout.add_widget(self.scrollview)
        
        # Crear contenedor para el botón (fuera del ScrollView)
        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])

        # Botón Volver (versión funcional)
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
        )
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        
        button_container.add_widget(btn_volver)
        main_layout.add_widget(button_container)
        
        self.add_widget(main_layout)
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

  #Screen "Recomendaciones"
class RecomendVisitadeAsilosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Contenedor principal (ahora es BoxLayout)
        main_layout = BoxLayout(orientation='vertical')
        
        # ScrollView para el contenido
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        # Layout que contendrá todo el contenido desplazable
        self.content_layout = BoxLayout(orientation='vertical', 
                                      padding=[40, 40, 40, 40], 
                                      spacing=20,
                                      size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Título de la pantalla
        label = Label(text="RECOMENDACIONES", 
                     font_size=24, 
                     color=ColorWhite, 
                     size_hint_y=None, 
                     height=50)
        self.content_layout.add_widget(label)
 
        actividades = [
            {
                "imagen": "noshort.png",
                "titulo": "          Vestir ropa decente, no shorts,\n"
                    "  no faldas y en la medida de lo posible,\n"
                    "                           no chanclas"
            },
            {
                "imagen": "empatia.png",
                "titulo": "No olvides que estas personas \n  te esperan con mucho amor"
            },
            {
                "imagen": "valor.png",
                "titulo":"Pon en practica tus valores como\n   respeto y solidaridad"
            }
        ]
 # Agregar cada actividad
        for actividad in actividades:
            box = BoxLayout(orientation='vertical', 
                          size_hint_y=None, 
                          height=200, 
                          padding=10, 
                          spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(
                text=f"[b]{actividad['titulo']}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=18
            ))

            box.add_widget(Image(source=actividad["imagen"], 
                               size_hint_y=None, 
                               height=60))
            self.content_layout.add_widget(box)

        # Añadir espacio al final antes del botón
        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        
        # Añadir el contenido al ScrollView
        self.scrollview.add_widget(self.content_layout)
        
        # Añadir ScrollView al layout principal
        main_layout.add_widget(self.scrollview)
        
        # Crear contenedor para el botón (fuera del ScrollView)
        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])

        # Botón Volver (versión funcional)
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
        )
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        
        button_container.add_widget(btn_volver)
        main_layout.add_widget(button_container)
        
        self.add_widget(main_layout)
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class RecomendRefugiosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # Contenedor principal (ahora es BoxLayout)
        main_layout = BoxLayout(orientation='vertical')
        
        # ScrollView para el contenido
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        # Layout que contendrá todo el contenido desplazable
        self.content_layout = BoxLayout(orientation='vertical', 
                                      padding=[40, 40, 40, 40], 
                                      spacing=20,
                                      size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Título de la pantalla
        label = Label(text="RECOMENDACIONES", 
                     font_size=24, 
                     color=ColorWhite, 
                     size_hint_y=None, 
                     height=50)
        self.content_layout.add_widget(label)
 
        actividades = [
            {
                "imagen": "noshort.png",
                "titulo": "Se recomienda usar jeans \n    y una camisa comoda."
            },
            {
                "imagen": "empatia.png",
                "titulo": "             Lleva tu pacienca!! \nrecuerda que vamos a visitar a \n  nuestros amiguitos peluditos"
            }
        ]
 # Agregar cada actividad
        for actividad in actividades:
            box = BoxLayout(orientation='vertical', 
                          size_hint_y=None, 
                          height=200, 
                          padding=10, 
                          spacing=5)
            with box.canvas.before:
                Color(1, 1, 1, 1)
                box.rect = Rectangle(size=box.size, pos=box.pos)
            box.bind(size=lambda inst, val, b=box: setattr(b.rect, 'size', val))
            box.bind(pos=lambda inst, val, b=box: setattr(b.rect, 'pos', val))

            box.add_widget(Label(
                text=f"[b]{actividad['titulo']}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=18
            ))

            box.add_widget(Image(source=actividad["imagen"], 
                               size_hint_y=None, 
                               height=60))
            self.content_layout.add_widget(box)

        # Añadir espacio al final antes del botón
        self.content_layout.add_widget(Widget(size_hint_y=None, height=20))
        
        # Añadir el contenido al ScrollView
        self.scrollview.add_widget(self.content_layout)
        
        # Añadir ScrollView al layout principal
        main_layout.add_widget(self.scrollview)
        
        # Crear contenedor para el botón (fuera del ScrollView)
        button_container = BoxLayout(size_hint_y=None, height=60, padding=[40, 0, 40, 20])

        # Botón Volver (versión funcional)
        btn_volver = Button(
            text="Volver",
            size_hint=(1, 1),
            font_size=16,
            color=ColorWhite
        )
        redondear_boton(btn_volver, azul_gris)
        btn_volver.bind(on_press=self.volver)
        
        button_container.add_widget(btn_volver)
        main_layout.add_widget(button_container)
        
        self.add_widget(main_layout)
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


 #App principal
class LoginApp(App):
    def build(self):
        self.title = "App de Login"
        sm = ScreenManager(transition=FadeTransition(duration=0.3)) #Soft transition
        sm.add_widget(BienvenidaScreen(name='bienvenida'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(UsuarioScreen(name='usuario'))
        sm.add_widget(EquipoScreen(name='equipo'))
        sm.add_widget(RegistrarScreen(name='registrar'))
        sm.add_widget(LimpiezaScreen(name='limpieza'))
        sm.add_widget(HogardeniñosScreen(name='Hogardeniños'))
        sm.add_widget(VisitadeasilosScreen(name='Visitadeasilos'))
        sm.add_widget(RefugiosScreen(name='refugios'))
        sm.add_widget(RecomendPlayaScreen(name='Recomendaciones'))
        sm.add_widget(FunzelScreen(name='funzel'))
        sm.add_widget(MarnScreen(name='marn'))
        sm.add_widget(TechoScreen(name='techo'))
        sm.add_widget(RecomendPlayaScreen(name='Recomendaciones'))
        sm.add_widget(RecomendhogarniñosScreen(name='recomendaciones'))
        sm.add_widget(RecomendVisitadeAsilosScreen(name='Recomendaciones3'))
        sm.add_widget(RecomendVisitadeAsilosScreen(name='Recomendaciones4'))
        return sm

 
if __name__ == '__main__':
    LoginApp().run()