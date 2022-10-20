# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def jumpingOnClouds(c):
    sol = [0] * len(c)
    sol[len(c)-1] = 0 
    sol[len(c)-2] = 1 if c[len(c)-2] == 0 else float('inf')

    for i in range(len(c)-3, -1, -1):
        sol[i] = min(sol[i+1], sol[i+2]) + 1 if c[i] == 0 else float('inf')
    return sol[0]