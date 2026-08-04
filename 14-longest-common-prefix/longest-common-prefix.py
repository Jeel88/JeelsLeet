class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        ans = ""

        # Go through each character of the first word
        for i in range(len(strs[0])):

            ch = strs[0][i]

            # Compare with every other word
            for word in strs[1:]:

                # If index is out of range or characters don't match
                if i >= len(word) or word[i] != ch:
                    return ans

            # Character matched in all words
            ans += ch

        return ans