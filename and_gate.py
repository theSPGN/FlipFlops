class AndGate:
    def __init__(self, input_1: bool = False, input_2: bool = False) -> None:
        self.input_1 = input_1
        self.input_2 = input_2

    def __new__(cls, input_1: bool = False, input_2: bool = False) -> bool:
        return bool(input_1 * input_2)


# callback:
# obj = AndGate(True, True)
# print(obj, type(obj))
