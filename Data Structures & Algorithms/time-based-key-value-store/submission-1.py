class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key,[]) + [(timestamp, value)]
        return None
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.store.get(key,[])
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]
            elif arr[m][0] > timestamp:
                r = m - 1
            else:
                res = arr[m][1]
                l = m + 1
        return res
        
