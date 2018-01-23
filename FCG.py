class InvalidSymbol(Exception):
    pass

class InvalidName(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{} is not a valid name".format(self.name)

class InvalidSymbol(InvalidName):
    def __init__(self, name):
        super(InvalidName, self).__init__(name)

    def __str__(self):
        return "{} is not a valid symbol".format(self.name)

class InvalidToken(InvalidName):
    def __init__(self, name):
        super(InvalidName, self).__init__(name)

    def __str__(self):
        return "{} is not a valid token".format(self.name)

class AST:
    def __init__(self, v, childs=[]):
        self.v = v
        self.childs = childs
        self._calculate_height()

    def _calculate_height(self):
        if childs:
            self.height = max(map(lambda n: n.height, self.childs)) + 1
        else:
            self.height = 1

class Grammar:
    def __init__(self, tokens, start_symbol = 'START'):
        self.S = start_symbol
        self.tokens = tokens
        self.rules = {}

    def add_rule(self, lhs, *rhs):
        if lhs in self.rules:
            self.rules[lhs].add(list(rhs))
        else:
            self.rules[lhs] = [list(rhs)]

    def __str__(self):
        res = ""
        for k,v in self.rules.items():
            res += "{} ::= {}\n".format(k, " ".join(v))

    def all_grammars(S = AST('START'), h=None):
        if h is not None:
            if S not in self.rules:
                raise InvalidToken(S)

