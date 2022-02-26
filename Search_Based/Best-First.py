import os
import sys
import math
import heapq
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Search_Based/")

import plotting, env
from Astar import AStar


class BestFirst(AStar):
    """BestFirst set the heuristics as the priority 
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
                       (self.heuristic(self.s_start), self.s_start))

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

                    # best first set the heuristics as the priority 
                    heapq.heappush(self.OPEN, (self.heuristic(s_n), s_n))

        return self.extract_path(self.PARENT), self.CLOSED


def main():
    s_start = (5,5)
    s_goal = (45,25)
    start_time = time.time()

    BF = BestFirst(s_start, s_goal, 'euclidean')
    plot = plotting.Plotting(s_start, s_goal)

    path, visited = BF.searching()
    end_time = time.time()
    print("Time spent =", end_time - start_time)
    visited = list(dict.fromkeys(visited))
    print("Number of explored nodes = ", len(visited))
    print("Number of traversed nodes =", len(path))
    plot.animation(path, visited, "Best-first Searching")  # animation


if __name__ == '__main__':
    main()