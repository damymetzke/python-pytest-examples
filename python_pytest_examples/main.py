from tkinter import filedialog

from python_pytest_examples.parse.parser import get_parser

path = filedialog.askopenfilename(
    filetypes=[("Excel file", ".xlsx"), ("Text file", ".txt")]
)

parser = get_parser(path)

with open(path) as file:
    print(parser.parse(file))

