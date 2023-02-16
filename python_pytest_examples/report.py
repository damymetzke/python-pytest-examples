from dataclasses import dataclass
from typing import Iterator, List


@dataclass
class Day:
    day: int
    income: int
    spent: int


@dataclass
class Report:
    days: List[Day]

    def __iter__(self) -> Iterator[Day]:
        return iter(self.days)
