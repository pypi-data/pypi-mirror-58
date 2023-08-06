"""Union-Find data structures & helper objects"""
from typing import Iterable, Any, Optional


class Partition:
    """A partition is a set of elements with a name, used to identify that all of those objects."""

    def __init__(self, name: str, elements: Iterable[Any]) -> None:
        self.name: str = name
        self._elements = set(elements)

    def __contains__(self, element: Any) -> bool:
        return element in self._elements

    def __len__(self) -> int:
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    def __or__(self, other):
        if self.__class__ is other.__class__:
            return self.__class__(name=f"{self.name}_{other.name}", elements=self._elements | set(other))
        return NotImplemented


class UnionFindSpace:
    """Manage the partitions of different objects, and allow for them to be found and merged."""

    def __init__(self, *partitions: Partition) -> None:
        self._partitions: dict = {p.name: p for p in partitions}
        self._element_to_partition: dict = {e: p.name for p in partitions for e in p}

    def __len__(self) -> int:
        return len(self._partitions)

    def find(self, element: Any) -> Partition:
        return self._element_to_partition[element]

    def union(self, partition1_name: str, partition2_name: str, new_name: Optional[str] = None) -> Partition:
        """Merge the two partitions given by their names (first & second parameters, respectively), into a new one."""

        partition_1 = self._partitions.pop(partition1_name)
        partition_2 = self._partitions.pop(partition2_name)

        new_partition = partition_1 | partition_2
        new_partition.name = new_name or new_partition.name

        self._partitions[new_partition.name] = new_partition
        for e in new_partition:
            self._element_to_partition[e] = new_partition.name

        return new_partition
