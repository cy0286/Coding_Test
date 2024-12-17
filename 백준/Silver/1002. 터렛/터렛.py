import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist_x = (x1 - x2) ** 2
    dist_y = (y2 - y1) ** 2
    distance = math.sqrt(dist_x + dist_y)

    # if distance > r1 + r2: # 두 원이 떨어져 있을 때
    #     print(0)
    # elif distance == r1 + r2: # 외접
    #     print(1)
    # elif distance!= 0 and distance == abs(r1 - r2): # 한 원이 다른 원에 내접
    #     print(1)
    # elif distance!=0 and distance < r1 + r2: # 내접
    #     print(2)
    # elif distance!= 0 and distance < abs(r1 - r2): # 한 원이 다른 원 안에 있음
    #     print(0)
    # elif distance == 0 and r1 != r2: # 같은 중심, 다른 반지름
    #     print(0)
    # elif distance == 0 and r1 == r2: # 같은 중심, 같은 반지름
    #     print(-1)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 + r2 > distance > abs(r1 - r2):
            print(2)
        elif r1 + r2 == distance or abs(r1 - r2) == distance:
            print(1)
        else:
            print(0)