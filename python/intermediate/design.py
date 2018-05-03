class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ix = {}
        self.name = {}
        self.count = 0
        self.count_list = []



    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.name:
            return False
        else:
            self.count += 1
            self.name[val] = self.count
            self.ix[self.count] = val
            self.count_list.append(self.count)

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.name:
            return False
        else:
            ix = self.name[val]
            self.name.pop(val)
            self.ix.pop(ix)
            self.count_list.remove(ix)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        rand = random.random()
        ix = self.count_list[int(len(self.count_list) * rand)]
        return self.ix[ix]



        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()