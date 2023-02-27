def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    square = [i * i for i in range(1, n)]
    #print(square)

    res = []

    def dfs(suma, target, count):
        if suma > target:
            return
        if target == suma:
            print("Target Reached ", count)
            res.append(count)
            return

        for n in square:
            dfs(suma + n, target, count + 1)

    dfs(0, n, 0)

    return min(res)


if __name__ == '__main__':
    res = numSquares(12)
    print("Final Result : " , res)