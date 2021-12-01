class LengthMetaClass(type):
    length = 10
    def __len__(self):
        return self.clslength()


class IncreasingList(object, metaclass=LengthMetaClass):
    @classmethod
    def clslength(cls):
        return cls.length

a = IncreasingList
print(len(a))
