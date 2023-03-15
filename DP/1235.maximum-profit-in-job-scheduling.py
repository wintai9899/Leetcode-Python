#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]
        jobs = list(zip(startTime, endTime, profit))
        
        # sort iin nondecreasing order according to endTime 
        jobs.sort(key = lambda i : i[1])

        dp = [0] * (len(jobs))
        # initialize dp[0] with first job profit
        dp[0] = jobs[0][2]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1], jobs[i][2])

            for j in range(i-1,-1,-1):
                #  not overlapped
                if jobs[j][1] <= jobs[i][0]:
                    dp[i] = max(jobs[i][2] + dp[j], dp[i])
                    break 
        return max(dp)

        
# @lc code=end

