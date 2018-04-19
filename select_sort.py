# 选择排序


class Slist(object):
    def __init__(self, _list=None):
        self.l = _list

    def swap(self, i, j):
        if i != j:
            self.l[i], self.l[j] = self.l[j], self.l[i]

    def select_sort(self):
        length = len(self.l)
        for i in range(length):
            max_num = 0
            for j in range(length-i):
                if self.l[j] > self.l[max_num]:
                    max_num = j
            self.swap(max_num, length-i-1)

    def __str__(self):
        return str(self.l)


if __name__ == '__main__':
    _list = Slist([1, 13, 5, 12, 4, 8, 15, 6, 23, 7, 5, 3, 2])
    _list.select_sort()
    print(_list)
