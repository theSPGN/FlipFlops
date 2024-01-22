import flipflop as ff

if __name__ == "__main__":
    for i in range(2):
        for j in range(2):
            k = ff.RS(r=bool(i), s=bool(j), default_q=False, clk=True, rs_type="sync")
            print(f"r={i}, s={j}, q={k()}")
