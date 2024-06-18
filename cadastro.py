from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.modalview import ModalView
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyAsGeTc9XeWi_N9-6pcb2Mk3jGf0Zpv0bY",
    'authDomain': "loginpita-65068.firebaseapp.com",
    'databaseURL': "https://loginpita-65068-default-rtdb.firebaseio.com/",
    'projectId': "loginpita-65068",
    'storageBucket': "loginpita-65068.appspot.com",
    'messagingSenderId': "104068236769",
    'appId': "1:104068236769:web:a1cacdc74c405c9f3d7ea0",
    'measurementId': "G-YH63NPQEZR"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

class Login(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        self.add_widget(Label(text="LOGIN", font_size=40, font_name='Georgia', color=get_color_from_hex('#0f0360')))

        self.email_input = TextInput(hint_text="Email...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#0f0360'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#0f0360'), font_size=20))
        self.add_widget(self.senha_input)

        self.cadastrar_button = Button(text="Entrar", background_color=(0, 1, 0, 0.75))
        self.cadastrar_button.bind(on_release=self.login)

        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=(0, 0, 1))
        self.login_button.bind(on_release=self.create_new_window)

        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

    def login(self, instance):
        email = self.email_input.text
        password = self.senha_input.text
        try:
            auth.sign_in_with_email_and_password(email, password)
            print("Login successful")
            # Código adicional após o login bem-sucedido
        except:
            print("Invalid login")

    def create_new_window(self, instance):
        new_window = NewWindow()
        new_window.open()
        Window.clearcolor = (1, 1, 1, 1)

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class NewWindow(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('#0f0360')))

        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.email_input = TextInput(hint_text="Digite seu email ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#0f0360'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#0f0360'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#0f0360'), font_size=20))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=(0, 0, 1))
        self.button_cadastrar.bind(on_release=self.register)

        self.add_widget(self.button_cadastrar)

    def register(self, instance):
        email = self.email_input.text
        password = self.senha_input.text
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Registration successful")
            self.open_login_window()  # Abre a tela de login após o cadastro bem-sucedido
        except:
            print("Registration failed")

    def open_login_window(self):
        login_window = Login()
        login_window.open()

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()
