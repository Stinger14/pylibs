def balancedSum(arr):
    size = len(arr)
    left_sum, right_sum, x, y = 0, 0, 0, 1
    
    # TODO divide array in 2 parts then get the sum of each side and compare
    
    for i in range(1, size):
        # start count at second element in arr
        right_sum += arr[i]
        
    while y < size:
        right_sum -= arr[y]
        left_sum += arr[x]
        
        if left_sum == right_sum:
            return arr[ x + 1]

        x += 1
        y += 1
    return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6]
    print(balancedSum(arr))