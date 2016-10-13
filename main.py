"""
main           imports    eval_functions.(for evaluation)
                          tokken.        (for parsing)
                          tests.         (for testing)

eval_functions imports    tokken.        (for evaluation)

tokken         imports    lexer.         (for parsing)

tests          imports    pretty much same as main
                          except itself(obviously)

lexer          imports    ply.lex        (for parsing)
"""
from eval_functions import evaluate
from tokken import string_to_tokens
from tests import *


def run():
    tokens = string_to_tokens()
    result = evaluate(tokens)
    print(result)

if __name__ == "__main__":
    exercise1_1()
    exercise1_2()
    exercise1_3()
