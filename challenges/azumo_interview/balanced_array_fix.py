def balancedSum(arr):
    size = int(len(arr)/2)
    sum1, sum2, = 0, 0,

    for i in range(0, size):
        sum1 += arr[i]

    for i in range(size, len(arr)):
        sum2 += arr[i]

    diff = sum1 - sum2
    if diff < 0:
        diff = (diff - diff * 2)
    elif diff == 0:
        return 0
    return diff

if __name__ == '__main__':
    arr = [1, 2, 5, 2, 4, 2]
    print(balancedSum(arr))