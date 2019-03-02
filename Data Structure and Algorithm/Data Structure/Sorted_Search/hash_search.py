"""
一 、创建一个散列函数，最大限度地减少冲突数，易于计算，并均匀分布在哈希表中的项
1 简单余数法
2 分组求合法
3 平方取中法

二 、冲突解决方法:(扩展)线性探测(+1/+n)
三 、查找:相应的也要用线性探测

hashvalue  0   1   2  3   4   5   6    7     8    9  10
slot      77  44  20  55  26  93  17  none  none  31  54
data      dog cat pig ...
"""

class HashTable():
    def __init__(self):
        self.size = 11        # 初始为11个槽key ,一般是质数
        self.slots = [None] * self.size  # key
        self.data = [None] * self.size   # value

    def put(self, key, data):
        # 先计算hash值
        hashvalue = self.hashfunction(key, len(self.slots))
        # 如果该hashvalue对应的slot没有值   put进去 比如一开始放入77(hashvalue==0)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        # 如果该hashvalue对应的slot已经有值 (两个数的hashvalue一样了)
        else:
            # 如果hashvalue对应的槽已有值且与待放入的key相同则replace  比如已有[77]dog 又放入[77]cat
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            # 如果hashvalue对应的槽已有值且与待放入的key不同,发生冲突
            # 冲突解决技术是 加1 rehash 函数的线性探测
            # 比如已有[77]dog 又放入[44]cat
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                # 如果该槽不为空，则迭代 rehash 函数，直到出现空槽或者槽的值与key相同
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                # 空槽
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                # 槽的值与key相同
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        """hash 函数实现简单的余数方法"""
        return key % size

    def rehash(self, oldhash, size):
        """冲突解决技术是 加1 rehash 函数的线性探测"""
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                # 找一圈没找到 return  data ==none 并stop
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
        
if __name__ == "__main__":
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    # [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
    print(H.data)
    # ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']

    # 如果有 替换新data
    H[20] = 'duck'
    print(H.data)
    # ['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']

    # 查找
    print(H[20])
    # duck
    print(H[99])
    # None
