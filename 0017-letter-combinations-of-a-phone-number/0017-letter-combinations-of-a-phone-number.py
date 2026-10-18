class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = [""]
        for d in digits:
            temp = []
            letters = mapping[d]
            for prefix in res:
                for char in letters:
                    temp.append(prefix + char)
            res = temp
            
        return res