from abc import ABC, abstractmethod
from io import TextIOBase

from python_pytest_examples.report import Day, Report


class Parser(ABC):
    @abstractmethod
    def parse(self, file: TextIOBase) -> Report:
        pass


class TextParser(Parser):
    def parse(self, file: TextIOBase) -> Report:
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


MAP_PARSERS = [
    (".txt", TextParser),
]


def get_parser(file_name: str) -> Parser:
    for extension, parser in MAP_PARSERS:
        if file_name.endswith(extension):
            return parser()
    raise Exception("Invalid file extension")
