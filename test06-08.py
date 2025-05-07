i, j = 0, 0

for i in range(0, 9):
    if i < 5:
        for j in range(0, 4-i, 1):
            print("  ", end="")
        for j in range(0, i*2+1, 1):
            print("\u2665",end="")
    else:
        for j in range(0, i-4, 1):
            print("  ", end="")
        for j in range(0, (9-i)*2-1, 1):
            print("\u2665",end="")
    print()
