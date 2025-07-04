
peliculas = []

cantidad = int(input("Ingrese la cantidad de peliculas a guardar: "))


for i in range(1,cantidad+1):
    print(f"-----------Guardar {i} Pelicula--------------")
    nombre = input("Ingrese el nombre de la pelicula: ")
    anio = int(input("Ingrese el año de estreno: "))
    peliculas.append({
        "nombre": nombre,
        "año": anio
    })

    for indice,pelicula in enumerate(peliculas):
        print(f"{indice+1} - {pelicula["nombre"]} - {pelicula["año"]}")




#sexo = ["m","f"]



