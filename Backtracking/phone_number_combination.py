from typing import List

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(start, path):
        if start == len(digits):
            res.append(''.join(path))
            return

        next_number = digits[start]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(start + 1, path)
            path.pop()

    res = []
    dfs(0, [])
    return res


if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))
