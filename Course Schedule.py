from collections import defaultdict as dd
from sys import setrecursionlimit as st
st(10**8)

class Solution:
    def cycle(self, tree, root, visited):
        if visited[root] == 2: return False
        if visited[root] == 1: return True
        visited[root] = 1
        for x in tree[root]:
            if visited[x] == 1:
                return True
            if visited[x] == 0 and self.cycle(tree, x, visited):
                return True
        visited[root] = 2
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = numCourses
        #n = len(prerequisites)
        edges = prerequisites
        tree = dd(list)
        for x, y in edges:
            tree[x].append(y)
        visited = [0] * course
        #processed = [0] * course
        for x in range(course):
            if self.cycle(tree, x, visited):
                #print(x)
                return False;
        return True;
