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
            controls = [
                ft.Dropdown()
            ]
        ),
        ft.Row(
            controls = [
                ft.Slider(rotate=math.pi*3/2)
            ],
        )
    ]
)


ft.app(target=main_form)