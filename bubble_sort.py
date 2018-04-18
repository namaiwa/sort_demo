# 冒泡排序


class Blist(object):
    def __init__(self, _list=None):
        self.l = _list

    def swap(self, i, j):
        if i != j:
            self.l[i], self.l[j] = self.l[j], self.l[i]

    def bubble_sort(self):
        length = len(self.l)
        for i in range(length):
            flag = True   # 设置flag，如果一次循环没有交换，说明已排序，break
            for j in range(length-i-1):
                if self.l[j] > self.l[j+1]:
                    self.swap(j, j+1)
                    flag = False
            if flag:
                break

    def __str__(self):
        return str(self.l)


if __name__ == '__main__':
    slist = Blist([1, 13, 5, 12, 4, 8, 5, 6, 23, 7, 5, 3, 2])
    slist.bubble_sort()
    print(slist)
