import sys
import os
from re import compile

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtWidgets

from changer import add_break
from ui_main import Ui_MainWindow



def process_input(input_text):
    lines = input_text.strip().split('\n')
    cleaned_lines = [line.replace(';', '').strip() for line in lines]
    return cleaned_lines



def get_variables(input_string):
    var_pattern = compile(r'[a-zA-Zα-ωΓ-Ω_0-9]+')
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
        
        self.ui.f_button1.clicked.connect(lambda: self.add_symb_to_form('α'))
        self.ui.f_button2.clicked.connect(lambda: self.add_symb_to_form('β'))
        self.ui.f_button3.clicked.connect(lambda: self.add_symb_to_form('γ'))
        self.ui.f_button4.clicked.connect(lambda: self.add_symb_to_form('δ'))
        self.ui.f_button5.clicked.connect(lambda: self.add_symb_to_form('ε'))
        self.ui.f_button6.clicked.connect(lambda: self.add_symb_to_form('ζ'))
        self.ui.f_button7.clicked.connect(lambda: self.add_symb_to_form('η'))
        self.ui.f_button8.clicked.connect(lambda: self.add_symb_to_form('θ'))
        self.ui.f_button9.clicked.connect(lambda: self.add_symb_to_form('ι'))
        self.ui.f_button10.clicked.connect(lambda: self.add_symb_to_form('κ'))
        self.ui.f_button11.clicked.connect(lambda: self.add_symb_to_form('λ'))
        self.ui.f_button12.clicked.connect(lambda: self.add_symb_to_form('ν'))
        self.ui.f_button13.clicked.connect(lambda: self.add_symb_to_form('ξ'))
        self.ui.f_button14.clicked.connect(lambda: self.add_symb_to_form('π'))
        self.ui.f_button15.clicked.connect(lambda: self.add_symb_to_form('ρ'))
        self.ui.f_button16.clicked.connect(lambda: self.add_symb_to_form('σ'))
        self.ui.f_button17.clicked.connect(lambda: self.add_symb_to_form('τ'))
        self.ui.f_button18.clicked.connect(lambda: self.add_symb_to_form('υ'))
        self.ui.f_button19.clicked.connect(lambda: self.add_symb_to_form('φ'))
        self.ui.f_button20.clicked.connect(lambda: self.add_symb_to_form('χ'))
        self.ui.f_button21.clicked.connect(lambda: self.add_symb_to_form('ψ'))
        self.ui.f_button22.clicked.connect(lambda: self.add_symb_to_form('ω'))
        self.ui.f_button23.clicked.connect(lambda: self.add_symb_to_form('Γ'))
        self.ui.f_button24.clicked.connect(lambda: self.add_symb_to_form('Δ'))
        self.ui.f_button25.clicked.connect(lambda: self.add_symb_to_form('Θ'))
        self.ui.f_button26.clicked.connect(lambda: self.add_symb_to_form('Λ'))
        self.ui.f_button27.clicked.connect(lambda: self.add_symb_to_form('Ξ'))
        self.ui.f_button28.clicked.connect(lambda: self.add_symb_to_form('Π'))
        self.ui.f_button29.clicked.connect(lambda: self.add_symb_to_form('Σ'))
        self.ui.f_button30.clicked.connect(lambda: self.add_symb_to_form('Φ'))
        self.ui.f_button31.clicked.connect(lambda: self.add_symb_to_form('Ψ'))
        self.ui.f_button32.clicked.connect(lambda: self.add_symb_to_form('Ω'))

        self.ui.f_button1_2.clicked.connect(lambda: self.add_symb_to_atoms('α'))
        self.ui.f_button2_2.clicked.connect(lambda: self.add_symb_to_atoms('β'))
        self.ui.f_button3_2.clicked.connect(lambda: self.add_symb_to_atoms('γ'))
        self.ui.f_button4_2.clicked.connect(lambda: self.add_symb_to_atoms('δ'))
        self.ui.f_button5_2.clicked.connect(lambda: self.add_symb_to_atoms('ε'))
        self.ui.f_button6_2.clicked.connect(lambda: self.add_symb_to_atoms('ζ'))
        self.ui.f_button7_2.clicked.connect(lambda: self.add_symb_to_atoms('η'))
        self.ui.f_button8_2.clicked.connect(lambda: self.add_symb_to_atoms('θ'))
        self.ui.f_button9_2.clicked.connect(lambda: self.add_symb_to_atoms('ι'))
        self.ui.f_button10_2.clicked.connect(lambda: self.add_symb_to_atoms('κ'))
        self.ui.f_button11_2.clicked.connect(lambda: self.add_symb_to_atoms('λ'))
        self.ui.f_button12_2.clicked.connect(lambda: self.add_symb_to_atoms('ν'))
        self.ui.f_button13_2.clicked.connect(lambda: self.add_symb_to_atoms('ξ'))
        self.ui.f_button14_2.clicked.connect(lambda: self.add_symb_to_atoms('π'))
        self.ui.f_button15_2.clicked.connect(lambda: self.add_symb_to_atoms('ρ'))
        self.ui.f_button16_2.clicked.connect(lambda: self.add_symb_to_atoms('σ'))
        self.ui.f_button17_2.clicked.connect(lambda: self.add_symb_to_atoms('τ'))
        self.ui.f_button18_2.clicked.connect(lambda: self.add_symb_to_atoms('υ'))
        self.ui.f_button19_2.clicked.connect(lambda: self.add_symb_to_atoms('φ'))
        self.ui.f_button20_2.clicked.connect(lambda: self.add_symb_to_atoms('χ'))
        self.ui.f_button21_2.clicked.connect(lambda: self.add_symb_to_atoms('ψ'))
        self.ui.f_button22_2.clicked.connect(lambda: self.add_symb_to_atoms('ω'))
        self.ui.f_button23_2.clicked.connect(lambda: self.add_symb_to_atoms('Γ'))
        self.ui.f_button24_2.clicked.connect(lambda: self.add_symb_to_atoms('Δ'))
        self.ui.f_button25_2.clicked.connect(lambda: self.add_symb_to_atoms('Θ'))
        self.ui.f_button26_2.clicked.connect(lambda: self.add_symb_to_atoms('Λ'))
        self.ui.f_button27_2.clicked.connect(lambda: self.add_symb_to_atoms('Ξ'))
        self.ui.f_button28_2.clicked.connect(lambda: self.add_symb_to_atoms('Π'))
        self.ui.f_button29_2.clicked.connect(lambda: self.add_symb_to_atoms('Σ'))
        self.ui.f_button30_2.clicked.connect(lambda: self.add_symb_to_atoms('Φ'))
        self.ui.f_button31_2.clicked.connect(lambda: self.add_symb_to_atoms('Ψ'))
        self.ui.f_button32_2.clicked.connect(lambda: self.add_symb_to_atoms('Ω'))



    def open_file(self):
        nofile = ('', '')
        current_folder_path = os.getcwd()
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", current_folder_path,
                                            "Maxima Files (*.mac)")
        
        if filename != nofile:
            file = open(filename[0], "r+")

            FileInput = file.read()

            InputList = process_input(FileInput)

            f = InputList[0]
            n = InputList[1]
            atoms = get_variables(InputList[2])

            self.ui.formula_input.clear()
            self.ui.formula_input.append(f)

            self.ui.atoms_input.setText(' '.join(atoms))

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

            out_file.write('g: ' + self.ui.solution_input.toPlainText() + ';')
            out_file.close

    def slove_func(self):
        f = self.ui.formula_input.toPlainText()
        n = self.ui.split_input.value()
        atoms = get_variables(self.ui.atoms_input.text())
        self.ui.solution_input.clear()
        self.ui.solution_input.append(add_break(f, n, atoms))

    def add_symb_to_form(self, symb):
        self.ui.formula_input.textCursor().insertText(symb)

    def add_symb_to_atoms(self, symb):
        if self.ui.atoms_input.cursorPosition() == 0 or self.ui.atoms_input.text()[self.ui.atoms_input.cursorPosition() - 1] == ' ':
            self.ui.atoms_input.insert(symb)
        else:
            self.ui.atoms_input.insert(' ' + symb)