def compute(func, *args):
    def add(x):
        return sum(list(x))

    def sub(x):
        return x[0] - add(x[1:])

    def mul(x):
        total = 1
        for i in x:
            total *= i
        return total

    def div(x):
        return x[0] / mul(x[1:])

    a = [int(i) for i in args]
    if func == '+':
        return add(a)
    elif func == '-':
        return sub(a)
    elif func == '*':
        return mul(a)
    elif func == '/':
        return div(a)