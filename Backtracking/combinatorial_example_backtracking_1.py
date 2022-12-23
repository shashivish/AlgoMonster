from typing import List


def letter_combination(n: int) -> List[str]:
    def dfs(start, path):
        if start == n:
            res.append(''.join(path))
            return

        for letter in ['a', 'b']:
            path.append(letter)
            print("Path : " , path)
            dfs(start + 1, path)
            print("Being Pop" , path)
            path.pop()
            print("After Pop" , path)

    res = []
    dfs(0, [])
    return res


if __name__ == '__main__':
    n = 2
    res = letter_combination(n)
    for line in sorted(res):
        print(line)
