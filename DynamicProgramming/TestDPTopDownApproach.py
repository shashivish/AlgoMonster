def perform_combination(input, current, start):
    if start == 3  :
        print(current)
        return



    perform_combination(input, current + [input[start]], start + 1)
    perform_combination(input, current, start + 1)
# if n == 0:
#     sums.add(sum)
#     return
# generate_sums(weights, sums, sum, n - 1)
# generate_sums(weights, sums, sum + weights[n - 1], n - 1)

if __name__ == '__main__':
    input = ['a', 'b', 'c']
    perform_combination(input, [], 0)
