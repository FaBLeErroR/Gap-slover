from re import split
from sympy import *

from sympy.parsing.sympy_parser import (
        parse_expr,
        standard_transformations,
        implicit_application,
        implicit_multiplication,
        implicit_multiplication_application,
        function_exponentiation)

transformations=(standard_transformations +
                 (implicit_multiplication,
                  implicit_application,
                  function_exponentiation,
                  ))

funcs = ['sin', 'cos', 'tan', 'cot', 'sqrt', 'sign']

# Берет разрыв от функции по заданным параметрам
def add_breaks(func, n, atoms):
    expr = prepare_expr(func)
    components = split_expr(expr)
    out = ''
    for component in components:
        out += component_gap(component, n, atoms)
    out = out.replace('^', '**')
    # parse_expr помогает привести выражение к более удобному для
    #  дальнейшей работы виду
    expr = parse_expr(out, transformations='all')
    expr = str(expr).replace('**', '^')
    return expr

# Подготавливает слагаемое и берет его разрыв
def component_gap(component, n, atoms):
    if len(component) == 1 and (component[0] == '+' or component[0] == '-'):
        return component[0]

    tokens = split_component(component)
 
    is_atom = False

    # Разрыв слагаемого без атомов равен 0
    for token in tokens:
        for atom in atoms:
            if atom in token:
                is_atom = True
                break
    if is_atom == False:
        return '0'
    
    # Перернос всех атомов в конец выражения
    atoms_lenght = 0  
    for atom in atoms:
        if atom in tokens[0]:
            tokens.append('*')
            tokens.append(tokens[0])
            tokens[0] = '1'
            atoms_lenght += 2
            break
    
    lenght = len(tokens) - atoms_lenght
    i = 2
    atom_replaced = False

    while i <= lenght:
        for atom in atoms:
            if atom in tokens[i]:
                tokens.append(tokens[i - 1])
                tokens.append(tokens[i])
                tokens.pop(i)
                tokens.pop(i-1)
                atoms_lenght += 2
                lenght -= 2
                atom_replaced = True
                break
        if atom_replaced:
            atom_replaced = False
        else:
            i += 2

    if tokens[-atoms_lenght] == '/':
        tokens = tokens[:-atoms_lenght] + ['*', '(', '1'] + tokens[-atoms_lenght:]
        tokens.append(')')
        atoms_lenght += 3
    elif tokens[-atoms_lenght] == '*':
        tokens = tokens[:-atoms_lenght] + ['*', '('] + tokens[-atoms_lenght + 1:]
        tokens.append(')')
        atoms_lenght += 1
    return get_gap(tokens, n, atoms, atoms_lenght)

# Разделяет слагаемое на отдельные функции и переменные
def split_component(component):
    tokens = split(r'(sin|cos|tan|cot|sqrt|sign|\*|\/|\))', str(component))

    i = 0
    while i < len(tokens):
        if tokens[i] in funcs:
            while tokens[i + 1] != ')':
                tokens[i] = tokens[i] + tokens[i + 1]
                tokens.pop(i + 1)
            tokens[i] = tokens[i] + tokens[i + 1]
            tokens.pop(i + 1)
        if tokens[i] == '':
            tokens.pop(i)
        else:
            i += 1

    return tokens

# Берет разыв для подготовленного слагаемого
def get_gap(tokens, n, atoms, atoms_lenght):
    out_min = ''
    out_pl = ''
    for i in range(len(tokens) - atoms_lenght, len(tokens)):
        n = int(n)
        token = tokens[i]
        if 'sin' in token or 'cos' in token or 'tan' in token or 'cot' in token or 'sign' in token or 'sqrt' in token:
            cur_token = split(r'(\(|\))', tokens[i])
            for j in range(len(cur_token)):
                if cur_token[j] == '(':
                    func_data = split(r'(\+|-|\*|\/|\^)', cur_token[j + 1])
                    for k in range(len(func_data)):
                        if (n == 0 or n ==1) and func_data[k] in atoms:
                            func_data[k] = func_data[k] + '_p'
                        elif n == 2 and func_data[k] in atoms:
                            func_data[k] = '(' + func_data[k] + '_r+' + func_data[k] + '_m)'
                    cur_token[j + 1] = ''.join(func_data)
            token = ''.join(cur_token) 
        else:
            if n == 0 or n ==1:
                if token in atoms:
                    token = token + '_p'
                if '^' in token:
                    if token.split('^')[0] in atoms:
                        token = token.split('^')[0] + '_p^' + token.split('^')[1]
                    if token.split('^')[1] in atoms:
                        token = token.split('^')[0] + '^' + token.split('^')[1] + '_p'
            elif n == 2:
                if token in atoms:
                    token = '(' + token + '_r+' + token + '_m)'
                if '^' in token:
                    if token.split('^')[0] in atoms:
                        token = '(' + token.split('^')[0] + '_r+' + token.split('^')[0] + '_m)^' + token.split('^')[1]
                    if token.split('^')[1] in atoms:
                        token = token.split('^')[0] + '^(' + token.split('^')[1] + '_r+' + token.split('^')[1] + '_m)'
        out_pl += token

        token = tokens[i]
        if 'sin' in token or 'cos' in token or 'tan' in token or 'cot' in token or 'sign' in token or 'sqrt' in token:
            cur_token = split(r'(\(|\))', tokens[i])
            for j in range(len(cur_token)):
                if cur_token[j] == '(':
                    func_data = split(r'(\+|-|\*|\/|\^)', cur_token[j + 1])
                    for k in range(len(func_data)):
                        if (n == 0 or n ==2) and func_data[k] in atoms:
                            func_data[k] = func_data[k] + '_m'
                        elif n == 1 and func_data[k] in atoms:
                            func_data[k] = '(' + func_data[k] + '_p-' + func_data[k] + '_r)'
                    cur_token[j + 1] = ''.join(func_data)
                    
            token = ''.join(cur_token) 
        else:
            if n == 0 or n ==2:
                if token in atoms:
                    token = token + '_m'
                if '^' in token:
                    if token.split('^')[0] in atoms:
                        token = token.split('^')[0] + '_m^' + token.split('^')[1]
                    if token.split('^')[1] in atoms:
                        token = token.split('^')[0] + '^' + token.split('^')[1] + '_m'
            elif n == 1:
                if token in atoms:
                    token = '(' + token + '_p-' + token + '_r)'
                if '^' in token:
                    if token.split('^')[0] in atoms:
                        token = '(' + token.split('^')[0] + '_p-' + token.split('^')[0] + '_r)^' + token.split('^')[1]
                    if token.split('^')[1] in atoms:
                        token = token.split('^')[0] + '^(' + token.split('^')[1] + '_p-' + token.split('^')[1] + '_r)'
        out_min += token
    
    return ''.join(tokens[0:-atoms_lenght]) + '(' +  out_pl + '-' + out_min + ')'

# Проводит выражение к и удобному для взятия разрывов виду
def prepare_expr(func):
    func = func.replace('^', '**')
    expr = parse_expr(func, transformations=transformations)
    expr = expand(expr)
    expr = str(expr).replace('**', '^')
    expr = str(expr).replace(' ', '')
    return expr

# Разбиват выражение на слагаемые
def split_expr(expr):
    components = split(r'(sin|cos|tan|cot|sqrt|sign|\+|-|\))', expr)
    i = 0
    while i < len(components):
        if components[i] in funcs:
            if i > 0 and not(components[i - 1] in ['+', '-']):
                components[i] = components[i - 1] + components[i]
                components.pop(i - 1)
                i -= 1

            while components[i + 1] != ')':
                components[i] = components[i] + components[i + 1]
                components.pop(i + 1)
            components[i] = components[i] + components[i + 1]
            components.pop(i + 1)

            if i < len(components) - 1:
                if not(components[i + 1] in ['+', '-']):
                    components[i] = components[i] + components[i + 1]
                    components.pop(i + 1)
        if components[i] == '':
            components.pop(i)
        else:
            i += 1
    return components