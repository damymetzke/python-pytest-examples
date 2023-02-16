from abc import ABC, abstractmethod
from typing import IO, Hashable, Tuple
import pandas as pd

from python_pytest_examples.report import Day, Report


class Parser(ABC):
    @abstractmethod
    def parse(self, file: IO) -> Report:
        pass


class TextParser(Parser):
    def parse(self, file: IO) -> Report:
        return Report(days=list(map(self.__parse_line, file)))

    @staticmethod
    def __parse_line(line: str) -> Day:
        day, income, spent = line.strip().split(" ")

        return Day(
            day=int(day),
            income=TextParser.__parse_money(income),
            spent=TextParser.__parse_money(spent),
        )

    @staticmethod
    def __parse_money(text: str) -> int:
        parts = text.split(".")
        if len(parts) == 1 or len(parts[1]) == 0:
            return int("{}00".format(parts[0]))

        if len(parts[1]) == 1:
            return int("{}{}0".format(*parts))

        return int("{}{}".format(*parts))


class ExcelParser(Parser):
    def parse(self, file: IO) -> Report:
        data = pd.read_excel(file)
        return Report(days=list(map(self.__parse_row, data.iterrows())))

    @staticmethod
    def __parse_row(row: Tuple[Hashable, pd.Series]) -> Day:
        _, data = row
        day, income, spent = data

        print(type(income))
        print(int(income * 100))

        return Day(
            day=int(day),
            income=int(income*100),
            spent=int(spent*100),
        )


MAP_PARSERS = [
    (".txt", TextParser, "r"),
    (".xlsx", ExcelParser, "rb"),
]


def get_parser(file_name: str) -> Tuple[Parser, str]:
    for extension, parser, mode in MAP_PARSERS:
        if file_name.endswith(extension):
            return (parser(), mode)
    raise Exception("Invalid file extension")
