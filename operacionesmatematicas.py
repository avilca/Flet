import flet as ft
from flet import *



def main(page):
    page.title = "Operaciones Matemáticas"
    
    def mostrar_valor1(event):
        page.dialog = dlg_valor1
        dlg_valor1.open = True
        page.update()    
    
    def cerrar_msg1(event):
        dlg_valor1.open = False
        page.update()    

    dlg_valor1 = ft.AlertDialog(
        modal=True, 
        title=ft.Text("Atención"),
        content=ft.Text("Falta ingresar el valor 1"), 
        actions=[
            ft.TextButton("De acuerdo", on_click=cerrar_msg1)],
        actions_alignment=ft.MainAxisAlignment.END)
    
    
    def cerrar_msg2(event):
        dlg_valor2.open = False
        page.update()
    
    dlg_valor2 = ft.AlertDialog(
        modal=True,
        title=ft.Text("Atención"),
        content=ft.Text("Falta ingresar el valor 2"),
        actions=[
            ft.TextButton("De acuerdo", on_click=cerrar_msg2)],
        actions_alignment=ft.MainAxisAlignment.END)
 
    
        
    def mostrar_valor2(event):
        page.dialog = dlg_valor2
        dlg_valor2.open = True
        page.update()    
        
    def valida_campos(event):
        if valor1.value == "":
            mostrar_valor1(event)
            return 
            
        if valor2.value == "":
            mostrar_valor2(event)
            return 
    
    
 
    def sumar(e):
                
        if valor1.value == "" or valor2.value == "":
            valida_campos(e)      
        else:
            valor1.error_text= ''
            valor2.error_text= ''
            txtresultado.value = str(int(valor1.value) +  int(valor2.value)) 

        page.update()

    def restar(e):
        if valor1.value == "" or valor2.value == "":
            valida_campos()    
        else:
            valor1.error_text= ''
            valor2.error_text= ''
            txtresultado.value = str(int(valor1.value) -  int(valor2.value))

        page.update()  

    def multiplicar(e):
        if valor1.value == "" or valor2.value == "":
            valida_campos()       
        else:
            valor1.error_text= ''
            valor2.error_text= ''
            txtresultado.value = str(int(valor1.value) *  int(valor2.value))

        page.update()

    def dividir(e):
        if valor1.value == "" or valor2.value == "":
            valida_campos()     
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


    txtresultado = ft.TextField(hint_text="", width=200)
    page.add(txtresultado)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER) 