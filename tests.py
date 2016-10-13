from eval_functions import evaluate
from tokken import string_to_tokens


def test(data):
    tokens = string_to_tokens(data)
    result = evaluate(tokens)
    return result


def asserteq(statement, value):
    """
    Assert Equal. Evaluates the statement and raises error if
    the evaluation result is NOT EQUAL TO value.
    :param statement: string input that machine can accept
    :param value: Nothing if success else Error.
    """
    try:
        assert test(statement) == value
    except AssertionError:
        try:
            # TODO fix this.
            assert test(statement).value == value
        except:
            raise AssertionError("{}, {}".format(test(statement), value))


def exercise1_1():
    """
    https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%_sec_1.1.1
    """
    asserteq("10", 10)
    asserteq("(+ 5 3 4)", 12)
    asserteq("(- 9 1)", 8)
    asserteq("(/ 6 2)", 3)
    asserteq("(+ (* 2 4) (- 4 6))", 6)
    asserteq("(define a 3)", 3)
    asserteq("(define b (+ a 1))", 4)
    asserteq("(+ a b (* a b))", 19)
    asserteq("(= a b)", False)
    asserteq("(if (and (> b a) (< b (* a b))) b a)", 4)
    asserteq("(cond ((= a 4) 6) ((= b 4) (+ 6 7 a)) (else 25))", 16)
    asserteq("(+ 2 (if (> b a) b a))", 6)
    asserteq("(* (cond ((> a b) a) ((< a b) b) (else -1)) (+ a 1))", 16)


def exercise1_2():
    pass


def exercise1_3():
    asserteq("(define a 1)", 1)
    asserteq("(define b 2)", 2)
    asserteq("(define c 3)", 3)
    asserteq('''
             (cond
                  (and (> a b) (> b c)
                  (+ (* a a) (* b b)))
                  (and (> a b) (> c b)
                  (+ (* a a) (* c c)))
                  (else
                  (+ (* b b) (* c c)))
              )
             ''', 13)


