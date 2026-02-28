from typing import Any, List, Generator
from abc import ABC, abstractmethod
from data_structures import MapBase

class SortedTableMapAbstract(MapBase, ABC):
    """Implementa un Mapeo utilizando una lista built-in Python ordenada. Los elementos se
    insertan en orden ascendente de clave.
    Args:
    MapBase: hereda los métodos de MapBase y de su superclase MutableMapping (de Python).
    """

    
    def __init__(self) -> None:
        """Crea la lista Python donde se almacenarán todas las entradas como una lista
        vacía."""
        self._table: List[MapBase._Item] = []



    @abstractmethod
    def __len__(self) -> int:
        """Devuelve la cantidad de entradas en el Mapeo.
        Returns:
        int: devuelve la longitud de la lista self._table
        """
        pass

    
    def __repr__(self) -> str:
        """Convierte en str el Mapeo.
        Returns:
        str: Convierte en str el Mapeo invocando a self.__str__()
        """
        return str(self)
    


    @abstractmethod
    def __str__(self) -> str:
        """Convierte en str el Mapeo.
        Returns:
        str: Concatena la versión en str de todas las entradas del Mapeo.
        """
        pass



    @abstractmethod
    def __getitem__(self, k: Any) -> Any:
        """Devuelve el valor asociado a la clave k en el Mapeo.
            Args:
            k (Any): clave del ítem que hay que buscar.
            Raises:
            KeyError: Arroja KeyError cuando la clave no pertenece al Mapeo.
            Returns:
            Any: Devuelve el _value del ítem cuya clave coincide con k.
            """
        pass


    @abstractmethod
    def __setitem__(self, k: Any, v: Any) -> None:
        """Establece como v como el nuevo valor del ítem con clave k.
        Args:
        k (Any): clave que se va a buscar en el mapeo.
        v (Any): valor para asignar al ítem con clave que k.
        """
        pass


    @abstractmethod
    def __delitem__(self, k: Any) -> None:
        """Elimina del Mapeo el ítem con clave k.
        Args:
        k (Any): clave que se va a buscar en los ítems del Mapeo.
        Raises:
        KeyError: Es arrojado cuando la clave k no se encuentra en el mapeo.
        """
        pass


    @abstractmethod
    def __iter__(self) -> Generator[Any, None, None]:
        """Devuelve un generator sobre el Mapeo que devuelve todas las claves.
        Yields:
        Generator[Any, None, None]: devuelve todas las claves del Mapeo.
        """
        pass


    @abstractmethod
    def iter_items(self) -> Generator[Any, None, None]:
        """Devuelve un generator sobre el Mapeo que devuelve todos los ítems.
        Yields:
        Generator[Any, None, None]: devuelve todas los ítems del Mapeo.
        """
        pass