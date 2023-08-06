def gInspect(*data):
    for d in data:
        print(f"type of {d} is {type(d)}")
        print(f"Value of {d} is {d}")


def get_variable_name(x) -> str:
    for k, v in locals().items():
        if v is x:
            return k


def print_var(x) -> None:
    print(get_variable_name(x), '=', x)


if __name__ == '__main__':
    a = 1
    b = 1
    print_var(a)
    print_var(b)
