stack = []


def push_element(x: int) -> None:
    stack.append(x);
    print(f"Element {x} has been pushed")


def pop_element():
    if len(stack) > 0:
        stack.pop()
        print("Element has been popped out")
    else:
        print("Stack is Empty.")


def print_stack():
    print(f"{stack}  with total element {len(stack)}")


def print_last_element_in_stack():
    print(f"Last Element in Stack : {stack[-1]}")


if __name__ == '__main__':
    # write a function for stack operation
    push_element(3)
    push_element(5)
    print_stack()
    print_last_element_in_stack()
    pop_element()
    print_stack()
    pop_element()
    pop_element()
