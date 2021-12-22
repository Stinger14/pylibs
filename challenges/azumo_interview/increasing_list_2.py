class IncreasingList:
    data = 0
    n = 9
    def append(self, val):
        self.data = [x for x in reversed(self.data) if x <= val]
        self.data.append(val)

    def pop(self):
        if self.data:
            self.data.pop()
        else:
            pass

    def __len__(self):
        pass

    for i in range(n):  
        p=input().split()
        if p[0]=="insert":
            list.insert(int(p[1]),int(p[2]))
        elif p[0]=="print":
            print(list)
        
        elif (p[0]=="remove"):
            list.remove(int(p[1]))
        elif p[0]=="append":
            list.append(int(p[1]))
        elif p[0]=="sort":
            list.sort()
        elif p[0]=="print":
            print(list)
        elif p[0]=="pop":
            list.pop()
        elif p[0]=="reverse":
            list.reverse()
        elif p[0]=="print":
            print(list)

    def append(self, val):
        """
        first, it removes all elements from the list that have greater values than val, starting from the last one, and once there are no greater element in the list, it appends val to the end of the list
        """
        # started from the bottom...
        self._data = [x for x in reversed(self._data) if x <= val]
        self._data.append(val)
        
    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise, if the list is empty, it does nothing
        """
        if self._data:
            self._data.pop()
        else:
            pass

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return str(self._data)


if __name__ == '__main__':
    obj = IncreasingList([1,2,3])
    print(len(obj))
    obj.pop()
    print(obj)
    obj.append(2)
    print(obj)