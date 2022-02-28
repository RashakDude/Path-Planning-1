import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fontP = FontProperties()
fontP.set_size('xx-small')

dfs_path = [(30, 20), (30, 19), (29, 18), (28, 17), (27, 16), (26, 15), (25, 14), (24, 14), (23, 14), (22, 14), (21, 14), (20, 13), (20, 12), (21, 11), (22, 12), (23, 11), (24, 12), (25, 11), (26, 12), (27, 13), (28, 14), (29, 15), (30, 16), (31, 17), (32, 18), (33, 19), (34, 20), (35, 21), (36, 22), (37, 21), (38, 20), (37, 19), (36, 18), (35, 17), (34, 16), (33, 15), (32, 14), (31, 13), (30, 12), (29, 11), (29, 10), (28, 9), (27, 9), (26, 9), (25, 9), (24, 9), (23, 9), (22, 9), (21, 9), (20, 9), (19, 9), (18, 9), (17, 9), (16, 9), (15, 8), (15, 7), (16, 6), (17, 7), (18, 6), (19, 7), (20, 6), (21, 7), (22, 6), (23, 7), (24, 6), (25, 7), (26, 6), (27, 7), (28, 6), (29, 7), (30, 6), (31, 7), (32, 6), (33, 5), (32, 4), (31, 4), (30, 4), (29, 4), (28, 4), (27, 4), (26, 4), (25, 4), (24, 4), (23, 4), (22, 4), (21, 4), (20, 4), (19, 4), (18, 4), (17, 4), (16, 4), (15, 4), (14, 4), (13, 4), (12, 4), (11, 4), (10, 3), (10, 2), (11, 1), (12, 2), (13, 1), (14, 2), (15, 1), (16, 2), (17, 1), (18, 2), (19, 1), (20, 2), (21, 1), (22, 2), (23, 1), (24, 2), (25, 1), (26, 2), (27, 1), (28, 2), (29, 1), (30, 2), (31, 1), (32, 2), (33, 1), (34, 2), (35, 3), (36, 4), (36, 5), (36, 6), (35, 7), (34, 8), (33, 9), (32, 10), (33, 11), (34, 12), (35, 13), (36, 14), (37, 15), (38, 16), (39, 17), (40, 18), (41, 19), (41, 20), (41, 21), (40, 22), (39, 23), (38, 24), (37, 25), (36, 26), (35, 26), (34, 26), (33, 26), (32, 26), (31, 26), (30, 26), (29, 26), (28, 26), (27, 26), (26, 26), (25, 26), (24, 26), (23, 26), (22, 26), (21, 26), (20, 26), (19, 26), (18, 25), (17, 24), (16, 23), (15, 22), (14, 21), (14, 20), (14, 19), (14, 18), (13, 17), (12, 16), (11, 15), (11, 14), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 16), (18, 15), (17, 14), (16, 13), (15, 12), (14, 11), (13, 10), (12, 9), (11, 8), (10, 7), (9, 6), (8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
bfs_path = [(30, 20), (29, 19), (29, 18), (29, 17), (29, 16), (29, 15), (29, 14), (29, 13), (29, 12), (29, 11), (29, 10), (29, 9), (30, 8), (31, 7), (32, 6), (33, 5), (34, 4), (35, 4), (36, 4), (37, 5), (37, 6), (37, 7), (38, 8), (38, 9), (39, 10), (39, 11), (39, 12), (40, 13), (40, 14), (41, 15), (41, 16), (41, 17), (41, 18), (41, 19), (41, 20), (41, 21), (40, 22), (39, 23), (38, 24), (37, 25), (36, 26), (35, 26), (34, 26), (33, 26), (32, 26), (31, 26), (30, 26), (29, 26), (28, 26), (27, 26), (26, 26), (25, 26), (24, 26), (23, 26), (22, 26), (21, 26), (20, 26), (19, 26), (18, 25), (17, 24), (16, 23), (15, 22), (14, 21), (13, 20), (12, 19), (11, 18), (11, 17), (11, 16), (11, 15), (11, 14), (10, 13), (9, 12), (8, 11), (7, 10), (7, 9), (7, 8), (6, 7), (5, 6), (5, 5)]
best_first_path = [(30, 20), (30, 19), (30, 18), (30, 17), (30, 16), (30, 15), (30, 14), (30, 13), (30, 12), (29, 11), (29, 10), (29, 9), (30, 8), (31, 7), (32, 6), (33, 5), (34, 4), (35, 4), (36, 4), (36, 5), (36, 6), (36, 7), (36, 8), (36, 9), (36, 10), (36, 11), (36, 12), (36, 13), (36, 14), (37, 15), (38, 16), (39, 17), (40, 18), (41, 19), (41, 20), (41, 21), (40, 22), (39, 23), (38, 24), (37, 25), (36, 26), (35, 26), (34, 26), (33, 26), (32, 26), (31, 26), (30, 26), (29, 26), (28, 26), (27, 26), (26, 26), (25, 26), (24, 26), (23, 26), (22, 26), (21, 26), (20, 26), (19, 26), (18, 25), (17, 24), (16, 23), (15, 22), (14, 21), (14, 20), (14, 19), (14, 18), (14, 17), (14, 16), (14, 15), (14, 14), (13, 13), (12, 12), (11, 11), (10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (5, 5)]
dijkstra_path = [(30, 20), (29, 19), (29, 18), (29, 17), (29, 16), (29, 15), (29, 14), (29, 13), (29, 12), (29, 11), (29, 10), (29, 9), (30, 8), (31, 7), (32, 6), (33, 5), (34, 4), (35, 4), (36, 4), (37, 5), (38, 6), (39, 7), (39, 8), (39, 9), (39, 10), (39, 11), (40, 12), (41, 13), (41, 14), (41, 15), (41, 16), (41, 17), (41, 18), (41, 19), (41, 20), (41, 21), (40, 22), (39, 23), (38, 24), (37, 25), (36, 26), (35, 26), (34, 26), (33, 26), (32, 26), (31, 26), (30, 26), (29, 26), (28, 26), (27, 26), (26, 26), (25, 26), (24, 26), (23, 26), (22, 26), (21, 26), (20, 26), (19, 26), (18, 25), (17, 24), (16, 23), (15, 22), (14, 21), (13, 20), (12, 19), (11, 18), (11, 17), (11, 16), (11, 15), (11, 14), (10, 13), (9, 12), (8, 11), (7, 10), (6, 9), (5, 8), (5, 7), (5, 6), (5, 5)]
astar_path = [(30, 20), (29, 19), (29, 18), (29, 17), (29, 16), (29, 15), (29, 14), (29, 13), (29, 12), (29, 11), (29, 10), (29, 9), (30, 8), (31, 7), (32, 6), (33, 5), (34, 4), (35, 4), (36, 4), (37, 5), (37, 6), (37, 7), (37, 8), (37, 9), (37, 10), (37, 11), (37, 12), (37, 13), (37, 14), (37, 15), (38, 16), (39, 17), (40, 18), (41, 19), (41, 20), (41, 21), (40, 22), (39, 23), (38, 24), (37, 25), (36, 26), (35, 26), (34, 26), (33, 26), (32, 26), (31, 26), (30, 26), (29, 26), (28, 26), (27, 26), (26, 26), (25, 26), (24, 26), (23, 26), (22, 26), (21, 26), (20, 26), (19, 26), (18, 25), (17, 24), (16, 23), (15, 22), (14, 21), (14, 20), (14, 19), (14, 18), (14, 17), (14, 16), (14, 15), (14, 14), (13, 13), (12, 12), (11, 11), (10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (5, 5)]
biastar_path = [(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19), (14, 20), (14, 21), (15, 22), (16, 23), (17, 24), (18, 25), (19, 26), (20, 26), (21, 26), (22, 26), (23, 26), (24, 26), (25, 26), (26, 26), (27, 26), (28, 26), (29, 26), (30, 26), (31, 26), (32, 26), (33, 26), (34, 26), (35, 26), (36, 26), (37, 25), (38, 24), (39, 23), (40, 22), (41, 21), (41, 20), (41, 19), (40, 18), (39, 17), (38, 16), (37, 15), (37, 14), (37, 13), (37, 12), (37, 11), (37, 10), (37, 9), (37, 8), (37, 7), (37, 6), (37, 5), (36, 4), (35, 4), (34, 4), (33, 5), (32, 6), (31, 7), (30, 8), (29, 9), (29, 10), (29, 11), (29, 12), (29, 13), (29, 14), (29, 15), (29, 16), (29, 17), (29, 18), (29, 19), (30, 20)]
lrtastar_100_path = [[(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (16, 17)], [(16, 17), (15, 18), (14, 19), (13, 20), (12, 21), (11, 22)], [(11, 22), (12, 21), (13, 20)], [(13, 20), (14, 21), (15, 22), (16, 23), (17, 24), (18, 25), (19, 26), (20, 27), (21, 28), (22, 29), (23, 29), (24, 29), (25, 29)], [(25, 29), (26, 28), (27, 27), (28, 26), (29, 26), (30, 26), (31, 26), (32, 26), (33, 26), (34, 26), (35, 26), (36, 25), (35, 24)], [(35, 24), (34, 23), (33, 22), (32, 21), (31, 20), (30, 20)]]
lrtastar_250_path = [[(5, 5), (4, 4), (3, 3), (3, 2), (3, 1)], [(3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6), (9, 7), (10, 8), (11, 9), (12, 10), (13, 11), (14, 12), (15, 13), (16, 14), (17, 15), (18, 16)], [(18, 16), (19, 17)], [(19, 17), (20, 17), (21, 17), (22, 17), (23, 18), (24, 19), (25, 20), (26, 20), (27, 20), (28, 20), (29, 20), (30, 20)]]
lrtastar_500_path = [[(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19), (14, 20), (15, 21), (16, 20)], [(16, 20), (17, 20), (18, 20), (19, 20), (20, 20), (21, 20), (22, 20), (23, 20), (24, 20), (25, 20), (26, 20), (27, 20), (28, 20), (29, 20), (30, 20)]]

x1 = [0]*len(dfs_path)
y1 = [0]*len(dfs_path)
for i in range(len(dfs_path)):
    x1[i] = dfs_path[i][0]
    y1[i] = dfs_path[i][1]

x2 = [0]*len(bfs_path)
y2 = [0]*len(bfs_path)
for i in range(len(bfs_path)):
    x2[i] = bfs_path[i][0]
    y2[i] = bfs_path[i][1]

x3 = [0]*len(best_first_path)
y3 = [0]*len(best_first_path)
for i in range(len(best_first_path)):
    x3[i] = best_first_path[i][0]
    y3[i] = best_first_path[i][1]

x4 = [0]*len(dijkstra_path)
y4 = [0]*len(dijkstra_path)
for i in range(len(dijkstra_path)):
    x4[i] = dijkstra_path[i][0]
    y4[i] = dijkstra_path[i][1]

x5 = [0]*len(astar_path)
y5 = [0]*len(astar_path)
for i in range(len(astar_path)):
    x5[i] = astar_path[i][0]
    y5[i] = astar_path[i][1]

x6 = [0]*len(biastar_path)
y6 = [0]*len(biastar_path)
for i in range(len(biastar_path)):
    x6[i] = biastar_path[i][0]
    y6[i] = biastar_path[i][1]

x7 = [0]*len(lrtastar_100_path)
y7 = [0]*len(lrtastar_100_path)
for i in range(len(lrtastar_100_path)):
    x7[i] = lrtastar_100_path[i][0]
    y7[i] = lrtastar_100_path[i][1]

x8 = [0]*len(lrtastar_250_path)
y8 = [0]*len(lrtastar_250_path)
for i in range(len(lrtastar_250_path)):
    x8[i] = lrtastar_250_path[i][0]
    y8[i] = lrtastar_250_path[i][1]

x9 = [0]*len(lrtastar_500_path)
y9 = [0]*len(lrtastar_500_path)
for i in range(len(lrtastar_500_path)):
    x9[i] = lrtastar_500_path[i][0]
    y9[i] = lrtastar_500_path[i][1]

plt.plot(x1,y1,'-')
plt.plot(x2,y2,'--')
plt.plot(x3,y3,'-.')
plt.plot(x4,y4,':')
plt.plot(x5,y5,'-')
plt.plot(x6,y6,'--')
plt.plot(x7,y7,'-.')
plt.plot(x8,y8,':')
plt.plot(x9,y9,'-')
plt.plot(5,5,'or')
plt.plot(30,20,'og')

plt.legend(["Depth-First", "Breadth-First", "Best-First", "Dijkstra's", "Astar", 
"Bidirectional-A*", "LRT-A* N = 100", "LRT-A* N = 250", "LRT-A* N = 500"], loc='upper left', prop=fontP)

plt.show()