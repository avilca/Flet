import flet as ft
from flet import *


def main(page: ft.Page):

    
    def button_clicked(e):
        t.value = f"Los datos:  '{codpro.value}', '{nompro.value}', '{ddcate.value}', '{ddpeso.value}'"
        page.update()


        

    t = ft.Text()


    codpro = ft.TextField(label="CÓDIGO PRODUCTO")
    nompro = ft.TextField(label="NOMBRE PRODUCTO")

    #combo de categoria
    ddcate = ft.Dropdown(label="CATEGORIA",
        width=150,
        options=[
            ft.dropdown.Option("dulce"),
            ft.dropdown.Option("salado"),
        ],
    )

    #combo de peso
    ddpeso = ft.Dropdown(label="PESO",
        width=100,
        options=[
            ft.dropdown.Option("KG"),
            ft.dropdown.Option("G"),
        ],
    )

    #Boton AGREGAR
    BtnAgregar = ft.ElevatedButton(
        text="Agregar", 
        bgcolor="blue",
        color="white",
        on_click=button_clicked
        )

        
    page.add(codpro, nompro, ddcate, ddpeso, t, BtnAgregar)

    page.add( 
            ft.DataTable(columns=[
                            ft.DataColumn(ft.Text("Código", weight="bold")),
                            ft.DataColumn(ft.Text("Producto", weight="bold")),
                            ft.DataColumn(ft.Text("Categoria",weight="bold")),
                            ft.DataColumn(ft.Text("Peso", weight="bold")),
                        ],
                    )    

    )


ft.app(target=main)