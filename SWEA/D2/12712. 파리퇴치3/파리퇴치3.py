T = int(input())

def result(graph, N, M):
    answer = []
    for i in range(N):
        for j in range(N):
            bugs = 0;

            # + 형태
            bugs += graph[i][j]
            for k in range(1, M):
                if i - k >= 0:
                    bugs += graph[i - k][j]
                if i + k < N:
                    bugs += graph[i + k][j]
                if j - k >= 0:
                    bugs += graph[i][j - k]
                if j + k < N:
                    bugs += graph[i][j + k]
            answer.append(bugs)

            # x 형태
            bugs = 0;
            bugs += graph[i][j]
            for k in range(1, M):
                if i - k >= 0 and j - k >= 0:
                    bugs += graph[i - k][j - k]
                if i + k < N and j + k < N:
                    bugs += graph[i + k][j + k]
                if i + k < N and j - k >= 0:
                    bugs += graph[i + k][j - k]
                if i - k >= 0 and j + k < N:
                    bugs += graph[i - k][j + k]
            answer.append(bugs)
    return max(answer)

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = []

    for _ in range(N):
        graph.append(list(map(int, input().split())))
    print(f"#{test_case} {result(graph, N, M)}")