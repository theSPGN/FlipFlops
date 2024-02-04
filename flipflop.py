from gates import NandGate as Gnand
from gates import NotGate as Gnot
from try_input import try_input


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
            not try_input(r)
            or not try_input(s)
            or not try_input(clk)
            or not try_input(default_q)
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
        if r is not None and try_input(r):
            self.r = r
        if s is not None and try_input(s):
            self.s = s
        if clk is not None and try_input(clk):
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
        if d is not None and try_input(d):
            self.d = d
        if clk is not None and try_input(clk):
            self.clk = clk
        return super().__call__(
            self.d,
            Gnot(self.d)()[0],
            self.clk,
        )


class JK(RS):
    def __init__(
        self,
        j: bool = False,
        k: bool = False,
        clk: bool = False,
        default_q: bool = False,
    ):
        self.j = j
        self.k = k
        self.clk = clk
        self.q = default_q
        self.q_neg = Gnot(self.q)()[0]
        self.r = Gnand(self.j, self.clk, self.q_neg)()
        self.s = Gnand(self.k, self.clk, self.q)()

        super().__init__(self.r, self.s, self.clk, self.q, rs_type="async")

    def __call__(self, j: bool = None, k: bool = None, clk: bool = None) -> bool:
        if j is not None and try_input(j):
            self.j = j
        if clk is not None and try_input(clk):
            self.clk = clk
        if k is not None and try_input(k):
            self.k = k

        self.r = Gnand(self.j, self.clk, self.q_neg)()
        self.s = Gnand(self.k, self.clk, self.q)()

        return super().__call__(
            self.r,
            self.s,
            self.clk,
        )


class Edge:
    def __init__(self, clk: bool = False, edge_type: str = "rising"):
        self.clk = clk
        self.edge_type = edge_type

    def __call__(self, clk: bool = None):
        if self.edge_type not in ["rising", "falling"]:
            self.edge_type = "rising"
            print(
                "\033[93m"
                + "The edge has been set on rising mode, "
                + "please specify type of edge, to remove this message"
                + "\033[0m"
            )

        clk = self.clk if clk is None else clk
        if not try_input(clk):
            raise ValueError("All arguments must be booleans")
        if self.clk == clk:
            return False
        else:
            if self.edge_type == "rising" and clk == True:
                self.clk = clk
                return True
            elif self.edge_type == "falling" and clk == False:
                self.clk = clk
                return True
            else:
                return False
