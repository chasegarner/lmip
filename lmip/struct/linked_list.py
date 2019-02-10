class LinkedList:

    def __init__(self):
        self._length = 0

    def __getitem__(self, target_index):
        for current_index, item in enumerate(self):
            if current_index == target_index:
                return item.value


    def __setitem__(self, index):
        pass

    def __delitem__(self, index):
        pass

    def __len__(self):
        return self._length

    def __iter__(self):
        pass

    def __contains__(self):
        pass

    def insert(self):
        pass

    def append(self):
        pass

    def delete(self):
        pass


class _ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        pass
