from collections import deque
if __name__ == '__main__':
    # Create deque instance
    queue = deque()
    # check if queue is empty
    if len(queue) == 0:
        print("Queue is empty")

    # Insert element in queue
    queue.append(3)
    queue.append(4)
    print(queue)

    # pop element
    queue.popleft()  # Return leftmost element whereas pop() removes right most element

    # add more element
    queue.append(7)
    queue.append(8)
    print(queue)

    # pop right
    queue.pop()
    print(queue)
