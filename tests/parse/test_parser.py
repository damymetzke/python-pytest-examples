from python_pytest_examples.parse.parser import TextParser, get_parser
from python_pytest_examples.report import Day, Report


def test_text_parser_used_for_text_file():
    result = get_parser("filename.txt")
    assert isinstance(result, TextParser)


def test_text_parser_can_read_file():
    INPUT = open("test_resources/parser_input.txt")
    EXPECTED = Report(
        days=[
            Day(day=1, income=110, spent=220),
            Day(day=2, income=200, spent=3333),
            Day(day=3, income=33300, spent=400),
            Day(day=4, income=0, spent=555),
        ]
    )

    parser = TextParser()
    result = parser.parse(INPUT)

    assert result == EXPECTED
