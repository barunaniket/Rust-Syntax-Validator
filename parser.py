import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements(p):
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('expr', p[1])

def p_variable_declaration(p):
    if p[2] == '=':
        p[0] = ('assign', p[1], p[3])
    else:
        p[0] = ('typed', p[1], p[3])

def p_function_definition(p):
    'function_definition : FUN ID LPAREN RPAREN LBRACE statements RBRACE'
    p[0] = ('fun', p[2], p[6])

def p_if_statement(p):
    if len(p) == 6:
        p[0] = ('if', p[2], p[4])
    else:
        p[0] = ('if_else', p[2], p[4], p[8])

def p_while_statement(p):
    'while_statement : WHILE expression LBRACE statements RBRACE'
    p[0] = ('while', p[2], p[4])

def p_for_statement(p):
    'for_statement : FOR ID IN expression DOTDOT expression LBRACE statements RBRACE'
    p[0] = ('for_range', p[2], p[4], p[6], p[8])

def p_expression(p):
    p[0] = p[1]

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at '{p.value}'")
    else:
        raise SyntaxError("Syntax error at EOF")

parser = yacc.yacc()
