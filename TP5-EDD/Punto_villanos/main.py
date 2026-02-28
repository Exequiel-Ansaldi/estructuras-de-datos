from Personaje import Personaje
class Ejecutable:
    @staticmethod
    def main():
        archivo = 'superheroes_villanos.txt' 
        lineas = Personaje.leer_archivo(archivo)
        personajes = Personaje.clasificar_personajes(lineas)
        for personaje in personajes:
            print(personaje)

        mapa = Personaje()
        cantidad_superheroes, cantidad_villanos = mapa.contar_superheroes_y_villanos()
        print(f"Cantidad de superheroes: {cantidad_superheroes}")
        print(f"Cantidad de villanos: {cantidad_villanos}")

if __name__ == "__main__":
    Ejecutable.main()