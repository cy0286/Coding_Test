from itertools import combinations

heights = [int(input()) for _ in range(9)] # 9명 중 7명 탐색

for comb in combinations(heights, 7):
    if sum(comb) == 100:
        result = sorted(comb)
        print(*result, sep ='\n')
        break