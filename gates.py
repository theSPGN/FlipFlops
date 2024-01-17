"""

It's about electronics,
not about Mr. Bill...
;)

"""

"""
callback instruction for Gate_name:
obj = Gate_name(True, True, True)
print("---")
print(obj)
print(type(obj))
print(obj())
print(type(obj()))
print(obj(True, True, False, True))

"""

# *Output is False if 'unwired', so if there is no input then expected output is False


class AndGate:
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


class OrGate(AndGate):
    def __call__(self, *args: bool) -> bool:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        if len(args):
            return any(args) if len(args) > 0 else False
        else:
            return any(self.args) if len(self.args) > 0 else False

    def __str__(self) -> str:
        return "OrGate"


class NotGate(AndGate):
    def __call__(self, *args: bool) -> tuple[bool]:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        if len(args):
            return tuple(not arg for arg in args)
        else:
            return tuple(not arg for arg in self.args)

    def __str__(self) -> str:
        return "NotGate"


class NorGate(AndGate):
    def __call__(self, *args: bool) -> bool:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        if len(args):
            return (args.count(True) == 0) if len(args) > 0 else False
        else:
            return (self.args.count(True) == 0) if len(self.args) > 0 else False

    def __str__(self) -> str:
        return "NorGate"


class NandGate(AndGate):
    def __call__(self, *args: bool) -> tuple[bool]:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        value = lambda a: True if len(a) > 0 and a.count(True) < len(a) else False

        if len(args):
            return value(args)
        else:
            return value(self.args)

    def __str__(self) -> str:
        return "NandGate"


class XorGate(AndGate):
    def __call__(self, *args: bool) -> bool:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        if len(args):
            return args.count(True) == 1
        else:
            return self.args.count(True) == 1

    def __str__(self) -> str:
        return "XorGate"


class XnorGate(AndGate):
    def __call__(self, *args: bool) -> bool:
        if not all(isinstance(arg, bool) for arg in args):
            raise ValueError("All arguments must be booleans")

        value = (
            lambda a: (a.count(True) == len(a) or a.count(False) == len(a))
            if len(a) > 0
            else False
        )

        if len(args):
            return value(args)
        else:
            return value(self.args)

    def __str__(self) -> str:
        return "XorGate"
