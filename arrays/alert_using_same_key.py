# Leetcode : https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hmap = {}
        for i in range(len(keyName)):
            hmap[keyName[i]] = hmap.get(keyName[i], []) + [int("".join(keyTime[i].split(":")))]

        results = []
        for ids, times in hmap.items():
            times.sort()
            for i in range(len(times)-2):
                if times[i+2] - times[i] < 60:
                    results.append(ids)
                    break
                elif times[i+2] // 100 == times[i] // 100 + 1 and times[i] % 100 - times[i+2] % 100 >= 0:
                    results.append(ids)
                    break
        return sorted(results)