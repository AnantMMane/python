class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__data_list = []

    def put(self, elem):
        self.__data_list.insert(0, elem)

    def get(self):
        if len(self.__data_list):
            return self.__data_list.pop()
        else:
            raise QueueError()

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        print("Queue contents:", self._Queue__data_list)
        self._Queue__data_list.insert(0,'Dummy')
        return len(self._Queue__data_list) == 0

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")