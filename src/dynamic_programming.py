class SubstringMatch:
    def longestCommonSubstring(self, file1, file2):
        '''
        Function to find the longest common strand of bytes common in the 2 given files
        in O(mn) time complexity where m and n are the size of file1 and file2 respectively
        Params:
            - file1: the contents of the 1st file
            - file2: the contents of the 2nd file
        Returns:
            - length of the longest common strand present in file1 and file2
        '''
        m, n = len(file1), len(file2)
        maxLen, firstInd, secondInd = 0, 0, 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if(file1[i-1] == file2[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
                    if(dp[i][j] > maxLen):
                        maxLen = dp[i][j]
                        firstInd = i - maxLen
                        secondInd = j - maxLen
        return maxLen, firstInd, secondInd