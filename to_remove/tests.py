from typing import overload, Any


class A:
    _var_single_underscore: int = 0
    __var_dabble_underscore: int = 6

    def __init__(self):
        self.a: int = 1

    def __custom__(self):
        pass

    @overload
    def method(self, s: str | int | list) -> str | int | list:
        print("str | int | list")
        return "str | int | list"

    @overload
    def method(self, s: str | int | float, st: dict | int) -> str | int | list:
        print("str | int | float, dict")
        return "str | int | float, dict"

    def method(self, *args) -> str | int | list:
        self.a = 0
        # print()
        for _ in args:
            print(type(_))
            print(_)

        return [*args]


class B(A):
    def __init__(self):
        super().__init__()
        self.b: int = 2


a = B()
print(a.method("str"))
print(a.method(1))
print(a.method([1, 2, 3]))
print(a.method("str", 1))
print(a.method("str", {"a": 1}))
print(a.method("str", 1593))

