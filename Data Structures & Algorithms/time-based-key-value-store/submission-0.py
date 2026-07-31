class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key,[]) + [(timestamp, value)]
        return None
    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key,[])
        if len(arr) == 0:
            return ""
        l = 0
        r = len(arr) - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]
            elif arr[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        if arr[m][0] <= timestamp:
            return arr[m][1]
        elif m > 0 and arr[m-1][0] <= timestamp:
            return arr[m-1][1]
        else:
            return ""
        
