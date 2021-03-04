class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(index, path):
            if sum(path) == target:
                res.append(path)
                return
            # 保证升序,否则出现[[2,2,3],[2,3,2],[3,2,2],[7]]
            for i in range(index, len(candidates)):
                if sum(path) + candidates[i] > target:
                    break
                backtrack(i, path+[candidates[i]])
        res = []
        backtrack(0, [])
        return res