class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []

        def find_combinations(start_index, current_target, current_path):
            if current_target == 0:
                results.append(list(current_path))
                return
            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > current_target:
                    break
                
                current_path.append(candidates[i])
                find_combinations(i + 1, current_target - candidates[i], current_path)
                current_path.pop()

        find_combinations(0, target, [])
        return results