# The code is similar to a youtube computerphile video
# by Professor Thorsten Altenkirch


class Expr(object):
    pass


class Const(Expr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Plus(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '( ' + str(self.left) + ' + ' + str(self.right) + ' )'

    def eval(self, env):
        evalExpr = ''.join([ch if ch not in env else str(env[ch]) for ch in str(self)])
        return eval(evalExpr)


class Minus(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '( ' + str(self.left) + ' - ' + str(self.right) + ' )'

    def eval(self, env):
        evalExpr = ''.join([ch if ch not in env else str(env[ch]) for ch in str(self)])
        return eval(evalExpr)


class Times(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '( ' + str(self.left) + ' * ' + str(self.right) + ' )'

    def eval(self, env):
        evalExpr = ''.join([ch if ch not in env else str(env[ch]) for ch in str(self)])
        return eval(evalExpr)


class Divide(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '( ' + str(self.left) + ' / ' + str(self.right) + ' )'

    def eval(self, env):
        evalExpr = ''.join([ch if ch not in env else str(env[ch]) for ch in str(self)])
        return eval(evalExpr)


def main():
    e1 = Times(Const(3), Var('x'))
    e2 = Plus(e1, Var('y'))
    print(e2.eval({'x': 2, 'y': 3}))


if __name__ == '__main__':
    main()
