class IncreasingList:
    l = []
    def append(self, val):
        [x for x in reversed(self.l) if x <= val]
        self.l.append(val)

    def pop(self):
        if self.l:
            self.l.pop()
        else:
            pass

    def __len__(self):
        return str(self.l)


if __name__ == '__main__':
    lst = IncreasingList()
    q = int(input())
    for _ in range(q):
        op = input().split()
        op_name = op[0]
        if op_name == "append":
            val = int(op[1])
            lst.append(val)
        elif op_name == "pop":
            lst.pop()
        elif op_name == "size":
            print(op_name)
        else:
            raise ValueError("invalid operation")
