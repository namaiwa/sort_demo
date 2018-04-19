# 归并排序


class MList(object):
    def __init__(self, _list=None):
        self.l = _list

    def swap(self, i, j):
        if i != j:
            self.l[i], self.l[j] = self.l[j], self.l[i]

    # 排序
    def merging_sort(self, start, end):   # 包括start，不包括end
        if end-start < 2:                 # 递归基
            return
        mi = int((end+start)/2)           # 以中点为界
        self.merging_sort(start, mi)      # 对前半段排序
        self.merging_sort(mi, end)        # 对后半段排序
        self.merging(start, mi, end)      # 归并

    # 归并
    def merging(self, start, mi, end):
        temp_list = self.l[start: mi]
        i = 0       # 临时列表索引
        j = mi      # 后半部分列表索引
        k = start   # 列表重排列部分的索引
        while 1:
            if temp_list[i] < self.l[j]:
                self.l[k] = temp_list[i]
                i += 1
                k += 1
                if i == len(temp_list):  # 如果临时列表遍历完,则可直接返回
                    return
            else:
                self.l[k] = self.l[j]
                k += 1
                if j < end-1:
                    j += 1
                else:
                    self.l[j] = float('inf')   # 如果后半部分列表遍历完,则在最后增加一个无穷大的哨兵

    def __str__(self):
        return str(self.l)


if __name__ == '__main__':
    _list = MList([1, 13, 25, 12, 4, 8, 5, 6, 23, 7, 15, 3, 33])
    _list.merging_sort(0, len(_list.l))
    print(_list)
