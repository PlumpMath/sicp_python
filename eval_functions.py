from tokken import Token
global memory, eval_function_dict
memory = {}


# only public method of this file.
def evaluate(exp):
    """
    Evaluate expression and returns numeric value.
    :param exp: Expression, type Token
    :return: numeric value.
    """
    global memory, eval_function_dict
    if isinstance(exp, Token):
        if exp.type == 'NUMBER':
            return exp.value
        elif exp.type == 'PACKAGE':
            return evaluate(exp.value)
        elif exp.type == 'BOOLEAN':
            return exp.value
        elif exp.type == 'NAME':
            return memory[exp.value]
    elif isinstance(exp, list):
        if exp[0].type in eval_function_dict:
            return eval_function_dict[exp[0].type](exp)
        elif isinstance(exp[0], Token):
            return evaluate(exp[0])
    raise TypeError("Unexpected input type {}".format(exp))


def eval_plus(exp):
    res = evaluate(exp[1])
    for item in exp[2:]:
        res += evaluate(item)
    return res


def eval_minus(exp):
    res = evaluate(exp[1])
    for item in exp[2:]:
        res -= evaluate(item)
    return res


def eval_divide(exp):
    res = evaluate(exp[1])
    for item in exp[2:]:
        res /= evaluate(item)
    return res


def eval_times(exp):
    res = evaluate(exp[1])
    for item in exp[2:]:
        res *= evaluate(item)
    return res


def eval_if(exp):
    if evaluate(exp[1]):
        return evaluate(exp[2])
    else:
        return evaluate(exp[3])


def eval_bigger_than(exp):
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) > evaluate(exp[2]):
        token.value = True
    return token


def eval_smaller_than(exp):
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) < evaluate(exp[2]):
        token.value = True
    return token


def eval_equal_to(exp):
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) == evaluate(exp[2]):
        token.value = True
    return token


def eval_define(exp):
    global memory
    memory[exp[1].value] = evaluate(exp[2])
    return memory[exp[1].value]


def eval_and(exp):
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) and evaluate(exp[2]):
        token.value = True
    return token


def eval_cond(exp):
    for item in exp[1:]:
        if evaluate(item):
            return evaluate(item.value[1])


def eval_else(exp):
    if exp[0].type == 'ELSE':
        return evaluate(exp[1])


# for shorter lines of code.
eval_function_dict = {'PLUS': eval_plus, 'MINUS': eval_minus, 'DIVIDE': eval_divide, 'TIMES': eval_times,
                      'IF': eval_if, 'BIGGERTHAN': eval_bigger_than, 'SMALLERTHAN': eval_smaller_than,
                      'EQUALTO': eval_equal_to, 'DEFINE': eval_define, 'AND': eval_and, 'COND': eval_cond}
