from re import split
import sympy
from sympy import *


# r_a, a_m, a_p, r_b, b_m, b_p = symbols('r_a a_m a_p r_b b_m b_p')

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


def add_break(f, n, atoms):
    # print(f)
    f = f.replace('^', '**')
    expr = parse_expr(f, transformations=transformations)
    expr = expand(expr)
    expr = str(expr).replace(' ', '')
    # expr = expr.replace('**', '^')
    # print(expr)

    components = split(r'(sin|cos|tan|cot|sqrt|sign|\+|-|\))', expr)
    # print(components)
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
    # print(components)
    out = ''
    for component in components:
        out += find_atoms(component, n, atoms)
    # print(out)
    # out.replace('^', '**')
    expr = parse_expr(out, transformations='all')
    print(expr)
    # expr = simplify(expr)
    expr = str(expr).replace('**', '^')
    return str(expr) 
    # return out
    # return change_comp(components, n, atoms)

def to_list(token):
    return [i for i in token]

def find_atoms(tokens, n, atoms):

    if len(tokens) == 1 and (tokens[0] == '+' or tokens[0] == '-'):
        return tokens[0]

    tokens = split(r'(sin|cos|tan|cot|sqrt|sign|\*|\/|\))', str(tokens))
    # print(tokens)

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

 
    is_atom = False

    for token in tokens:
        for atom in atoms:
            if atom in token:
                is_atom = True
                break
    if is_atom == False:
        return '0'
    
    # tokens.append('')
    atoms_lenght = 0  
    for atom in atoms:
        if atom in tokens[0]:
            tokens.append('*')
            tokens.append(tokens[0])
            tokens[0] = '1'
            atoms_lenght += 2
            break

    
    lenght = len(tokens)
    i = 2

    while i < lenght:
        for atom in atoms:
            if atom in tokens[i]:
                # print(str(i) + ' ' + tokens[i] + ' ' + atom)
                tokens.append(tokens[i - 1])
                tokens.append(tokens[i])
                tokens.pop(i)
                tokens.pop(i-1)
                atoms_lenght += 2
                lenght -= 2
                break
        i += 2

    # print(tokens)
    if tokens[-atoms_lenght] == '/':
        tokens = tokens[:-atoms_lenght] + ['*', '(', '1'] + tokens[-atoms_lenght:]
        tokens.append(')')
        atoms_lenght += 3
    elif tokens[-atoms_lenght] == '*':
        tokens = tokens[:-atoms_lenght] + ['*', '('] + tokens[-atoms_lenght + 1:]
        tokens.append(')')
        atoms_lenght += 1
    

    # print(-atoms_lenght)
    # print(tokens)

    out_min = ''
    out_pl = ''
    for i in range(len(tokens) - atoms_lenght, len(tokens)):
        n = int(n)
        token = tokens[i]
        print('input: ' + token)
        if 'sin' in token or 'cos' in token or 'tan' in token or 'cot' in token or 'sign' in token or 'sqrt' in token:
            cur_token = split(r'(\(|\))', tokens[i])
            # print(cur_token)
            for j in range(len(cur_token)):
                if cur_token[j] == '(':
                    for atom in atoms:
                        if n == 0 or n ==1:
                            cur_token[j + 1] = cur_token[j + 1].replace(atom, atom + '_p')
                        elif n == 2:
                            cur_token[j + 1] = cur_token[j + 1].replace(atom, '(' + atom + '_r+' + atom + '_m)') 
            token = ''.join(cur_token) 
            # print(token)  
        else:
            for atom in atoms:
                if n == 0 or n ==1:
                    token = token.replace(atom, atom + '_p')
                elif n == 2:
                    token = token.replace(atom, '(' + atom + '_r+' + atom + '_m)')
        out_pl += token

        token = tokens[i]
        # print(token)
        if 'sin' in token or 'cos' in token or 'tan' in token or 'cot' in token or 'sign' in token or 'sqrt' in token:
            cur_token = split(r'(\(|\))', tokens[i])
            # print(cur_token)
            for j in range(len(cur_token)):
                if cur_token[j] == '(':
                    for atom in atoms:
                        if n == 0 or n ==2:
                            cur_token[j + 1] = cur_token[j + 1].replace(atom, atom + '_m')
                        elif n == 1:
                            cur_token[j + 1] = cur_token[j + 1].replace(atom, '(' + atom + '_p-' + atom + '_r)')   
            token = ''.join(cur_token) 
            # print(token) 
        else:
            for atom in atoms:
                if n == 0 or n == 2:
                    token = token.replace(atom, atom + '_m')
                elif n ==1:
                    token = token.replace(atom, '(' + atom + '_p-' + atom + '_r)')
        out_min += token
    
    print('outstr: ' + out_pl + ' ' + out_min)
    return ''.join(tokens[0:-atoms_lenght]) + '(' +  out_pl + '-' + out_min + ')'





    # print(tokens)
    # print(str(atoms_lenght) + ' ' + tokens[-atoms_lenght] + '' + str(lenght) + tokens[lenght])

    # return '0'
        

    # tokens.append('')     
    # for i in range(len(tokens)):
    #     for j in range(i + 1, len(tokens)):
    #         print(str(i) + ' ' + str(j))
    #         if (tokens[i] in atoms) and (tokens[j] in atoms):
    #             if tokens[j - 1] == '*':
    #                 if i == j - 2:
    #                     tokens[j-1] = mul_change(tokens[i], tokens[j], n)
    #                     tokens[i], tokens[j] = '', ''
    #                 else:
    #                     a, b = tokens[i], tokens[j]
    #                     tokens = tokens[0:i] + tokens[i] + '*' + tokens[j] + tokens[i + 1: j -1] + tokens[j + 1: len(tokens)]
    #                     tokens[i + 1] = mul_change(a, b, n)
    #                     tokens[i], tokens[i + 2] = '', ''
    #                 # return add_breaking(tokens, n, atoms)
    #             elif tokens[j - 1] == '/':
    #                 if i == j - 2:
    #                     tokens[j - 1] = div_change(tokens[i], tokens[j], n)
    #                     tokens[i], tokens[j] = '', ''
    #                 else:
    #                     a, b = tokens[i], tokens[j]
    #                     tokens = [''.join(tokens[0:i]), tokens[i], '/', tokens[j], ''.join(tokens[i + 1: j - 1]), ''.join(tokens[j + 1: len(tokens)])]
    #                     print('tokens(div): ' + str(tokens))
    #                     tokens[i + 2] = div_change(a, b, n)
    #                     tokens[i + 1], tokens[i + 3] = '', ''
    #                     print('tokens(div2): ' + str(tokens))
    #                 # return add_breaking(tokens, n, atoms)
    #             elif tokens[i - 1] == '/':
    #                 a, b = tokens[j], tokens[i]
    #                 tokens = tokens[0:i] + tokens[j] + '/' + tokens[i] + tokens[i + 1: j -1] + tokens[j + 1: len(tokens)]
    #                 tokens[j + 1] = div_change(a, b, n)
    #                 tokens[j], tokens[j + 2] = '', ''
    #                 # return add_breaking(tokens, n, atoms)
    #             elif 'sin' in tokens[j]:
    #                 tokens[j] = sin_change(tokens[j])
    #             return add_break(''.join(tokens), n, atoms)
    return ''.join(tokens)

def single_change(a, n):
    if int(n) == 0:
        return '(' + str(a) + '_p-' + str(a) + '_m)'
    elif int(n) == 1 or int(n) == 2:
        return str(a) + '_r'

def mul_change(a, b, n):
    print('n: ' + str(n))
    output = ''
    if int(n) == 0:
        output = '(' + str(a) + '_p-' + str(a) + '_m)-(' + str(b) + '_p-' + str(b) + '_m)'
    elif int(n) == 1:
        # output = '(' + str(a) + '_p*r_' + str(b) + '+' + str(b) + '_p*r_' + str(a) + '-r_' + str(a) + '*r_' + str(b) + ')'
        output = '(' + str(a) + '_p*' + str(b) + '_r+' + str(b) + '_p*' + str(a) + '_r-' + str(a) + '_r*' + str(b) + '_r)'
    elif int(n) == 2:
        # output = '(' + str(a) + '_m*r_' + str(b) + '+' + str(b) + '_m*r_' + str(a) + '+r_' + str(a) + '*r_' + str(b) + ')'
        output = '(' + str(a) + '_m*' + str(b) + '_r+' + str(b) + '_m*' + str(a) + '_r-' + str(a) + '_r*' + str(b) + '_r)'
    return output

def div_change(a, b, n):
    print('n: ' + str(n))
    if int(n) == 0:
        return '(' + str(a) + '_p-' + str(a) + '_m)/(' + str(b) + '_p-' + str(b) + '_m)'
    elif int(n) == 1:
        # return '(' + str(a) + '_p/' + str(b) + '_p-(' + str(a) + '_p-r_' + str(a) + ')/(' + str(b) + '_p-r_' + str(b) + '))'
        return '(' + str(a) + '_p/' + str(b) + '_p-(' + str(a) + '_p-' + str(a) + '_r)/(' + str(b) + '_p-' + str(b) + '_r))'
    elif int(n) == 2:
        # return '((r_' + str(a) + '+' +str(a) + '_m)/(r_' + str(b) + '+' + str(b) + '_m)-' + str(a) + '_m/' + str(b) + '_m)'
        return '((' + str(a) + '_r+' +str(a) + '_m)/(' + str(b) + '_r+' + str(b) + '_m)-' + str(a) + '_m/' + str(b) + '_m)'
    
def sin_change(a, n):
    return

def sum_change(a, b, n):
    if int(n) == 0:
        return '(' + str(a) + '_p-' + str(a) + '_m+' + str(b) + '_p-' + str(b) + '_m)'
    elif int(n) == 1:
        return '(r(' + str(a) + ')+r(' + str(b) + '))'
    elif int(n) == 2:
        return '(r(' + str(a) + ')+r(' + str(b) + '))'

def dif_change(a, b, n):
    if int(n) == 0:
        return '(' + str(a) + '_p-' + str(a) + '_m-' + str(b) + '_p+' + str(b) + '_m)'
    elif int(n) == 1:
        return '(r(' + str(a) + ')-r(' + str(b) + '))'
    elif int(n) == 2:
        return '(r(' + str(a) + ')-r(' + str(b) + '))'
