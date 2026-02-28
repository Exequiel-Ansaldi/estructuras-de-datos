from typing import Any, Generator, List, Tuple
from sorted_table_map_abstract import SortedTableMapAbstract

class SortedTableMap(SortedTableMapAbstract):

    def __init__(self) -> None:
        super().__init__()


    def __len__(self) -> int:
        return len(self._table)
    
    def __str__(self) -> str:
        return ', '.join(f'({item._key}: {item._value})' for item in self._table)
    
    def __getitem__(self, k: Any) -> Any:
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError(f"Key {k} no esta en el map.")
    
    def __setitem__(self, k: Any, v: Any) -> None:
        for index, item in enumerate(self._table):
            if item._key == k:
                item._value = v
                return
            elif item._key > k:
                self._table.insert(index, self._Item(k, v))
                return
        self._table.append(self._Item(k, v))


    def __delitem__(self, k: Any) -> None:
        for index, item in enumerate(self._table):
            if item._key == k:
                del self._table[index] 
                return
        raise KeyError(f"Key {k} no encontrada en el map.")
    
    def __iter__(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key

    def iter_items(self) -> Generator[Tuple[Any, Any], None, None]:
        for item in self._table:
            yield (item._key, item._value)