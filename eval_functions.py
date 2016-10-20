from tokken import Token
from memory import memory
from log import log
from functools import reduce


def eval_log(exp):
    log.i(exp)


# only public method of this file.
def evaluate(exp):
    """
    Evaluate expression and returns numeric value.
    :param exp: Expression, type Token
    :return: numeric value or function.
    """
    global memory, eval_function_dict, log

    eval_log(exp)
    # log.indent += 1
    log.do_indent(exp)
    result = None
    if isinstance(exp, Token):
        if exp.type == 'PACKAGE':
            res = evaluate(exp.value)
            if isinstance(res, list) and len(res) == 1:
                result = evaluate(res[0])
            result = evaluate(res)
        elif exp.type == 'NUMBER':
            result = exp.value
        elif exp.type == 'BOOLEAN':
            result = exp.value
        elif exp.type == 'NAME':
            value = memory[exp.value]
            log.i("{} is {}".format(exp.value, value))
            result = value
        elif exp.type == 'ELSE':
            result = Token(type='BOOLEAN', value=True)
    elif isinstance(exp, list):
        if isinstance(exp[0], Token) and exp[0].type in eval_function_dict:
            result = eval_function_dict[exp[0].type](exp)
        elif len(exp) == 1:
            result = evaluate(exp[0])
        elif isinstance(exp[0], Token):
            first = evaluate(exp[0])
            rest = exp[1:]
            result = evaluate([first] + rest)
        elif reduce(lambda x, y:  x or isinstance(y, Token), exp):
            result = list(map(lambda x: evaluate(x) if isinstance(x, Token) else x, exp))


    if result is None:
        result = exp

    log.do_dedent(exp)
    return result


class EvalException(Exception):
    def __init__(self, message):
        self.message = message


def req_params(exp, number):
    if len(exp) != number:
        raise EvalException("Wrong number of arguments {}".format(number))


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
    req_params(exp, 4)
    if evaluate(exp[1]):
        return evaluate(exp[2])
    else:
        return evaluate(exp[3])


def eval_bigger_than(exp):
    req_params(exp, 3)
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) > evaluate(exp[2]):
        token.value = True
    return token


def eval_smaller_than(exp):
    req_params(exp, 3)
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) < evaluate(exp[2]):
        token.value = True
    return token


def eval_equal_to(exp):
    req_params(exp, 3)
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) == evaluate(exp[2]):
        token.value = True
    return token


def eval_define(exp):
    global memory
    # If defining variable
    if len(exp) == 3:
        key = exp[1].value
        value = evaluate(exp[2])
        memory[key] = value
        return value
    # Else, it's defining a function
    # First is a name of a function
    # Last is the procedure it should take
    # everything in between are parameters
    else:
        key = exp[1].value
        procedure = exp[-1]
        parameters = exp[2:-1]
        value = Token(type='FUNCTION', value=(parameters, procedure), key=key)
        memory[key] = value
        return value


def eval_function(exp):
    global memory
    params = exp[0].value[0]
    param_kv = {}
    for i in range(len(params)):
        param_kv[params[i].value] = evaluate(exp[1 + i])
    function = exp[0].value[1]
    frozen_memory = memory.freeze()
    for key, value in param_kv.items():
        memory[key] = value
    result = evaluate(function)
    memory.melt(frozen_memory)
    return result


def eval_and(exp):
    req_params(exp, 3)
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) and evaluate(exp[2]):
        token.value = True
    return token


def eval_or(exp):
    req_params(exp, 3)
    token = Token(type='BOOLEAN', value=False)
    if evaluate(exp[1]) or evaluate(exp[2]):
        token.value = True
    return token


def eval_cond(exp):
    for item in exp[1:]:
        condition = evaluate(item.value[0])
        if condition:
            return evaluate(item.value[1])


def eval_modulus(exp):
    req_params(exp, 3)
    res = evaluate(exp[1]) % evaluate(exp[2])
    return res


# for shorter lines of code.
eval_function_dict = {'PLUS': eval_plus, 'MINUS': eval_minus, 'DIVIDE': eval_divide, 'TIMES': eval_times,
                      'IF': eval_if, 'BIGGERTHAN': eval_bigger_than, 'SMALLERTHAN': eval_smaller_than,
                      'EQUALTO': eval_equal_to, 'DEFINE': eval_define, 'AND': eval_and, 'COND': eval_cond,
                      'FUNCTION': eval_function, 'MODULUS': eval_modulus, 'OR': eval_or}
