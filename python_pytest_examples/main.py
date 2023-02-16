from tkinter import filedialog

from python_pytest_examples.parse.parser import get_parser

path = filedialog.askopenfilename(
    filetypes=[("Excel file", ".xlsx"), ("Text file", ".txt")]
)

parser, mode = get_parser(path)

with open(path, mode=mode) as file:
    report = parser.parse(file)

    for day in report:
        print(
            "Day {}, income €{}.{}, spent €{}.{}".format(
                day.day,
                str(day.income // 100),
                str(day.income % 100).ljust(2, '0'),
                str(day.spent // 100),
                str(day.spent % 100).ljust(2, '0'),
            )
        )
