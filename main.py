from funciones import guardar,mostrar,menu,buscar,eliminar
peliculas = []
encontrado = False
while True:
    try:
        menu()
        opt = int(input("Ingrese la opcion: "))
        if opt == 1:
            print("Guardar")        
            guardar(peliculas)
            print("Peliculas guardadas exitosamente!!!!")        
        elif opt == 2:
            print("Mostrar")
            mostrar(peliculas)        
        elif opt == 3:
            print("Eliminar")
            eliminar(peliculas)
        elif opt == 4:
            print("Buscar")
            buscar(peliculas)
        elif opt == 5:
            print("Salir")
            break
    except ValueError:
        print("Solo valores numericos")


print("Gracias, vuelva pronto, mande fruta")