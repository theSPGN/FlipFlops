import matplotlib

print(matplotlib.__file__)


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


# callback instruction:

# obj = AndGate(True, True, True)
# print("---")
# print(obj)
# print(type(obj))
# print(obj())
# print(type(obj()))
# print(obj(True, True, False, True))
