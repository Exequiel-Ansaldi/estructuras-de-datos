import re
from typing import Tuple
from data_structures import ProbeHashMap

class Personaje(ProbeHashMap):
    def __init__(self, nombre, bando):
        self.nombre = nombre
        self.bando = bando

    def __repr__(self):
        return f"{self.bando}: {self.nombre}"

    @staticmethod
    def leer_archivo(archivo):
        with open(archivo, 'r') as f:
            return f.readlines()

    @staticmethod
    def clasificar_personajes(lineas):
        personajes = []
        patron = r'(?P<bando>super_heroe|villano)\((?P<nombre>[a-z_]+(?:_[a-z_]+)*)\)'
        for linea in lineas:
            linea = linea.strip()
            coincidencia = re.match(patron, linea)
            if coincidencia:
                bando = coincidencia.group('bando')
                nombre = coincidencia.group('nombre').replace("_", " ")
                personajes.append(Personaje(nombre, bando))
        
        return personajes
    
    def contar_superheroes_y_villanos(self) -> Tuple[int, int]:
        cantidad_superheroes = 0
        cantidad_villanos = 0
        
        for clave in self:
            if clave.startswith("super_heroe"):
                cantidad_superheroes += 1
            elif clave.startswith("villano"):
                cantidad_villanos += 1
        
        return cantidad_superheroes, cantidad_villanos