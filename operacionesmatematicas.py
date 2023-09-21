import flet as ft

def main(page):

    def sumar(e):
        txtresultado.value = str(int(valor1.value) +  int(valor2.value))
        page.update()

    def restar(e):
        txtresultado.value = str(int(valor1.value) -  int(valor2.value))
        page.update()  

    def multiplicar(e):
        txtresultado.value = str(int(valor1.value) *  int(valor2.value))
        page.update()

    def dividir(e):
        txtresultado.value = str(int(valor1.value) /  int(valor2.value))
        page.update()            

    page.add(ft.Text(value="Ingrese 1er valor", color="yellow", size=20))
    page.update()
    valor1 = ft.TextField(hint_text="", width=200)
    page.add(valor1)

    page.add(ft.Text(value="Ingrese 2do valor", color="yellow", size=20))
    page.update()
    valor2 =ft.TextField(hint_text="", width=200)
    page.add(valor2)
    
    page.add(ft.ElevatedButton(
        text="+", 
        on_click = sumar,
        data="+", 
        )
    )
    page.update()

    page.add(ft.ElevatedButton(
        text="-", 
        on_click = restar, 
        data="-",
        )
    )
    page.update()

    page.add(ft.ElevatedButton(
        text="*", 
        on_click = multiplicar, 
        data="*",
        )
    )
    page.update()

    page.add(ft.ElevatedButton(
        text="/", 
        on_click = dividir, 
        data="*",
        )
    )
    page.update()
    

    txtresultado = ft.TextField(hint_text="", width=200)
    page.add(txtresultado)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)        