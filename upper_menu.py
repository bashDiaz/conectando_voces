import flet as ft
import time
import random

class UpperMenu:

    def __init__(self, page):
        self.page = page

    def _clicked(self, e):
        number = random.randint(1, 6)
        text = ft.Text(f'button clicked: {number}' , color='white')
        self.page.add(text) 
        time.sleep(number)
        self.page.remove(text)

    def create_menu(self):
        return ft.AppBar(
            leading=ft.Image('Logo.png', height=200, width=200, fit=ft.ImageFit.COVER),
            leading_width=70,
            bgcolor=ft.colors.LIGHT_BLUE_200,
            actions=[
                ft.IconButton(ft.icons.SETTINGS, on_click=self._clicked),
                ft.IconButton(ft.icons.SEARCH, on_click=self._clicked),
                ft.IconButton(ft.icons.MORE_VERT, on_click=self._clicked),
            ]
        )