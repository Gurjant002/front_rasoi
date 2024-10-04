import asyncio
import flet as ft


async def main(page: ft.Page):
    page.title = "Rasoi"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.EDIT_DOCUMENT,
                label="Facturas",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.PAYMENTS,
                label="Caja",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.PERSON,
                label="Clientes",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.RESTAURANT_MENU,
                label="Restaurant Menu",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.CHECKROOM,
                label="Otros 2",
                bgcolor=ft.colors.WHITE
            ),
        ],
        indicator_shape=ft.RoundedRectangleBorder(radius=8),
        
    )
    page.add(ft.Text("Me voy a cagar =)!", size=50) )
ft.app(target=main, assets_dir="assets")
