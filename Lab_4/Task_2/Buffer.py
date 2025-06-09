class Buffer:
    def __init__(self):
        self._data = []

    def add(self, *a):
        self._data.extend(a)

        while len(self._data) >= 5:
            five = self._data[:5]
            print(sum(five))
            self._data = self._data[5:]

    def get_current_part(self):
        return self._data