import flet as ft
from Audio import play_audio
import time


class Card:
    
    def __init__(self, data_info, data_img, folder, page):
        self.data_info = data_info
        self.data_img = data_img
        self.folder = folder
        self.page = page 
    
    def _sound(self):
        if self.contenedor.bgcolor == ft.colors.LIGHT_BLUE_200:
            self.contenedor.bgcolor = ft.colors.DEEP_ORANGE_200
            self.page.update()
            time.sleep(0.1)
            self.contenedor.bgcolor = ft.colors.LIGHT_BLUE_200
            self.page.update()
            play_audio(self.data_info)

    def create_card(self):
        self.img_container = ft.Image('pictogramas//'+self.folder+'//'+self.data_img, height=150, width=150, fit=ft.ImageFit.COVER)
        self.contenedor = ft.Container(
                self.img_container,
                height=150,
                width=300,
                padding=5,
                bgcolor=ft.colors.LIGHT_BLUE_200,
                blur=5,
                border_radius=10,
                alignment=ft.alignment.center
            )
        carta = ft.Stack([
            self.contenedor,   
            ft.Container(
                alignment=ft.alignment.bottom_center,
                on_click=(lambda x: self._sound())
                )],
            col={'xs':6,'sm':3,'xl':1,},
            height=150,
            width=60,
            )
        return carta