class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        self.l = 0
        self.r = len(self.dictionary[key]) - 1
        result = ""
        while self.l <= self.r:
            self.m = (self.l+self.r) // 2
            if self.dictionary[key][self.m][1] == timestamp:
                return self.dictionary[key][self.m][0]
            if timestamp < self.dictionary[key][self.m][1]:
                self.r = self.m - 1
            else:
                result = self.dictionary[key][self.m][0]
                self.l = self.m + 1
        return result


    """
    [alice: happy, 1; sad, 3; happy, 5; mad, 6; happy, 7]
    

    1, 3, 5, 6, 7
    l = 0, r = 4
    m = 5
    1, 3
    l = 3

    10, 20, 30
    
    
    """
    