# 插入排序


class Ilist(object):
    def __init__(self, _list=None):
        self.l = _list

    # def swap(self, i, j):
    #     if i != j:
    #         self.l[i], self.l[j] = self.l[j], self.l[i]

    def insert_sort(self):
        length = len(self.l)
        for i in range(1, length):
            if self.l[i] < self.l[i-1]:
                temp = self.l[i]
                j = i-1

                # 赋值次数太多
                # while self.l[j] > self.l[j+1] and j >= 0:
                #     self.swap(j, j+1)
                #     j -= 1

                # 利用temp变量，减少赋值次数
                while temp < self.l[j] and j >= 0:
                    self.l[j+1] = self.l[j]
                    j -= 1
                self.l[j+1] = temp

    def __str__(self):
        return str(self.l)


if __name__ == '__main__':
    _list = Ilist([1, 13, 5, 12, 4, 8, 15, 6, 23, 7, 5, 3, 2])
    _list.insert_sort()
    print(_list)
