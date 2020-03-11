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


class integerDivide(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '( ' + str(self.left) + ' // ' + str(self.right) + ' )'

    def eval(self, env):
        evalExpr = ''.join([ch if ch not in env else str(env[ch]) for ch in str(self)])
        return eval(evalExpr)


def main():
    var1, var2, var3 = Var('x'), Var('y'), Var('z')
    const1, const2 = Const(3), Const(4)
    e1 = Plus(var1, var2)
    e2 = Times(const1, e1)
    e3 = Minus(var2, var3)
    e4 = Times(const2, e3)
    e5 = Divide(e2, e4)
    e6 = integerDivide(e2, e4)
    valuesForVars = {'x': 7, 'y': 5, 'z': 2}
    print(e5.eval(valuesForVars))
    print(e6.eval(valuesForVars))


if __name__ == '__main__':
    main()
