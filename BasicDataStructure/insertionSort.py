def insertion_sort_list(unsorted_list: list[int]) -> list[int]:
    for i, num in enumerate(unsorted_list):
        print("Index ", i, "  Value : ", num)
        print("List to Be Sorted : ", unsorted_list)
        current = i
        while current > 0:
            if unsorted_list[i] < unsorted_list[i - 1]:
                # swap if first one is smaller
                print("Swapping Element : ", unsorted_list[i], unsorted_list[i - 1])
                unsorted_list[i], unsorted_list[i - 1] = unsorted_list[i - 1], unsorted_list[i]
            current -= 1

    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [-1, 5, 8, 0, 10]
    sorted_list = insertion_sort_list(unsorted_list)
    print(sorted_list)
