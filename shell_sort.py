# 希尔排序
# 以插入排序为基础的改进排序算法


class ShellList(object):
    def __init__(self, _list=None):
        self.l = _list

    def shell_sort(self):
        length = len(self.l)

        increment = length
        while increment > 1:
            increment = int(increment/2)   # 设置增量

            for i in range(increment, length):      # 利用插入排序的方法对每组进行排序
                if self.l[i] < self.l[i-increment]:
                    temp = self.l[i]
                    j = i-increment
                    while temp < self.l[j] and j >= 0:
                        self.l[j+increment] = self.l[j]
                        j -= increment
                    self.l[j+increment] = temp

    def __str__(self):
        return str(self.l)


if __name__ == '__main__':
    _list = ShellList([1, 13, 5, 12, 4, 8, 15, 6, 23, 7, 5, 3, 2])
    _list.shell_sort()
    print(_list)
