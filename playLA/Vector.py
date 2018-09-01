class Vector:
    def __init__(self, lst):
        self._values = lst

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self, other)])

    def __getitem__(self, index):
        """取向量第一个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度"""
        return len(self._values)

    def __repr__(self):
        """迭代器"""
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

