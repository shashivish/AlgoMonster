from typing import List


def word_break(s: str, words: List[str]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    memo = {}
    def helper(start):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        ans = False
        for word in words:
            # print("Searching ->", word)
            if s[start:].startswith(word):
                if helper(start + len(word)):
                    ans = True
                    break
        memo[start] = ans
        return ans

    return helper(0)


if __name__ == '__main__':
    # algomonster
    # algo monster
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    words = "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa".split()
    res = word_break(s, words)
    print('true' if res else 'false')
