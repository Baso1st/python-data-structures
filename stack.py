

class Stack:

    def __init__(self):
        self._dataList = []


    def push(self, data):
        self._dataList = [data] + self._dataList


    def pop(self):
        if len(self._dataList) == 0:
            return

        first = self._dataList[0]
        self._dataList.remove(first)
        return first

    def get_count(self):
        return len(self._dataList)

    def peek(self): 
        return self._dataList[0]

    def __iter__(self):
        return iter(self._dataList)
