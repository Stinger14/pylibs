if __name__ == '__main__':
    nl, tmp = [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nl.append([name, score])
    ls2 = sorted(set([x[1] for x in nl]))
    for x in nl:
        if x[1] == ls2[1]:
            tmp.append(x[0])
    print('\n'.join(x for x in sorted(tmp)))
