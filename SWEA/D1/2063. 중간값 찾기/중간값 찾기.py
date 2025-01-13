N = int(input())
score = list(map(int, input().split()))
score.sort()
n = len(score)
median = score[n // 2]
print(median)