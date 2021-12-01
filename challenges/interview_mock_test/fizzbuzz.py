def fizzBuzz(n):
    for i in range(n + 1):
        if i == 0:
            i += 1
            continue
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            continue
        elif i % 3 == 0:
            print('Fizz')
            continue
        elif i % 5 == 0:
            print('Buzz')
            continue
        print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)