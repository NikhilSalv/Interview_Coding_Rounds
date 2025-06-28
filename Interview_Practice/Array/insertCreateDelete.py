import random


"""

"""
class RandomizedSet(object):

    def __init__(self):
        self.elements = []
        self.element_index = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.elements:
            self.elements.append(val)
            self.element_index[val] = len(self.elements) - 1
            return True
        else:
            return False

        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.elements:
            index_to_remove = self.element_index[val]
            last_element = self.elements.pop()
            self.elements[index_to_remove] = last_element
            self.element_index[last_element] = index_to_remove

            del self.element_index[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.elements)


if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.insert(3))
    print(obj.insert(4))
    print(obj.insert(5))
    print(obj.remove(3))
    print(obj.elements)
    print(obj.element_index)
    