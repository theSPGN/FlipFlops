from gates import NandGate as nand


# All the flip flops are made with nands
class RS:
    def __init__(
        self, r: bool = False, s: bool = False, clk: bool = False, type: str = "async"
    ):
        if (
            not isinstance(r, bool)
            or not isinstance(s, bool)
            or not isinstance(clk, bool)
        ):
            raise ValueError("All arguments must be booleans")

        if type is not "async" and type is not "sync":
            raise ValueError('Value of type has to be "sync" or "async"')

        self.r = r
        self.s = s
        self.q = None
        self.clk = clk
        self.type = type

    def __call__(self, r: bool = None, s: bool = None) -> bool:
        if r is not None:
            self.r = r
        if s is not None:
            self.s = s

        return self.q

    def __str__(self) -> str:
        return "RSAsync"


k = RS(True, False)
print(k())
