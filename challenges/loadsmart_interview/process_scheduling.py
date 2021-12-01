def minimumTime(ability, processes):
    pass
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ability_count = int(input().strip())

    ability = []

    for _ in range(ability_count):
        ability_item = int(input().strip())
        ability.append(ability_item)

    processes = int(input().strip())

    result = minimumTime(ability, processes)

    fptr.write(str(result) + '\n')

    fptr.close()