import flet as ft


def main(page):

    page.title = "SUMA"

    def button_clicked(e):
        txtresultado.value = str(int(valor1.value) + int(valor2.value))
        page.update()

    page.add(ft.Text("Operación de SUMA", size=50, color="yellow"))
    

    page.add(ft.Text(value = "Ingrese primer valor", color="green", size=20))
    page.update()
    valor1 = ft.TextField(hint_text="", width=200)
    page.add(valor1)


    page.add(ft.Text(value = "Ingrese segundo valor", color="green", size=20))
    page.update()
    valor2 = ft.TextField(hint_text="", width=200)
    page.add(valor2)



    page.add(ft.ElevatedButton(
        text="+",
        on_click=button_clicked,
        data = "+",
        )
    )


    txtresultado = ft.TextField(hint_text="", width=100)
    page.add(txtresultado)
    page.update()



ft.app(target = main, view=ft.AppView.WEB_BROWSER)