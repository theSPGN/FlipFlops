from gates import NandGate as Gnand
from gates import NotGate as Gnot


class RS:
    def __init__(
        self,
        r: bool = False,
        s: bool = False,
        clk: bool = False,
        default_q: bool = False,
        rs_type: str = "async",
    ):
        if (
            not isinstance(r, bool)
            or not isinstance(s, bool)
            or not isinstance(clk, bool)
            or not isinstance(default_q, bool)
        ):
            raise ValueError("All arguments must be booleans")

        if rs_type != "async" and rs_type != "sync":
            raise ValueError('Value of rs_type has to be "sync" or "async"')

        self.r = r
        self.s = s
        self.q = default_q
        self.q_neg = Gnot(self.q)()[0]
        self.clk = clk
        self.rs_type = rs_type

    def __call__(self, r: bool = None, s: bool = None, clk: bool = None) -> bool:
        if r is not None and isinstance(r, bool):
            self.r = r
        if s is not None and isinstance(s, bool):
            self.s = s
        if clk is not None and isinstance(clk, bool):
            self.clk = clk

        if self.rs_type == "async":
            if self.r == False:
                self.q = Gnand(self.q_neg, self.r)()
                self.q_neg = Gnand(self.q, self.s)()
            elif self.s == False:
                self.q_neg = Gnand(self.q, self.s)()
                self.q = Gnand(self.q_neg, self.r)()

        elif self.rs_type == "sync":
            if clk == False:
                pass
            else:
                r_clk_nand = Gnand(self.clk, self.r)()
                s_clk_nand = Gnand(self.clk, self.s)()

                if r_clk_nand == False:
                    self.q = Gnand(self.q_neg, r_clk_nand)()
                    self.q_neg = Gnand(self.q, s_clk_nand)()
                elif s_clk_nand == False:
                    self.q_neg = Gnand(self.q, s_clk_nand)()
                    self.q = Gnand(self.q_neg, r_clk_nand)()

        if self.q_neg == True and self.q == True:
            print("\033[93m" + "Forbidden state" + "\033[0m")

        return self.q

    def __str__(self) -> str:
        return "RSAsync"


class D(RS):
    def __init__(self, d: bool = False, clk: bool = False, default_q: bool = False):
        self.d = d
        self.clk = clk
        self.q = default_q
        self.q_neg = Gnot(self.q)()[0]

        super().__init__(self.d, Gnot(self.d)()[0], self.clk, self.q, rs_type="sync")

    def __call__(self, d: bool = None, clk: bool = None) -> bool:
        if d is not None and isinstance(d, bool):
            self.d = d
        if clk is not None and isinstance(clk, bool):
            self.clk = clk
        return super().__call__(
            self.d,
            Gnot(self.d)()[0],
            self.clk,
        )
