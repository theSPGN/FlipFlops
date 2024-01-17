class AndGate:
    def __init__(self, *args: tuple[bool]) -> None:
        self.args = args

    def __call__(self, *args) -> bool:
        return all(args) if len(args) > 0 else False

    def __str__(self) -> str:
        return "AndGate"


# callback:
# obj = AndGate()
# print(obj, type(obj))
# print(obj(True, True, False, True))
