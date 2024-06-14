from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class Login(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = (0, 0, 0, 0)
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 40]

        
        self.add_widget(Label(text="LOGIN", font_size=30))

        
        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        

        self.add_widget(Label(text="Nome de usuário:"))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:"))
        self.add_widget(self.senha_input)
        
        
        self.cadastrar_button = Button(text="Cadastrar", background_color=(0, 1, 0, 1))
        self.login_button = Button(text="Já possuo uma conta", background_color=(0, 0, 1))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

        Window.size = (900, 600)

class CadastroApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#229a00')
        
        flo = FloatLayout()
        
        self.nome = TextInput(
            text='Seu nome', size_hint=(.2, .1), pos=(770, 500)
        )
        flo.add_widget(self.nome)

        self.phone = TextInput(
            text='Digite seu telefone', size_hint=(.2, .1), pos=(770, 400)
        )
        flo.add_widget(self.phone)

        self.email = TextInput(
            text='Digite seu Email', size_hint=(.2, .1), pos=(770, 300)
        )
        flo.add_widget(self.email)

        self.senha = TextInput(
            text='Crie sua senha', size_hint=(.2, .1), pos=(770, 200)
        )
        flo.add_widget(self.senha)

        b2 = Button(
            text='Cadastrar', size_hint=(.3, .1),
            pos_hint={'center_x': .5, 'center_y': .20},
            on_press=self.cadastrar
        )

        self.label_cadastrar = Label(
            pos_hint={'center_x': .50, 'center_y': .30}, 
            color=[1, 1, 1, 1]
        )

        flo.add_widget(b2)
        flo.add_widget(self.label_cadastrar)

        return flo

    def cadastrar(self, instance):
        N = self.nome.text
        mensagem = f'O Login {N} cadastrou minha fera!'
        self.label_cadastrar.text = mensagem

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()