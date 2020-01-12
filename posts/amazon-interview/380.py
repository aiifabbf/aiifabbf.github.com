import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {} # key存val，value存val在array list中的下标
        self.buffer = [] # 这就是那个array list，存的是val

    def insert(self, val: int) -> bool: # 插入的时候比较简单
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mapping: # 如果本来就在里面
            return False # 啥也不做
        else: # 如果不在里面
            self.mapping[val] = len(self.buffer) # 开一个新的条目，key存val，value指向array list的最后一个格子
            self.buffer.append(val) # array list的最后建一个新的格子，存val
            return True

    def remove(self, val: int) -> bool: # 删除的时候是最麻烦的
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mapping: # 如果val存在
            thatValue = self.buffer[-1] # 先看下array list的最后一个元素是什么
            self.mapping[val], self.mapping[thatValue] = self.mapping[thatValue], self.mapping[val] # 调换一下两个条目的value
            # self.buffer[self.mapping[val]] = val # 没有必要更新这个条目的value指向的array list里那个格子里的元素，因为反正要删掉的
            self.buffer[self.mapping[thatValue]] = thatValue # 更新一下那个条目的value指向的array list里那个格子里的元素
            self.buffer.pop() # 删掉array list的最后一个元素
            self.mapping.pop(val) # 删掉hash map里对应的条目
            return True
        else: # 如果val不存在
            return False # 啥也不做

    def getRandom(self) -> int: # 随机取也很简单
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.buffer) - 1) # 随机产生一个下标
        return self.buffer[index] # 到array list里面去取那个下标的val

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()