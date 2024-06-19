from PySide6.QtWidgets import QApplication
import sys
from re import compile

from main_window import MainWindow

from changer import add_break


# def process_input(input_text):
#     # Split the input text into lines
#     lines = input_text.strip().split('\n')

#     # Remove semicolons from each line and strip any extra whitespace
#     cleaned_lines = [line.replace(';', '').strip() for line in lines]

#     return cleaned_lines


# def get_variables(input_string):
#     var_pattern = compile(r'[a-zA-Zα-ωΓ-Ω]+')
#     variables = set(var_pattern.findall(input_string))
#     return variables


# file = open(f'input.mac', "r+")

# FileInput = file.read()
# print(FileInput)

# InputList = process_input(FileInput)
# for i in InputList:
#     print(i)

# f = InputList[0]
# n = InputList[1]
# discontinuous_quantities = get_variables(InputList[2])



# add_break(f, n, discontinuous_quantities)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())