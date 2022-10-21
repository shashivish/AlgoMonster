def square_root(n: int) -> int:
    start = 1    
    square_value = 1    
    while square_value <= n :
        start += 1
        square_value = start * start


    return start-1

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
