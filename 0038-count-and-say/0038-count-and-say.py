class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current_sequence = "1"
        
        for _ in range(n - 1):
            next_sequence = []
            count = 1
            
            for index in range(len(current_sequence)):
                if index + 1 < len(current_sequence) and current_sequence[index] == current_sequence[index + 1]:
                    count += 1
                else:
                    next_sequence.append(str(count))
                    next_sequence.append(current_sequence[index])
                    count = 1
            
            current_sequence = "".join(next_sequence)
            
        return current_sequence  