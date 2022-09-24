# Leetcode: https://leetcode.com/problems/avoid-flood-in-the-city/

from bisect import bisect_left
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1 if lake > 0 else 1 for lake in rains]
        full_lakes, dry_days = {}, []
        for day, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(day)
            else:
                if lake in full_lakes:
                    dry_day = bisect_left(dry_days, full_lakes[lake])
                    if dry_day >= len(dry_days):
                        return []
                    res[dry_days.pop(dry_day)] = lake
                    full_lakes[lake] = day
                else:
                    full_lakes[lake] = day
        return res
        