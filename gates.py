"""

It's about electronics,
not about Mr. Bill...
;)

"""


class AndGate:
    """
    callback instruction for AndGate:
    obj = AndGate(True, True, True)
    print("---")
    print(obj)
    print(type(obj))
    print(obj())
    print(type(obj()))
    print(obj(True, True, False, True))
    """

    def __init__(self, *args: bool) -> None:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        self.args = args

    def __call__(self, *args: bool) -> bool:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        if len(args):
            return all(args) if len(args) > 0 else False
        else:
            return all(self.args) if len(self.args) > 0 else False

    def __str__(self) -> str:
        return "AndGate"


class OrGate:
    """
    callback instruction for OrGate:
    obj = OrGate(False, False, False)
    print("---")
    print(obj)
    print(type(obj))
    print(obj())
    print(type(obj()))
    print(obj(True, True, False, True))
    """

    def __init__(self, *args: bool) -> None:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        self.args = args

    def __call__(self, *args: bool) -> bool:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        if len(args):
            return any(args) if len(args) > 0 else False
        else:
            return any(self.args) if len(self.args) > 0 else False

    def __str__(self) -> str:
        return "OrGate"


class NotGate:
    """
    callback instruction for NotGate:
    obj = NotGate(False, False, False)
    print("---")
    print(obj)
    print(type(obj))
    print(obj())
    print(type(obj()))
    print(obj(True, True, False, True))
    """

    def __init__(self, *args: bool) -> None:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        self.args = args

    def __call__(self, *args: bool) -> tuple[bool]:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        if len(args):
            return tuple(not arg for arg in args)
        else:
            return tuple(not arg for arg in self.args)

    def __str__(self) -> str:
        return "NotGate"
