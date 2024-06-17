import sys
import os
# import re
from re import compile

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtWidgets
# from PySide6.QtWidgets import *

from changer import add_break
from ui_main import Ui_MainWindow


def process_input(input_text):
    # Split the input text into lines
    lines = input_text.strip().split('\n')

    # Remove semicolons from each line and strip any extra whitespace
    cleaned_lines = [line.replace(';', '').strip() for line in lines]

    return cleaned_lines


def get_variables(input_string):
    var_pattern = compile(r'[a-zA-Zα-ωΓ-Ω]+')
    variables = set(var_pattern.findall(input_string))
    return variables


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.load_button.clicked.connect(self.open_file)
        self.ui.save_button.clicked.connect(self.save_file)
        self.ui.slave_button.clicked.connect(self.slove_func)
        # self.ui.pushButton.clicked.connect(self.get_cursor_position)



    def open_file(self):
        
        nofile = ('', '')
        current_folder_path = os.getcwd()
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", current_folder_path,
                                            "Maxima Files (*.mac)")
        
        if filename != nofile:
            file = open(filename[0], "r+")

            FileInput = file.read()
            print(FileInput)

            InputList = process_input(FileInput)
            for i in InputList:
                print(i)

            f = InputList[0]
            n = InputList[1]
            discontinuous_quantities = get_variables(InputList[2])

            self.ui.formula_input.clear()
            self.ui.formula_input.append(f)

            self.ui.atoms_input.setText(' '.join(discontinuous_quantities))

            self.ui.split_input.setValue(int(n))

    def save_file(self):
        nofile = ('', '')
        current_folder_path = os.getcwd()
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", current_folder_path,
                                            "Maxima Files (*.mac)")
        
        if filename != nofile:
            if '.mac' in filename[0]:
                out_file = open(filename[0], "w")
            else:
                out_file = open(filename[0] + '.mac', "w")

            out_file.write(self.ui.solution_input.toPlainText())
            out_file.close
        print(filename)

    def slove_func(self):
        f = self.ui.formula_input.toPlainText()
        n = self.ui.split_input.value()
        atoms = get_variables(self.ui.atoms_input.text())
        print(f)
        print(n)
        print(atoms)
        self.ui.solution_input.clear()
        self.ui.solution_input.append(add_break(f, n, atoms))

    # def get_cursor_position(self):
    #     self.ui.formula_input.textCursor().insertText('Done')
    #     print(self.ui.formula_input.textCursor().position())

    #     self.ui.atoms_input.insert('atom')
    #     print(self.ui.atoms_input.cursorPosition())