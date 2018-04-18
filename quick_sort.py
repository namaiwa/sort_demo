# 快速排序


class Qlist(object):
    def __init__(self, _list=None):
        self.l = _list

    def swap(self, i, j):
        if i != j:
            self.l[i], self.l[j] = self.l[j], self.l[i]

    def quick_sort(self, start, end):
        pivot_key = self.l[start]  # 轴点选取列表第一个元素
        j = start                   # j代表小于轴点序列末尾下标
        for i in range(start+1, end+1):      # 0号元素被选作轴点，所以从一号元素开始
            if self.l[i] < pivot_key:
                j += 1
                self.swap(i, j)
        self.swap(start, j)

        # 递归调用
        if start < j-1:
            self.quick_sort(start, j-1)
        if end > j+1:
            self.quick_sort(j+1, end)

    def __str__(self):
        return str(self.l)


if __name__ == '__main__':
    slist = Qlist([13, 1, 5, 12, 4, 8, 15, 6, 23, 7, 5, 3, 2])
    slist.quick_sort(0, len(slist.l)-1)
    print(slist)
