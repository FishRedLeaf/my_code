class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(index, path, visited):
            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                if i in visited:
                    continue
                c = candidates[i]
                if i > 0 and (candidates[i-1] == c and i-1 not in visited):
                    continue
                if c + sum(path) > target:
                    break
                
                visited.add(i)
                backtrack(i, path+[c], visited)
                visited.remove(i)
        res = []
        backtrack(0, [], set())
        return res