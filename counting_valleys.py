# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def countingValleys(steps, path):
    level = sol = 0
    for p in path:
        level = level + 1 if p == 'U' else level - 1
        if level == 0:
            sol = sol + 1 if p == 'U' else sol
    return sol