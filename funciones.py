
def menu():
    print("----Tienda de peliculas----")
    print("1. Guardar pelicula")
    print("2. Mostrar pelicula")
    print("3. Buscar pelicula")
    print("4. Eliminar pelicula")
    print("5. Salir")


def guardar(nombre,tipo,publicacion,peliculas_lista,i):    
    pelicula = {
        "id": i,
        "nombre": nombre,
        "tipo": tipo,
        "publicacion":publicacion
    }

    peliculas_lista.append(pelicula)

def mostrar(peliculas_lista):
    for peli in peliculas_lista:
        print(f"El id es: {peli["id"]}")
        print(f"El nombre es: {peli["nombre"]}")
        print(f"El tipo es: {peli["tipo"]}")
        print(f"La publicacion es: {peli["publicacion"]}")