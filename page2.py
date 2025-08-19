import flet as ft
from custom_flet_components.custom_router import Router
class DefaultScreen(ft.Column):
    def __init__(self, page: ft.Page, router: Router):

        super().__init__(
            controls=[
                ft.Text("Go to Default Page"),
            ft.ElevatedButton(
                "click",
                on_click=lambda _: page.go("/")
            )
            ]
        )
