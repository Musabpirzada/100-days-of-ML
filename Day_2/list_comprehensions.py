if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    liss = [i for i in range(x+1)]
    piss = [j for j in range(y+1)]
    ziss = [k for k in range(z+1)]
    finall = [[a,b,c] for a in liss for b in piss for c in ziss]
    sums = [t for t in finall if sum(t) != n]
    print(sums)
