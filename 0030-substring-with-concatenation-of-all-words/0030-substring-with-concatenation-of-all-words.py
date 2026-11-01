class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []
        for i in range(word_len):
            left = i
            current_count = Counter()
            words_used = 0
            for right in range(i, len(s) - word_len + 1, word_len):
                    sub = s[right : right + word_len]
                    
                    if sub in word_count:
                        current_count[sub] += 1
                        words_used += 1

                        while current_count[sub] > word_count[sub]:
                            left_sub = s[left : left + word_len]
                            current_count[left_sub] -= 1
                            words_used -= 1
                            left += word_len
                        if words_used == num_words:
                            result.append(left)
                    else:
                        current_count.clear()
                        words_used = 0
                        left = right + word_len
                    
        return result