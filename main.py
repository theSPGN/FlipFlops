import flipflop as ff

if __name__ == "__main__":

    q = ff.RS(r=0, s=0, clk=0, default_q=True, rs_type="sync")
    print("\nRS-sync flipflop:")
    for clk in range(2):
        for r in range(2):
            for s in range(2):
                output = q(r=r, s=s, clk=clk)
                print(f"r={r}, s={s}, clk={clk} q={int(output)}")


    q = ff.RS(r=0, s=0, default_q=False, rs_type="async")
    print("\nRS-async flipflop:")
    for r in range(2):
        for s in range(2):
            output = q(r=r, s=s)
            print(f"r={r}, s={s}, q={int(output)}")


    q = ff.D(d=0, clk=0, default_q=True)
    print("\nD flipflop:")
    for clk in range(2):
        for d in range(2):
            output = q(d=d, clk=clk)
            print(f"d={d}, clk={clk}, q={int(output)}")


    q = ff.JK(j=0, k=0, clk=0, default_q=False)
    print("\nJK flipflop:")
    for clk in range(2):
        for j in range(2):
            for k in range(2):
                output = q(j=j, k=k, clk=clk)
                print(f"j={j}, k={k}, clk={clk}, q={int(output)}")
