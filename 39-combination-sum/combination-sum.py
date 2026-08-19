class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def solve(start, current, total):

            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                current.append(candidates[i])

                solve(i, current, total + candidates[i])

                current.pop()

        solve(0, [], 0)

        return result