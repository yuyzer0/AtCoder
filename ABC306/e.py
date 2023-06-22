from collections import defaultdict
import heapq


n, k, q = map(int, input().split())
list_xy = []
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    list_xy.append([x, y])

list_a = [0] * n
upper = [0] * k
upper_size = k
lower = [0 * -1] * (n - k)
deleted_cnt_upper = defaultdict(int)
deleted_cnt_lower = defaultdict(int)

ans = 0

for x, y in list_xy:
    now_a = list_a[x]
    list_a[x] = y
    min_upper = -1
    max_lower = -1
    # min_uppper の決定
    while len(upper) > 0:
        min_upper = heapq.heappop(upper)
        if deleted_cnt_upper[min_upper] > 0:
            deleted_cnt_upper[min_upper] -= 1
            continue
        else:
            heapq.heappush(upper, min_upper)
            break
    # max_lower の決定
    while len(lower) > 0:
        max_lower = heapq.heappop(lower) * -1
        if deleted_cnt_lower[max_lower] > 0:
            deleted_cnt_lower[max_lower] -= 1
            continue
        else:
            heapq.heappush(lower, max_lower * -1)
            break
    # 更新 now_a
    if now_a >= min_upper:
        # upperの値を変更
        if y >= min_upper:
            heapq.heappush(upper, y)
            deleted_cnt_upper[now_a] += 1
            ans += y - now_a
        else:
            deleted_cnt_upper[now_a] += 1
            heapq.heappush(lower, y * -1)
            max_lower = heapq.heappop(lower) * -1
            heapq.heappush(upper, max_lower)
            ans += max_lower - now_a
    else:
        # lowerの値を変更
        if y < min_upper:
            deleted_cnt_lower[now_a] += 1
            heapq.heappush(lower, y * -1)
        else:
            deleted_cnt_lower[now_a] += 1
            heapq.heappush(upper, y)
            min_upper = heapq.heappop(upper)
            heapq.heappush(lower, min_upper * -1)
            ans += y - min_upper
    print(ans)
