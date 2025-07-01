from funciones import guardar,menu,mostrar

peliculas = []
while True:
    menu()
    opt = int(input("Ingrese una opcion: "))
    if opt == 1:
        print("Guardar")
        cantidad = int(input("Ingrese la cantidad de peliculas a guardar: "))

        for i in range(1,cantidad + 1):    
            nombre = input(f"Ingrese el nombre de la {i} pelicula: ")
            tipo = input("Ingrese el tipo de la pelicula: ")
            publicacion = input("Ingrese el año de su publicación: ")
            guardar(nombre,tipo,publicacion,peliculas,i)
    elif opt == 2:
        mostrar(peliculas)
    elif opt == 3:
        print("Buscar")
    elif opt == 4:
        print("Eliminar")
    elif opt == 5:
        break
        