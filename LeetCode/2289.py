def totalSteps(nums):
    counter = 0

    def removeElement(nums):
        flag = False
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] > nums[i]:
                nums.pop(i)
                flag = True
            i -= 1
        return flag

    flag = True
    while flag:
        counter += 1
        flag = removeElement(nums)
        print(nums , "Flag ", flag )


    return counter


if __name__ == '__main__':
    nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]
    print(totalSteps(nums))
