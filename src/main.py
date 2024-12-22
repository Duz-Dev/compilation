import flet as ft


def main(page: ft.Page):
    #?Configuraciones de la ventana
    page.title = "Lista de Tareas. By PablOS" #Titulo de la ventana
    page.bgcolor = "#250e42" #color de fondo
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #Alinea los elementos al centro por defecto en toda la pagina
    #tamaño de la ventana
    page.window.width = 450 
    page.window.height = 800   
    page.window.alignment = ft.alignment.center #Alineo la ventana al centro
    page.window.resizable = False #Desactivo que se pueda redimensionar
    
    
    #?Variables
    tareas:list = []#Lista que recolecta las tareas creadas
    
    #?controles
    #Titulo dentro de la app
    title = ft.Container(
            content=ft.Text(value="LISTA DE TAREAS", size=30,color=ft.Colors.WHITE,weight=ft.FontWeight.BOLD),
            padding=ft.padding.only(top=40)#Método especial para indicar un espaciado especifico, en este caso añadí 40pxv (40 pixeles virtuales), por el problema del notch en movil.
            )
    page.add(title)
    
    #Widget de texto de entrada para añadir tareas    
    tarea_input = ft.TextField(hint_text="Escribe una tarea nueva",autofocus=True,text_size=18,color=ft.Colors.BLACK,border_color=ft.Colors.WHITE,fill_color=ft.Colors.WHITE,border_radius=5)
    page.add(ft.Container(content=tarea_input,padding=5 ))
    
    #?Acciones de la app
    def añadir_tareas(e):
        """
        ### Acción: Añadir tareas
        Esta función ira recolectando el texto agregado a el `TextFild` y lo añadira a el control de tipo ``ListTile` (Una sola fila de altura fija que generalmente contiene algo de texto, así como un icono principal o posterior.)
        
        Variables:
        -   Tarea[ft.ListTile]: Hace uso de el texto de tarea_input.value y lo añade a un control Text, y le adjunta antes de añadir dicho text un control Checkbox.
        -   Tareas[List]: Posteriormente añadimos dicha tarea creada en el listTile a la lista Tareas.
        """
        if tarea_input.value: #Si tarea_input NO esta vació, procede con lo sig:
            tarea = ft.ListTile(
                title=ft.Text(tarea_input.value),
                
                leading=ft.Checkbox(on_change=seleccionar_tarea,active_color=ft.Colors.BLUE_400,focus_color="#cccccc",fill_color=ft.Colors.WHITE,check_color=ft.Colors.BLACK),
                
                bgcolor="#55367a",text_color=ft.Colors.WHITE
                )
            tareas.append(tarea)#Añadimos la tarea a la lista tareas
            tarea_input.value = "" #limpiamos el input de tareas
            actualizar_lista()#llamamos la función Actualizar lista para que refleje las nuevas tareas añadidas
            tarea_input.focus()#Hace focus nuevamente sobre el input
            page.update()
    
    def seleccionar_tarea(e):
        """
        ### Acción: Seleccionar tareas
        
        Variables
        -   seleccionadas[List]: Recorremos la lista `tareas` y posteriormente creamos una lista nueva el cual solo contenga los textos de los `listTile` si dicho control tiene seleccionado su checkbox.
        
        argumento:
            e (_type_): Argumento obligatorio. Representa el evento que se produce al realizar una acción, como un clic en un botón. Flet espera que esa función acepte un parámetro para capturar el evento generado, dicho parámetro es la variable `e`. Este parámetro contiene detalles sobre el evento. Aunque no se utilice dentro de la función, es obligatorio incorporarlo, si esta función es utilizada por algun evento externo como el de los botones que añadí.
        """
        seleccionadas = [t.title.value for t in tareas if t.leading.value]#Utilizo  comprensión de listas (list comprehension).
        
        tareas_seleccionadas.value = "tareas seleccionadas: " + ", ".join(seleccionadas) #El párrafo final de la pagina tendrá la lista en formato str creada en `seleccionadas`
        page.update()
        
    def actualizar_lista():
        """
        ### Acción: Actualizar la lista_tareas
        Función especifica para poder limpiar elementos previamente añadidos al control `listView` llamado `lista_tareas` y posteriormente mostrar los elementos actualmente alojados en la lista `tareas` (los cuales si recordamos son los `ListTile`).
        """
        lista_tareas.controls.clear()#Eliminamos todos los elementos de la lista. Esto es importante ya que de lo contrario el control no nos permitirá añadir los nuevos elementos generados.
        
        lista_tareas.controls.extend(tareas)#añadimos todos los elementos de la lista tareas.
        page.update()
        
    def eliminar_lista(e):
        """
        ### Acción: Eliminar elementos de la lista
        Elimina cada rastro generado de las tareas, como el control creado ListView `Lista_tareas`, limpiamos la lista `tareas` y el control Text que alberga el párrafo de `tareas_seleccionadas`, este ultimo añadido al final de la pagina. 
        
        Argumento:
            e (_type_): Obligatorio. Ya que la función es llamada por un evento
        """
        lista_tareas.controls.clear()# Limpia la lista que recolecto los controles de `tareas` usando el método `clear()`
        tareas.clear()# Limpia la lista eliminando cada elemento dentro de esta.
        tareas_seleccionadas.value = "" #el párrafo al final de la pagina es eliminado quitándole el texto
        page.update()
    
    #?Botones principales
    button_agregar = ft.Container(
        content=ft.Row(
            controls=[
                #>>>Botón: Agregar tareas
                ft.FilledButton(text="Agregar tarea",width=180,color=ft.Colors.WHITE,height=35,on_click=añadir_tareas,bgcolor="#55367a"),#Llama a la función añadir_tareas cuando le dan clic a este mismo.
                #>>>Botón: Eliminar lista completa
                ft.FilledButton(text="Eliminar lista",width=180,color=ft.Colors.WHITE,height=35,on_click=eliminar_lista,bgcolor="#55367a")#Llama a la función eliminar_lista para eliminar todos los elementos generados.

            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        padding=10)
    page.add(button_agregar)
    
    #?Visual. Lista de tareas
    lista_tareas = ft.ListView(expand=1,spacing=3)#Creamos un control de tipo ListView el cual contendrá todos los listTile que creamos que están en la lista Tareas. El valor de `expand=1`Indica que la pagina se expandera por completo hasta donde abarque toda la pantalla. `spacing=3` añade un espacio entre los controles que se añadan a este de 3 pixeles virtuales.
    page.add(lista_tareas)
    
    #?Visual. Párrafo de tareas seleccionadas
    tareas_seleccionadas = ft.Text(value="",size=20,weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    #Añadimos un control Text al final de la pagina el cual contendrá un texto con todos los checkbox seleccionados
    
    page.add(tareas_seleccionadas)   
    
    

ft.app(main)