from functools import singledispatch


@singledispatch
def func( num: int ):
    return "int"


@func.register
def func_overload( num: str ):
    return "str"


print(func(1))
print(func("s"))
