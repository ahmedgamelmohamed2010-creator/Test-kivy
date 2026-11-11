from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp


class TestApp(App):
    def build(self):
        self.count = 0

        root = BoxLayout(
            orientation="vertical",
            padding=dp(24),
            spacing=dp(18),
        )

        title = Label(
            text="Kivy APK Test",
            font_size="28sp",
            bold=True,
            size_hint_y=None,
            height=dp(70),
        )
        root.add_widget(title)

        self.message = Label(
            text="If you can see this screen, the app is running!",
            font_size="18sp",
            halign="center",
            valign="middle",
        )
        self.message.bind(size=self._update_text_size)
        root.add_widget(self.message)

        self.counter_label = Label(
            text="Button clicks: 0",
            font_size="22sp",
            size_hint_y=None,
            height=dp(60),
        )
        root.add_widget(self.counter_label)

        button = Button(
            text="Tap me",
            font_size="20sp",
            size_hint_y=None,
            height=dp(58),
        )
        button.bind(on_release=self.increase_counter)
        root.add_widget(button)

        return root

    def _update_text_size(self, instance, size):
        instance.text_size = size

    def increase_counter(self, _instance):
        self.count += 1
        self.counter_label.text = f"Button clicks: {self.count}"


if __name__ == "__main__":
    TestApp().run()
