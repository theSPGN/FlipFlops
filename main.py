import flipflop as ff

if __name__ == "__main__":
    print("\nRS-sync flipflop:")
    for i in range(2):
        for j in range(2):
            k = ff.RS(r=bool(i), s=bool(j), clk=True, default_q=True, rs_type="sync")
            print(f"r={i}, s={j}, q={int(k())}")

    print("\nRS-async flipflop:")
    for i in range(2):
        for j in range(2):
            k = ff.RS(r=bool(i), s=bool(j), clk=True, default_q=False, rs_type="async")
            print(f"r={i}, s={j}, q={int(k())}")

    print("\nD flipflop:")
    for i in range(2):
        for j in range(2):
            k = ff.D(d=bool(i), clk=bool(j), default_q=False)
            print(f"d={i}, clk={j}, q={int(k())}")
