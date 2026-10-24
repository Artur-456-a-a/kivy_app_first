from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CounterApp(App):
    def build(self):
        # Инициализируем счетчик
        self.count = 0

        # Создаем вертикальный контейнер для виджетов
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Создаем текстовую метку
        self.label = Label(
            text="Нажми на кнопку!", 
            font_size='24sp'
        )

        # Создаем кнопку и привязываем к ней функцию при нажатии
        button = Button(
            text="Кликни меня!",
            font_size='20sp',
            background_color=(0.2, 0.6, 1, 1)  # Синеватый цвет кнопки
        )
        button.bind(on_press=self.increment_counter)

        # Добавляем виджеты в контейнер
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def increment_counter(self, instance):
        # Увеличиваем счетчик и обновляем текст на экране
        self.count += 1
        self.label.text = f"Количество кликов: {self.count}"


if __name__ == '__main__':
    CounterApp().run()
