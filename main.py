import asyncio
import flet as ft


async def main(page: ft.Page):
    page.title = "Rasoi"
    buttons = get_buttons()
    
    page.add(
        ft.Row(
            [
                button for button in buttons
            ]
        )
    )

def get_buttons():
    buttons = [
        ft.ElevatedButton("Facturas", on_click=lambda _: print("Clicked!")),
        ft.ElevatedButton("Caja", on_click=lambda _: print("Clicked!")),
        ft.ElevatedButton("Clientes", on_click=lambda _: print("Clicked!")),
        ft.ElevatedButton("Otros 1", on_click=lambda _: print("Clicked!")),
        ft.ElevatedButton("Otros 2", on_click=lambda _: print("Clicked!")),
    ]
    return buttons

ft.app(target=main, assets_dir="assets")
