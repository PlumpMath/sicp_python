from eval_functions import evaluate
from tokken import string_to_tokens
'''
From now on builtin functions will be defined here and will be dynamically loaded at the runtime.
'''


# Only public method of this file.
def load_builtins():
    add_remainder()
    add_gcd()
    add_make_rat()
    add_abs()


def add_remainder():
    exp = string_to_tokens('''
    (define remainder a b
        (if (or (> a b) (= a b))
        (remainder (- a b) b)
        a
        )
    )
    ''')
    evaluate(exp)
    print("remainder added")


def add_gcd():
    exp = string_to_tokens('''
    (define gcd a b
        (if (= b 0)
        a
        (gcd b (remainder a b))
        )
    )
    ''')
    evaluate(exp)
    print("gcd added")


def add_abs():
    exp = string_to_tokens('''
    (define abs a
        {if (> a 0)
            a
            (-a)
        }
    )
    ''')
    evaluate(exp)


def add_make_rat():
    exp = string_to_tokens('''
    (define make_rat n d
        { if (> (* n d) 0
            {
                ((/ n (gcd n d)) (/ d (gcd n d)))
            }
            {
                ((/ n (gcd n d)) (/ d (gcd n d)))
            }
        }
    )
    ''')
    evaluate(exp)
    print("make_rat added")