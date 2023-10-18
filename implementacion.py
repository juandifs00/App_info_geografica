from abc import ABC, abstractmethod
from typing import List

# Interfaz Exportable
class Exportable(ABC):
    @abstractmethod
    def exportar(self) -> str:
        pass
    
# Clase Nodo
class NodoCiudad(Exportable):
    def __init__(self, nombre: str, estado: str) -> None:
        self.nombre = nombre
        self.estado = estado

    def exportar(self) -> str:
        return f"<nodo_ciudad nombre='{self.nombre}' estado='{self.estado}' />"
    
class NodoIndustria(Exportable):
    def __init__(self, nombre: str, estado: str) -> None:
        super().__init__()
        self.nombre = nombre
        self.estado = estado

    def exportar(self) -> str:
        return f"<nodo_industria nombre='{self.nombre}' estado='{self.estado}' />"

class NodoLugarTurismo(Exportable):
    def __init__(self, nombre: str, estado: str, tipo: str) -> None:
        super().__init__()
        self.nombre = nombre
        self.estado = estado
        self.tipo = tipo

    def exportar(self) -> str:
        return f"<nodo_lugar_turismo nombre='{self.nombre}' estado='{self.estado}' tipo='{self.tipo}' />"

# Clase Enlace
class Enlace:
    def __init__(self, origen: NodoCiudad, destino: NodoCiudad) -> None:
        self.origen = origen
        self.destino = destino

# Clase Grafo
class Grafo:
    def __init__(self) -> None:
        self.nodos: List[NodoCiudad] = []
        self.enlaces: List[Enlace] = []

    def agregar_nodo(self, nodo: NodoCiudad) -> None:
        self.nodos.append(nodo)

    def agregar_enlace(self, enlace: Enlace) -> None:
        self.enlaces.append(enlace)

    def exportar(self) -> str:
        xml = f"<grafo>"
        for nodo in self.nodos:
            xml += nodo.exportar()
        for enlace in self.enlaces:
            xml += f"<enlace origen='{enlace.origen.nombre}' destino='{enlace.destino.nombre}' />"
        xml += "</grafo>"
        return xml

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_nodo(NodoCiudad("Bogota", "Colombia"))
grafo.agregar_nodo(NodoCiudad("Medellin", "Colombia"))

grafo.agregar_nodo(NodoIndustria("Industria 1", "Colombia"))
grafo.agregar_nodo(NodoIndustria("Industria 2", "Colombia"))

grafo.agregar_nodo(NodoLugarTurismo("Lugar turistico 1", "Colombia", "Parque"))
grafo.agregar_nodo(NodoLugarTurismo("Lugar turistico 2", "Colombia", "Museo"))

grafo.agregar_enlace(Enlace(grafo.nodos[0], grafo.nodos[1]))
grafo.agregar_enlace(Enlace(grafo.nodos[2], grafo.nodos[3]))
grafo.agregar_enlace(Enlace(grafo.nodos[4], grafo.nodos[5]))

print(grafo.exportar()) 