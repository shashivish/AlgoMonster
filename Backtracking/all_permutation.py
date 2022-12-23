from typing import List


def permutations(letters):

    def dfs(start_index, path, used, res):
        if start_index == len(letters):
            res.append(path)
            print("Added to Result : ", res)
            return

        for i, letter in enumerate(letters):
            # skip used letters
            print("For i ", i, " Letter ", letter)
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            print("Added to Path ", path)
            used[i] = True
            dfs(start_index + 1, path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False
        return res

    res = []
    res  = dfs(0, [], [False] * len(letters), res)
    print("Final Result : ", res)
    return res


if __name__ == '__main__':
    letters = ['a', 'b', 'c']
    res = permutations(letters)
    print("Result : " , res)
    for line in sorted(res):
        print(line)
