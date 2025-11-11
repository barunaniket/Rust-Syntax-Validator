import ply.yacc as yacc
from lexer import tokens

# Root rule
def p_program(p):
    'program : statements'
    p[0] = ('program', p[1])

# A sequence of statements
def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]

# Statement types
def p_statement(p):
    '''statement : variable_declaration SEMICOLON
                 | function_definition
                 | if_statement
                 | while_statement
                 | for_statement'''
    p[0] = p[1]

# Variable declaration: ID = expr or ID : expr
def p_variable_declaration_assign(p):
    'variable_declaration : ID EQUALS expression'
    p[0] = ('assign', p[1], p[3])

def p_variable_declaration_typed(p):
    'variable_declaration : ID COLON expression'
    p[0] = ('typed', p[1], p[3])

# Function definition
def p_function_definition(p):
    'function_definition : FUN ID LPAREN RPAREN LBRACE statements RBRACE'
    p[0] = ('fun', p[2], p[6])

# If and If-Else statements
def p_if_statement(p):
    '''if_statement : IF expression LBRACE statements RBRACE
                    | IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    if len(p) == 6:
        p[0] = ('if', p[2], p[4])
    else:
        p[0] = ('if_else', p[2], p[4], p[8])

# While loop
def p_while_statement(p):
    'while_statement : WHILE expression LBRACE statements RBRACE'
    p[0] = ('while', p[2], p[4])

# For loop
def p_for_statement(p):
    'for_statement : FOR ID IN expression DOTDOT expression LBRACE statements RBRACE'
    p[0] = ('for_range', p[2], p[4], p[6], p[8])

# Expression
def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('num', p[1])

# Error handling
def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at '{p.value}'")
    else:
        raise SyntaxError("Syntax error at EOF")

parser = yacc.yacc()
