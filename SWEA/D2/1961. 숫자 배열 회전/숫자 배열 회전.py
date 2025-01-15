T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    degree_90 = [[0] * N for _ in range(N)]
    degree_180 = [[0] * N for _ in range(N)]
    degree_270 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            degree_90[j][N - 1 - i] = matrix[i][j]
            degree_180[N - 1 - i][N - 1 - j] = matrix[i][j]
            degree_270[N - 1 - j][i] = matrix[i][j]

    print(f"#{test_case}")
    for i in range(N):
        result_90 = ''.join(map(str, degree_90[i]))
        result_180 = ''.join(map(str, degree_180[i]))
        result_270 = ''.join(map(str, degree_270[i]))
        print(result_90, result_180, result_270)