if __name__ == '__main__':
    x, y, z, n = map(int, input('enter vals with spaces').split(" "))
    print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])