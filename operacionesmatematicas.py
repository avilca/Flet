import flet as ft

def main(page):

    page.title = "Operaciones Matematicas"


    def sumar(e):
                
        if valor1.value == "" or valor2.value == "":
            valor1.error_text = "por favor ingrese primer valor"
            valor2.error_text = "por favor ingrese segundo valor"       
        else:
            valor1.error_text= ''
            valor2.error_text= ''
            txtresultado.value = str(int(valor1.value) +  int(valor2.value)) 

        page.update()

    def restar(e):
        if valor1.value == "" or valor2.value == "":
            valor1.error_text = "por favor ingrese primer valor"
            valor2.error_text = "por favor ingrese segundo valor"       
        else:
            valor1.error_text= ''
            valor2.error_text= ''
            txtresultado.value = str(int(valor1.value) -  int(valor2.value))

        page.update()  

    def multiplicar(e):
        if valor1.value == "" or valor2.value == "":
            valor1.error_text = "por favor ingrese primer valor"
            valor2.error_text = "por favor ingrese segundo valor"       
        else:
            valor1.error_text= ''
            valor2.error_text= ''
            txtresultado.value = str(int(valor1.value) *  int(valor2.value))

        page.update()

    def dividir(e):
        if valor1.value == "" or valor2.value == "":
            valor1.error_text = "por favor ingrese primer valor"
            valor2.error_text = "por favor ingrese segundo valor"       
        else:
            valor1.error_text= ''
            valor2.error_text= ''
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
    


    page.add(
             ft.Row(controls=[valor1, valor2]),
             ft.Row(
                    controls=[
                        ft.ElevatedButton(text="+", on_click = sumar),
                        ft.ElevatedButton(text="-", on_click = restar),
                        ft.ElevatedButton(text="*", on_click = multiplicar),
                        ft.ElevatedButton(text="/", on_click = dividir),
                      ]    
                    )
             )      
    page.update()

    '''page.add(ft.ElevatedButton(
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
    '''


    txtresultado = ft.TextField(hint_text="", width=200)
    page.add(txtresultado)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)        