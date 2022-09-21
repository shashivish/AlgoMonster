from collections import deque


def rotate_left_till_zero(nums):
    queue = deque(nums)
    while queue[0] != 0:
        left_element = queue.popleft()
        queue.append(left_element)
        print(queue)
    return queue

if __name__ == '__main__':
    nums = [7, 6, 4, 2, 8, 0]
    rotate_left_till_zero(nums)
