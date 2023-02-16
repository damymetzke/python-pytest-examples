from dataclasses import dataclass
from typing import List


@dataclass
class Day():
    day: int
    income: int
    spent: int


@dataclass
class Report():
    days: List[Day]
