import flet as ft
from flet import *


def main(page: ft.Page):

    codpro = TextField(label="CÓDIGO PRODUCTO")
    nompro = TextField(label="NOMBRE PRODUCTO")

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

    #CREAR LOS CONTROLES PARA EDITAR
    
    edit_nompro = TextField(label="NOMBRE PRODUCTO")
    edit_ddcate = Dropdown(label="CATEGORIA")
    edit_ddpeso = Dropdown(label="PESO")
    edit_codpro = TextField(label="CÓDIGO PRODUCTO")


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

    #FUNCION ELIMINAR
    def eliminar(e):
        tablaproducto.rows.remove(tablaproducto.rows[0])

        #MENSAJE con Barra inferior
        page.snack_bar = SnackBar(
            Text("SE ELIMINO DATO", size = 30),
            bgcolor = "red"            
        )
        page.snack_bar.open = True
        #FIN DEL MENSAJE inferior
 
        page.update()


    #FUNCION GUARDAR
    def guardar(e):
        pass

    # Crear Dialogo
    dialog = AlertDialog(
        title=Text("Editar datos"),
        content=Column([
            edit_nompro,
            edit_ddcate,
            edit_ddpeso,
        ]),
        actions=[
            TextButton("Guardar",
                       on_click=guardar
                       )
        ]
    )


    #Funcion EDITAR
    def editar(e):
        edit_nompro.value = TextField
        edit_ddcate.value = Dropdown
        edit_ddpeso.value = Dropdown
        

        page.dialog = dialog
        dialog.open = True
        page.update()


    

    #FUNCION para AGREGAR     
    def agregar(e):
        
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
                                   icon_color ="red",
                                   on_click = editar,
                                   ),    
                            ])
                        ),
                ]
            )
        )
        #MENSAJE con Barra inferior
        page.snack_bar = SnackBar(
            Text("DATO INGRESADO", size = 30),
            bgcolor = "green"
        )
        page.snack_bar.open = True
        #FIN DEL MENSAJE

        #Limpiar los controles
        codpro.value = ""
        nompro.value = ""
        ddcate.value = ""
        ddpeso.value = ""

        page.update()

       
    #Boton AGREGAR
    BtnAgregar = ElevatedButton(
        text="Agregar", 
        bgcolor="blue",
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