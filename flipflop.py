class RS:
    def __init__(self, r: bool = False, s: bool = False):
        if not isinstance(r, bool) or not isinstance(s, bool):
            raise ValueError("All arguments must be booleans")
        self.r = r
        self.s = s
        self.q = float("nan")
