
def my_var():
    var = 42
    print(var, "has a type", type(var))
    var = "42"
    print(var, "has a type", type(var))
    var = "quarante-deux"
    print(var, "has a type", type(var))
    var = 42.0
    print(var, "has a type", type(var))
    var = True
    print(var, "has a type", type(var))
    var = [42]
    print(var, "has a type", type(var))
    var = {42: 42}
    print(var, "has a type", type(var))
    var = (42,)
    print(var, "has a type", type(var))
    var = set()


if __name__ == '__main__':
    my_var()
