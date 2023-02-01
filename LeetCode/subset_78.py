def subset(arr):
    N = len(arr)
    res = [[]]

    def recurse(soFar, start):
        if start == N:
            return

        for i in range(start, N):
            soFar.append(arr[i])
            res.append(soFar[:])
            print("soFar : " , soFar)
            recurse(soFar, i + 1)
            soFar.pop()
            print("Poping So Far : " , soFar , " with i :" , i)
    recurse([], 0)

    return res


if __name__ == '__main__':
    arr = [1, 2, 3]
    result = subset(arr)
    print(result)
