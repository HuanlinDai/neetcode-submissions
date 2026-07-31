class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                change[5] += 1
                continue
            elif bills[i] == 10:
                change[10] += 1
                if change[5] > 0:
                    change[5] -= 1
                    continue
                else:
                    return False
            elif bills[i] == 20:
                if change[10] > 0:
                    if change[5] > 0:
                        change[10] -= 1
                        change[5] -= 1
                        continue
                    else:
                        return False
                elif change[5] > 2:
                    change[5] -= 2
                else:
                    return False

        return True