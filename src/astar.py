import heapq
import math

def heuristic(a, b):
    (x1, y1), (x2, y2) = a, b
    return math.hypot(x2 - x1, y2 - y1)

def astar(graph, start, goal, positions):
    open_set = [(0, start)]
    g_score = {start: 0}
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1], g_score[goal]

        for neighbor, attrs in graph[current].items():
            tentative = g_score[current] + attrs['weight']
            if tentative < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score = tentative + heuristic(positions[current], positions[neighbor])
                heapq.heappush(open_set, (f_score, neighbor))
    return None, float('inf')
