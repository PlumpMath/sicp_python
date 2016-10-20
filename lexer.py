def get_lexer():
    """
    Lexer builder using ply.lex.
    Lex is just used as a parser so do not pay too much attention
    on this file.
    DO NOT run PEP008 checker nor python optimizer on this file.
    :return: lexer.
    """
    import ply.lex as lex

    # List of token names.
    tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES',
              'DIVIDE', 'LPAREN', 'RPAREN', 'NAME',
              'DEFINE', 'PACKAGE', 'BIGGERTHAN',
              'SMALLERTHAN', 'EQUALTO', 'IF', 'AND',
              'COND', 'ELSE', 'MODULUS', 'OR')

    # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_BIGGERTHAN = r'>'
    t_SMALLERTHAN = r'<'
    t_EQUALTO = r'='
    t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # A regular expression rule with some action code
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # REGEX for reserved word DEFINE.
    # This is defined as function to
    # be prioritized than t_NAME regex.
    def t_DEFINE(t):
        r'DEFINE|define'
        return t

    def t_IF(t):
        r'IF|if'
        return t

    def t_AND(t):
        r'AND|and'
        return t

    def t_COND(t):
        r'COND|cond'
        return t

    def t_ELSE(t):
        r'ELSE|else'
        return t

    def t_OR(t):
        r'OR|or'
        return t

    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    lexer = lex.lex()
    return lexer