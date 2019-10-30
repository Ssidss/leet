"""
1029. Two City Scheduling
Easy
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

做差的排序
撈前半的[0]
後半的[1]
"""

def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    res = 0
    costs = sorted(costs,key = lambda x:x[0]-x[1])
    N = len(costs)//2
    c = 0
    for i in costs:
        if c < N:
            res += i[0]
            c+=1
        else:
            res += i[1]
    return res
