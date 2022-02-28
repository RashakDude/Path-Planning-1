import os
import sys
from collections import deque
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Search_Based/")

import plotting, env
from Astar import AStar
import math
import heapq

class BFS(AStar):
    """BFS add the new visited node in the end of the openset
    """
    def searching(self):
        """
        Breadth-first Searching.
        :return: path, visited order
        """

        self.PARENT[self.s_start] = self.s_start
        self.g[self.s_start] = 0
        self.g[self.s_goal] = math.inf
        heapq.heappush(self.OPEN,
                       (0, self.s_start))

        while self.OPEN:
            _, s = heapq.heappop(self.OPEN)
            self.CLOSED.append(s)

            if s == self.s_goal:
                break

            for s_n in self.get_neighbor(s):
                new_cost = self.g[s] + self.cost(s, s_n)

                if s_n not in self.g:
                    self.g[s_n] = math.inf

                if new_cost < self.g[s_n]:  # conditions for updating Cost
                    self.g[s_n] = new_cost
                    self.PARENT[s_n] = s

                    # bfs, add new node to the end of the openset
                    prior = self.OPEN[-1][0]+1 if len(self.OPEN)>0 else 0
                    heapq.heappush(self.OPEN, (prior, s_n))

        return self.extract_path(self.PARENT), self.CLOSED


def main():
    s_start = (5,5)
    s_goal = (30,20)
    start_time = time.time()

    bfs = BFS(s_start, s_goal, 'None')
    plot = plotting.Plotting(s_start, s_goal)

    path, visited = bfs.searching()
    end_time = time.time()
    print("Time spent =", end_time - start_time)

    visited = list(dict.fromkeys(visited))
    print("Number of explored nodes = ", len(visited))
    print("Number of traversed nodes =", len(path))
    print(path)
    # plot.animation(path, visited, "Breadth-first Searching (BFS)")


if __name__ == '__main__':
    main()
