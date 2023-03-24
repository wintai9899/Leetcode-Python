#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (56.28%)
# Likes:    8111
# Dislikes: 1618
# Total Accepted:    420.3K
# Total Submissions: 746.8K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any
# order. Each task is done in one unit of time. For each unit of time, the CPU
# could complete either one task or just be idle.
# 
# However, there is a non-negative integer n that represents the cooldown
# period between two same tasks (the same letter in the array), that is that
# there must be at least n units of time between any two same tasks.
# 
# Return the least number of units of times that the CPU will take to finish
# all the given tasks.
# 
# 
# Example 1:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# 
# 
# Example 2:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# 
# 
# Example 3:
# 
# 
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle
# -> idle -> A
# 
# 
# 
# Constraints:
# 
# 
# 1 <= task.length <= 10^4
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].
# 
# 
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # no idle time
        if n == 0:
            return len(tasks)
        
        # eg. tasks = [A,A,A,B,B,C,C]
        # taskCount = {A : 3, B: 2, C: 2}
        taskCount = Counter(tasks)
        # maxHeap = {-3,-2,-2}
        maxHeap = [-cnt for cnt in taskCount.values()]
        heapq.heapify(maxHeap)
        # q = [(taskCount, idleTime)]
        q = collections.deque()

        time = 0 

        while maxHeap or q:
            time += 1
            # if there are still uncompleted tasks
            # +1 because its negative signed
            if maxHeap:
                taskCount = 1 + heapq.heappop(maxHeap)
                # not completed yet, add to queue
                if taskCount != 0:
                    # nextTaskTime = currentTime + idletime
                    nextTaskTime = time + n
                    q.append([taskCount, nextTaskTime])

            # cooldown time finished
            if q and q[0][1] == time:
                todo = q.popleft()[0]
                heapq.heappush(maxHeap, todo)
        
        return time
        

