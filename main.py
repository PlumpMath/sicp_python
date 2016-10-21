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
from tests import *
from eval_functions import EvalException, evaluate
from builtin_functions import load_builtins
from log import log
from memory import memory
import sys
import traceback


def run():
    global log
    while True:
        log.enable["PACKAGE"] = False
        log.enable["NAME"] = False
        log.enable["NUMBER"] = False
        try:
            tokens = string_to_tokens()
            for line in tokens:
                log.line_no = 0
                result = evaluate(line)
                print("--")
            print("output: {}".format(result))
        except KeyboardInterrupt:
            print('Keyboard Interrupt detected. Bye!')
            exit()
        except EvalException as e:
            log.e("ERROR! {}".format(e.message))
            continue
        except AttributeError as e:
            log.e("ERROR! {}".format(e))
            continue
        except KeyError as e:
            print(e)
            continue
        except IndexError as e:
            print(e)
            traceback.print_exc()
            continue
        except Exception as e:
            # traceback.print_exc()
            print(e)
            continue

if __name__ == "__main__":
    log.set(0)
    exercise1_1()
    exercise1_2()
    exercise1_3()
    exercise1_4()
    memory.clean()
    load_builtins()
    log.set(10)
    run()
