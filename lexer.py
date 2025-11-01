import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'EQUALS', 'COLON', 'SEMICOLON', 'DOTDOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'IF', 'ELSE', 'WHILE', 'FOR', 'IN', 'FUN'
)

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'fun': 'FUN'
}

t_EQUALS = r'='
t_COLON = r':'
t_SEMICOLON = r';'
t_DOTDOT = r'\.\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_comment(t):
    r'//[^\n]*'
    pass

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
