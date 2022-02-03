class Stack:

    def __init__(self):
        self._dataList = []


    def push(self, data):
        # self._dataList.append(data)
        self._dataList = [data] + self._dataList


    def pop(self, data):
        if len(self._dataList) == 0:
            return None

        first = data[0]
        self._dataList.remove(first)
        return first


    def get_count(self):
        pass

    def peek(self): 
        pass

    def __iter__(self):
        pass
