# Complete the 'cmap' function below.
#
# The function must be a generator and should return an iterable.
# The function accepts following parameters:
#  1. STRING_ARRAY funcs
#  2. INTEGER_ARRAY arr
#
# funcs may be: lambda x:x*x or lambda x:x+x
# arr may be: [1,2,4,5]


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


def my_funcs(funcs):
    for f in funcs:
        return f()


def cmap(funcs, arr):
    # Write your code here
    yield map(my_funcs, arr)

if __name__ == '__main__':
    # print(list(cmap(['lamda x:x*x', 'lambda x:x+x'], [1,2,4,5])))
    # gen = infinite_sequence()
    funcs = ['lambda x:x*x', 'lambda x:x+x']
    arr = [1,2,4,5]
    m = cmap([x.strip('') for x in funcs], arr)
    print(list((m)))   
