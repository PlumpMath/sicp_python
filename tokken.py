from lexer import get_lexer
lexer = get_lexer()


class Token(object):
    '''
    Token class to replace lexerToken. Lexer is just a parser
    and this is real token. The file is named tokken.py because
    there is native library named token.
    '''
    def __init__(self, LexToken=None, type=None, value=None):
        if LexToken is not None:
            self.type = LexToken.type
            self.value = LexToken.value
        elif type is not None:
            self.type = type
        else:
            raise BaseException("Tokens init exception")
        if value is not None:
            self.value = value

    def __repr__(self):
        return "Token: {} '{}'".format(self.type, self.value)

    def __bool__(self):
        if self.value == True or self.value == False:
            return self.value
        else:
            raise TypeError("Non-boolean type {}".format(self))


def string_to_tokens(data=None):
    """
    Gets user input or string input and returns tokens.
    :param data: optional. If not provided, ask user for input.
    :return: List of packed Token instances.
    """
    tokens = []
    while True:
        if data is None:
            data = input(">")
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                my_token = lexer_token_to_token(tokens)
                return pack(my_token)
            tokens.append(tok)


def lexer_token_to_token(tokens):
    """
    Changes lexerToken to Tokens.
    :param tokens: list of lexerToken instances
    :return: list of Token instances.
    """
    result = []
    for token in tokens:
        result.append(Token(token))
    return result


def pack(tokens):
    """
    Packs parenthesized tokens into packages.
    ex) input : + 1 (1)
        output: + 1 package(1)
    :param tokens: list of Token instances.
    :return: list of Token instances.
    """
    lparen_index = None
    length = len(tokens)
    lcursor = length
    # search for last lparen
    for token in reversed(tokens):
        lcursor -= 1
        if token.type == 'LPAREN':
            lparen_index = lcursor
            break

    if lparen_index is None:
        return tokens

    # search for matching rparen
    rparen_index = lcursor + 1
    for token in tokens[rparen_index:]:
        if token.type == 'RPAREN':
            break
        rparen_index += 1

    package = Token(type='PACKAGE', value=tokens[lparen_index + 1:rparen_index])
    if len(package.value) == 1:
        package = package.value[0]
    for i in range(rparen_index + 1 - lparen_index):
        tokens.pop(lparen_index)
    tokens.insert(lparen_index, package)
    return pack(tokens)