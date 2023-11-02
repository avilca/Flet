import flet as ft
from flet import *


def main(page):


    #Tamaño de ventana 
    page.window_resizable = False
        

    #CONTROLES (Controls)

    codpro = TextField(label="CÓDIGO PRODUCTO", width = 200)
    nompro = TextField(label="NOMBRE PRODUCTO", width = 600)

    #combo de categoria (Category)
    ddcate = Dropdown(label="CATEGORIA",
        width=150,
        options=[
            dropdown.Option("dulce"),
            dropdown.Option("salado"),
        ],
    )

    #combo de peso (weight)
    ddpeso = Dropdown(label="PESO",
        width=100,
        options=[
            dropdown.Option("KG"),
            ft.dropdown.Option("G"),
        ],
    )

    #CONTROLES PARA EDITAR DATOS (Controls for Edit)
    edit_nomprotxt = TextField(label="NOMBRE PRODUCTO")

    edit_ddcate = Dropdown(label="CATEGORIA",
        width=150,
        options=[
            dropdown.Option("dulce"),
            dropdown.Option("salado"),
        ],
    )

    edit_ddpeso = Dropdown(label="PESO",
        width=100,
        options=[
            dropdown.Option("KG"),
            dropdown.Option("G"),
        ],
    )


    #DATATABLE
    tablaproducto = DataTable(
                  #CABECERA DE LAS CALUMNAS  
                  columns=[
                      DataColumn(Text("CÓDIGO")),
                      DataColumn(Text("PRODUCTO")),
                      DataColumn(Text("CATEGORÍA")),
                      DataColumn(Text("PESO")),
                      DataColumn(Text("ACCIONES")),
                  ],
                  #FILAS  
                  rows=[]          
    )



    def cerrar_mensaje(e):
        dialog2.open = False
        page.update()


    def mostrar_mensaje(e):
        page.dialog = dialog2
        dialog2.open = True
        page.update()

    
    #DIALOG PARA MENSAJE DE CAMPOS VACIOS
    dialog2 = AlertDialog(
        
        title=Text("Algún campo esta vacío. \nPOR FAVOR ingrese los datos", color="red"),
        actions=[
            ElevatedButton("Aceptar",
                       on_click=cerrar_mensaje, 
                       bgcolor= "red", 
                       color= "white",
                      ),        
        ],
    )    


    #FUNCION ELIMINAR (Function Delete)
    def eliminar(e):
        tablaproducto.rows.remove(tablaproducto.rows[0])

        #MENSAJE con Barra inferior
        page.snack_bar = SnackBar(
            Text("SE ELIMINO DATO", size = 30),
            bgcolor = "red",
            duration= 450,            
        )
        page.snack_bar.open = True
        #FIN DEL MENSAJE inferior
 
        page.update()



    #Funcion GUARDAR (Function Save)
    def guardar(e):

        e.control.data = "OFF"
        filas = tablaproducto.rows[:]
        for valor in filas:
            if valor.cells[-1].content.controls[1].data == 'OFF':
                fila = filas.index(valor)
       
        tablaproducto.rows[fila].cells[1].content.value = edit_nomprotxt.value
        tablaproducto.rows[fila].cells[2].content.value = edit_ddcate.value
        tablaproducto.rows[fila].cells[3].content.value = edit_ddpeso.value

        page.dialog = dialog
        dialog.open = False
        page.update()       


    def cerrar_dialog1(e):
        dialog.open = False
        page.update()
    


    # Crear Dialog
    dialog = AlertDialog(
        title=Text("Modificando datos"),
        content=Column([
            edit_nomprotxt,
            edit_ddcate,
            edit_ddpeso,              
         ]),
        actions=[
            ElevatedButton("Guardar",
                       on_click=guardar, 
                       bgcolor= "green", 
                       color= "white",
                      ),

            ElevatedButton("Cancelar", 
                           bgcolor = "red", 
                           color = "white",
                           on_click=cerrar_dialog1
                      ),
        ],
    )

    #Funcion EDITAR (Function Edit)
    def editar(e):
           
        e.control.data = "ON"
        filas = tablaproducto.rows[:]
        for valor in filas:
            if valor.cells[-1].content.controls[1].data == 'ON':
                fila = filas.index(valor)


        e.control.data = "OFF"
        edit_nomprotxt.value = tablaproducto.rows[fila].cells[1].content.value
        edit_ddcate.value = tablaproducto.rows[fila].cells[2].content.value
        edit_ddpeso.value = tablaproducto.rows[fila].cells[3].content.value
       

        page.dialog = dialog
        dialog.open = True
        page.update()


    #FUNCION para AGREGAR (Function Add)    
    def agregar(e):
        
        
        lista = [codpro, nompro, ddcate, ddpeso]
        
        check = False

        for campo in lista:
            if campo.value == '' or not campo.value:
                mostrar_mensaje(e)
                check = True

        if check == False:
            tablaproducto.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(codpro.value)),
                            DataCell(Text(nompro.value)),
                            DataCell(Text(ddcate.value)),
                            DataCell(Text(ddpeso.value)),
                            DataCell(
                                Row([
                                IconButton("delete", 
                                        icon_color ="red",
                                        on_click = eliminar,
                                            ),
                                IconButton("create", 
                                        icon_color ="blue",
                                        on_click = editar
                                        ),    
                                    ])
                                ),
                        ]
                    )
                )
                #MENSAJE con Barra inferior
            page.snack_bar = SnackBar(
                    Text("DATO INGRESADO", size = 30),
                    bgcolor = "green",
                    duration= 450,
                )
            page.snack_bar.open = True
                #FIN DEL MENSAJE

                #Limpiar los controles
            codpro.value = ""
            nompro.value = ""
            ddcate.value = ""
            ddpeso.value = ""
            BtnAgregar.focus()
            page.update()

       
    #Boton AGREGAR
    BtnAgregar = ElevatedButton(
        text="Agregar", 
        bgcolor="green",
        color="white",
        on_click=agregar
        )
    

    page.add(
		Column([
			Text("PRODUCTOS",size=30,weight="bold"),
			codpro, nompro,ddcate, ddpeso,
			Row([BtnAgregar]),
			tablaproducto
 
			])
 
		)


ft.app(target=main)