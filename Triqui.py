import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class TriquiGame(GridLayout):
    def __init__(self, **kwargs):
        super(TriquiGame, self).__init__(**kwargs)
        self.cols = 3
        self.turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

        # Crear botones para el tablero
        for i in range(3):
            for j in range(3):
                button = Button(font_size=32)
                button.bind(on_press=self.on_button_press)
                button.coord = (i, j)  # Coordenas para identificar el botón
                self.add_widget(button)

        # Modificando el Label con tipografía personalizada
        self.info_label = Label(
            text="Turno de: X",
            font_size=40,            # Tamaño del texto
            font_name="Bobaland.ttf",  # Ruta a la tipografía personalizada
            size_hint=(1, 0.5),      # Controla el tamaño relativo del Label
            height=50                # Altura específica del Label
        )
        self.add_widget(self.info_label)

    def on_button_press(self, instance):
        i, j = instance.coord

        # No permitir cambiar un botón ya jugado
        if instance.text == '':
            instance.text = self.turn
            self.board[i][j] = self.turn

            if self.check_winner():
                self.info_label.text = f"Ganador: {self.turn}"
                self.disable_buttons()
            elif self.check_draw():
                self.info_label.text = "Empate"
                self.disable_buttons()
            else:
                self.switch_turn()

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
        self.info_label.text = f"Turno de: {self.turn}"

    def check_winner(self):
        # Verificar filas, columnas y diagonales
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def disable_buttons(self):
        # Deshabilitar todos los botones después de que termina el juego
        for child in self.children:
            if isinstance(child, Button):
                child.disabled = True


class TriquiApp(App):
    def build(self):
        return TriquiGame()

if __name__ == "__main__":
    TriquiApp().run()
