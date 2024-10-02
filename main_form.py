import math

import flet as ft

def main_form(page: ft.Page):
    page.title = "Voice Changer"
    page.padding = 20
    page.window.height = 600
    page.window.width = 800
    page.add(content)



content = ft.Column(
    controls = [
        ft.Row(
            controls =[
                ft.Dropdown(
                    label="Выберите элемент",
                    options=[
                        ft.dropdown.Option("apple"),
                        ft.dropdown.Option("banana"),
                        ft.dropdown.Option("cherry")
                    ]
                )
            ]
        ),
        ft.Row(
            controls = [
                ft.Slider()
            ],
        )
    ]
)


ft.app(target=main_form)