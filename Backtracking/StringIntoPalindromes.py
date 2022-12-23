from typing import List


def partition(s: str) -> List[List[str]]:
    ans = []

    n = len(s)
    print("Lenght of String : " , n)
    def is_palindrome(word):
        return word == word[::-1]

    def dfs(start, cur_path):
        if start == n:
            ans.append(cur_path[:])
            return

        for end in range(start + 1, n + 1):
            print("Start ", start, " End ", end)
            prefix = s[start: end]
            print("Prefix : ", prefix)
            if is_palindrome(prefix):
                dfs(end, cur_path + [prefix])

    dfs(0, [])
    return ans


if __name__ == '__main__':
    s = 'aab'
    res = partition(s)
    for row in res:
        print(' '.join(row))
