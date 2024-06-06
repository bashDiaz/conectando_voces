import flet as ft
import upper_menu as um
import Generate_cards as gc
import os



def card_rows(page, dir, folder):
    # Create a list of cards
    cards = [os.path.splitext(element)[0] for element in dir]
    imgs = [element for element in dir]
    
    # Create a list of Card objects
    card_objects = [gc.Card(card, img, folder, page) for card, img in zip(cards, imgs)]
    
    # Create a list of card containers
    card_containers = [card.create_card() for card in card_objects]

    card_rows = ft.Column(
        controls = [ft.ResponsiveRow(card_containers)],
        scroll=True
    )
    return card_rows

def main(page: ft.Page):

    ## Set window propierties
    page.bgcolor = '#EFEBE8'
    page.scroll = True

    # Create page upper menu
    upper_menu = um.UpperMenu(page)
    page.appbar = upper_menu.create_menu()
    
    # Create page content
    main_column = ft.Column(
        controls = [],
        scroll = True,
        spacing = 0,
        expand = True)
    

    path = os.getcwd() + '\\conectando_voces\\assets\\pictogramas'
    dir = os.listdir(path)
    for folder in dir:
        main_column.controls.append(ft.Text(folder, size=20, weight='bold', color='black'))
        data_path_col = os.path.join(path, folder)
        dir_int = os.listdir(data_path_col)
        main_column.controls.append(card_rows(page, dir_int, folder))
        main_column.controls.append(ft.Divider(thickness=3))


    page.add(main_column)
    page.update()


ft.app(main)
