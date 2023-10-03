import flet as ft


def main(page: ft.Page):

    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tbcod.value}', '{tbnom.value}', '{ddcate.value}', '{ddpeso.value}'"
        page.update()



    t = ft.Text()

    tbcod = ft.TextField(label="CÓDIGO PRODUCTO")
    tbnom = ft.TextField(label="NOMBRE PRODUCTO")

    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    ddcate = ft.Dropdown(label="CATEGORIA",
        width=150,
        options=[
            ft.dropdown.Option("dulce"),
            ft.dropdown.Option("salado"),
        ],
    )

    ddpeso = ft.Dropdown(label="PESO",
        width=100,
        options=[
            ft.dropdown.Option("KG"),
            ft.dropdown.Option("G"),
        ],
    )

    
    
    page.add(tbcod, tbnom, ddcate, ddpeso, t, b)




ft.app(target=main, view=ft.AppView.WEB_BROWSER)