class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        max_length = 0
        word_length = len(word)

        for i in range(word_length):
            for j in range(i+1, word_length+1):
                substring = word[i:j]
                if substring in forbidden:
                    break
                if len(substring) > max_length:
                    max_length = len(substring)

        return max_length
word = "word"
forbidden = ["for", "bid", "den"]
solution = Solution()
result = solution.longestValidSubstring(word, forbidden)
print(result)
