# Complete the 'cmap' function below.
#
# The function must be a generator and should return an iterable.
# The function accepts following parameters:
#  1. STRING_ARRAY funcs
#  2. INTEGER_ARRAY arr
#

import types


def cmap(funcs, arr):
    # Write your code here
    while funcs:
        yield funcs
        map(funcs, arr)

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    funcs_count = int(input().strip())

    funcs = []

    for _ in range(funcs_count):
        funcs_item = input().strip()
        funcs.append(eval(funcs_item))

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = cmap(funcs, arr)
    assert(isinstance(result, types.GeneratorType))
    output = []
    for result_item in result:
        output.append(result_item)
    fptr.write('\n'.join(map(str, output)))
    fptr.write('\n')

    fptr.close()