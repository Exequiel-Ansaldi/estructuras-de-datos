from sorted_table_map import SortedTableMap

class SortedTableMapClient(SortedTableMap):
    def main():
        map_instance = SortedTableMap()
        print("Añadiendo elementos...")
        map_instance['a'] = 10
        map_instance['c'] = 30
        map_instance['b'] = 20



        print("Contenido del mapa:", map_instance)
        print("Actualizando el valor de la clave 'b' a 25")
        map_instance['b'] = 25
        print("Valor de la clave 'b':", map_instance['b'])  
        try:
            print("Valor de la clave 'd':", map_instance['d'])
        except KeyError as e:
            print(e) 




        print("Eliminando la clave 'a'...")
        del map_instance['a']
        print("Contenido del mapa tras la eliminación de 'a':", map_instance)
        try:
            print("Valor de la clave 'a':", map_instance['a']) 
        except KeyError as e:
            print(e)



        print("Iterando sobre las claves del mapa:")
        for key in map_instance:
            print(key)



        print("Iterando sobre los ítems del mapa:")
        for item in map_instance.iter_items():
            print(item)
        

    if __name__ == "__main__":
        main()