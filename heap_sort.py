# 堆排序


class HeapList(object):
    def __init__(self, _list=None):
        self.l = _list

    def swap(self, i, j):
        if i != j:
            self.l[i], self.l[j] = self.l[j], self.l[i]

    # 堆调整   s表示需要调整位置的序号， m表示堆的长度
    def heap_adjust(self, s, m):
        lis = self.l
        temp = lis[s]
        while s <= m/2 - 1:
            i = s * 2 + 1
            if i+1 < m:
                if lis[i] < lis[i+1]:
                    i += 1
            if temp > lis[i]:
                break
            lis[s] = lis[i]
            s = i
        lis[s] = temp

    # 堆排序
    def heap_sort(self):
        length = len(self.l)
        # 循环进行堆调整，直至最后数组变为一个完全二叉堆
        j = int(length/2)-1
        while j >= 0:
            self.heap_adjust(j, length)
            j -= 1
        # 循环将堆顶与数组最后元素交换位置，使堆的长度减一，对堆进行调整
        i = length - 1
        while i >= 0:
            self.swap(0, i)
            self.heap_adjust(0, i)
            i -= 1

    def __str__(self):
        return str(self.l)


if __name__ == '__main__':
    _list = HeapList([1, 13, 25, 12, 4, 8, 5, 6, 23, 7, 15, 3, 2])
    _list.heap_sort()
    print(_list)
