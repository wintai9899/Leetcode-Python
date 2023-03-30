#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Hard (41.22%)
# Likes:    4556
# Dislikes: 1644
# Total Accepted:    325.3K
# Total Submissions: 789K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight. Reconstruct
# the itinerary in order and return it.
# 
# All of the tickets belong to a man who departs from "JFK", thus, the
# itinerary must begin with "JFK". If there are multiple valid itineraries, you
# should return the itinerary that has the smallest lexical order when read as
# a single string.
# 
# 
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
# ["JFK", "LGB"].
# 
# 
# You may assume all tickets form at least one valid itinerary. You must use
# all the tickets once and only once.
# 
# 
# Example 1:
# 
# 
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# 
# 
# Example 2:
# 
# 
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi
# 
# 
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adjancency list
        graph = {src : [] for src,dest in tickets}
        # sort in lexical order
        tickets.sort()
        
        for src, dst in tickets:
            graph[src].append(dst)

        # always begin with JFK
        res = ["JFK"]

        def dfs(src):
            # base case: found solution
            if len(res) == len(tickets) + 1:
                return True

            # this src has no outgoing edges
            if src not in graph:
                return False

            # dfs on neighbors 
            # we want to modify the actual adj list
            temp = list(graph[src])
            for i, neigh in enumerate(temp):
                # remove from adj list
                graph[src].pop(i)
                res.append(neigh)

                # backtrack: to go back when we arrive at place with no outgoing edges
                # found 1 solution -> return True
                if dfs(neigh):
                    return True
                
                # clean up
                graph[src].insert(i,neigh)
                res.pop()
            return False
        dfs("JFK")
        return res
        
            
        
# @lc code=end

