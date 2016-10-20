from tokken import Token


class Memory(object):
    def __init__(self):
        self.var_memory = {}
        self.func_memory = {}

    def get_var(self, key):
        try:
            return self.var_memory[key]
        except KeyError:
            # print('Undefined variable {} in get_var'.format(key))
            return None

    def set_var(self, key, value):
        if key in self.func_memory:
            del self.func_memory[key]
        self.var_memory[key] = value
        return value

    def get_func(self, key):
        try:
            return self.func_memory[key]
        except KeyError:
            # print('Undefined variable {} in get_func'.format(key))
            return None

    def set_func(self, key, procedure):
        if key in self.var_memory:
            del self.var_memory[key]
        self.func_memory[key] = procedure
        return procedure

    def __getitem__(self, key):
        res = self.get_var(key)
        if res is None:
            res = self.get_func(key)
            if res is None:
                raise KeyError('Undefined name: {}'.format(key))
        return res

    def __setitem__(self, key, value):
        if isinstance(value, Token) and value.type == 'FUNCTION':
            self.set_func(key, value)
        else:
            self.set_var(key, value)
        return value

    def freeze(self):
        frozen_memory = (self.var_memory.copy(), self.func_memory.copy())
        self.var_memory = {}
        return frozen_memory

    def melt(self, frozen_memory):
        self.var_memory = frozen_memory[0]
        self.func_memory = frozen_memory[1]

    def clean(self):
        self.var_memory = {}
        self.func_memory = {}

memory = Memory()
