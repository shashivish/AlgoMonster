import collections
from typing import List
from collections import deque


def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    if end not in word_list:
        return 0

    pattern_map = collections.defaultdict(list)
    word_set = set(word_list)
    word_set.add(begin)
    for word in word_set:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            pattern_map[pattern].append(word)

    #print("Pattern Map", pattern_map)

    queue = deque([begin])
    visited = set()
    res = 0

    while queue:
        n = len(queue)
        for _ in range(n):
            word = queue.popleft()

            if word == end:
                return res

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                possible_next_words = pattern_map[pattern]
                for next_word in possible_next_words:
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append(next_word)
        res += 1

    return res


if __name__ == '__main__':
    begin = input()
    end = input()
    word_list = input().split()
    res = word_ladder(begin, end, word_list)
    print(res)
