from collections import defaultdict
from tokken import Token


class Log(object):
    """
    level 0 : None
    level 1 : FATAL
    level 2 : ERROR
    level 3 : Debug
    level 4 : Info
    level 5 : all
    """
    line_no = 0
    indent = 0
    indent_limit = 5

    def __init__(self):
        self.level = 5
        self.enable = defaultdict(lambda: True)

    def set(self, level):
        self.level = level

    def i(self, data):
        if self.level >= 4:
            self.print_log(data)

    def d(self, data):
        if self.level >= 3:
            self.print_log(data)

    def e(self, data):
        if self.level >= 2:
            self.print_log(data)

    def f(self, data):
        if self.level >= 1:
            self.print_log(data)
            
    def print_log(self, data):
        if self.indent >= self.indent_limit:
            return
        if isinstance(data, Token):
            if self.enable[data.type]:
                print("{:<3}{}{}".format(self.line_no, " "*self.indent, str(data)))
                self.line_no += 1
        elif isinstance(data, list):
            print("{:<3}{}{}".format(self.line_no, " "*self.indent, str(data)[1:-1]))
            self.line_no += 1
        else:
            print("{:<3}{}{}".format(self.line_no, " "*self.indent, "{}".format(data)))
            self.line_no += 1

    def do_indent(self, data):
        if isinstance(data, Token):
            self.indent += 1

    def do_dedent(self, data):
        if isinstance(data, Token):
            self.indent -= 1


log = Log()
