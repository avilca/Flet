import flet as ft

def main(page):

    page.title = "Operaciones Matematicas"

    def sumar(e):
          
         
        
        if valor1.value == "" or valor2.value == "":
            valor1.error_text = "por favor ingrese primer valor"
            valor2.error_text = "por favor ingrese segundo valor"       
        else:
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

    page.add(ft.Text("Operaciones Matematicas", size=50, color="green"))

    page.add(ft.Text(value="Ingrese 1er valor", color="green", size=20))
    page.update()
    valor1 = ft.TextField(hint_text="", width=200)
    page.add(valor1)

    page.add(ft.Text(value="Ingrese 2do valor", color="green", size=20))
    page.update()
    valor2 =ft.TextField(hint_text="", width=200)
    page.add(valor2)
    
    page.add(ft.ElevatedButton(
        text="+", 
        on_click = sumar,
        )
    )
    page.update()

    page.add(ft.ElevatedButton(
        text="-", 
        on_click = restar, 
        )
    )
    page.update()

    page.add(ft.ElevatedButton(
        text="*", 
        on_click = multiplicar, 
        )
    )
    page.update()

    page.add(ft.ElevatedButton(
        text="/", 
        on_click = dividir, 
        )
    )
    page.update()
    

    txtresultado = ft.TextField(hint_text="", width=200)
    page.add(txtresultado)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)        