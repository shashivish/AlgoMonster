import heapq


def nth_ugly_number(n: int) -> int:
    prime_numbers = [2, 3, 5]
    ans = [1]
    used = [1]
    for _ in range(n-1):
        n = heapq.heappop(ans)
        for multiplier in prime_numbers:
            if multiplier*n not in used :
                heapq.heappush(ans  , multiplier*n)
                used.append(multiplier*n)
        print(used)

    return ans[0]


if __name__ == '__main__':
    n = int(input())
    res = nth_ugly_number(n)
    print(res)
