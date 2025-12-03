import heapq
from collections import deque
from math import inf
import time

# =========================
# Load weighted graph (bidirectional)
# =========================
def load_weighted_graph(filename):
    graph = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            node, neighbors = line.split(":", 1)
            node = node.strip()
            graph.setdefault(node, {})
            for n in neighbors.split(","):
                n = n.strip()
                if not n:
                    continue
                parts = n.split()
                if len(parts) >= 2:
                    neighbor = parts[0].strip()
                    try:
                        dist = float(parts[1])
                    except:
                        continue
                else:
                    continue
                graph[node][neighbor] = dist
                # اجعل الرابط ثنائي الاتجاه
                if neighbor not in graph:
                    graph[neighbor] = {}
                if node not in graph[neighbor]:
                    graph[neighbor][node] = dist
    return graph

# =========================
# Load unweighted graph (bidirectional)
# =========================
def load_unweighted_graph(filename):
    weighted = load_weighted_graph(filename)
    return {node: list(neighbors.keys()) for node, neighbors in weighted.items()}

# =========================
# Compute total distance
# =========================
def compute_total_distance(path, weighted_graph):
    if not path or len(path) < 2:
        return 0.0
    total = 0.0
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        if a in weighted_graph and b in weighted_graph[a]:
            total += weighted_graph[a][b]
        elif b in weighted_graph and a in weighted_graph[b]:
            total += weighted_graph[b][a]
    return total

# =========================
# BFS
# =========================
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    visited_order = []

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        if current == goal:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent.get(node)
            path.reverse()
            return path, visited_order

        for neighbor in sorted(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return None, visited_order

# =========================
# DFS
# =========================
def dfs(graph, start, goal):
    stack = [start]
    visited = set([start])
    parent = {start: None}
    visited_order = []

    while stack:
        current = stack.pop()
        visited_order.append(current)

        if current == goal:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent.get(node)
            path.reverse()
            return path, visited_order

        for neighbor in sorted(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
    return None, visited_order

# =========================
# A* Algorithm
# =========================
def astar(graph, start, goal, heuristics):
    open_heap = []
    heapq.heappush(open_heap, (heuristics.get(start, 0), 0.0, start))
    g_score = {start: 0.0}
    came_from = {}
    closed_set = set()
    visited_order = []

    while open_heap:
        f_curr, g_curr, current = heapq.heappop(open_heap)
        if current in closed_set:
            continue
        closed_set.add(current)
        visited_order.append(current)

        if current == goal:
            path = []
            node = current
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            path.reverse()
            return path, visited_order

        for neighbor, weight in graph.get(current, {}).items():
            if neighbor in closed_set:
                continue
            tentative_g = g_curr + weight
            if tentative_g < g_score.get(neighbor, inf):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                f = tentative_g + heuristics.get(neighbor, 0)
                heapq.heappush(open_heap, (f, tentative_g, neighbor))

    return None, visited_order

# =========================
# Main
# =========================
if __name__== "__main__":
    FILE = "input_file.txt"

    graph_unweighted = load_unweighted_graph(FILE)
    graph_weighted = load_weighted_graph(FILE)
    nodes = list(graph_unweighted.keys())

    heuristics = {
        "Saudi_Arabia": 550, "Asia": 450, "USA": 380, "Turkey": 430,
        "France": 300, "Amazonia": 350, "China": 320, "Korea": 300,
        "Indonesia": 250, "Japan": 400, "Mexico": 370, "Pier": 340,
        "Iran": 310, "India": 290, "Egypt": 200, "Greece": 180,
        "Kuwait": 150, "Warzone": 140, "Levant": 230, "Morocco": 210,
        "Italy": 190, "The_Plant": 170
    }

    print("\nAvailable Places:")
    for i, node in enumerate(nodes):
        print(f"{i} = {node}")

    start_i = int(input("\nEnter start index: "))
    goal_i = int(input("Enter goal index: "))

    start = nodes[start_i]
    goal = nodes[goal_i]

    print("\n1 = BFS\n2 = DFS\n3 = A*\n")
    choice = input("Your choice: ").strip()

    t0 = time.time()
    if choice == "1":
        path, visited = bfs(graph_unweighted, start, goal)
    elif choice == "2":
        path, visited = dfs(graph_unweighted, start, goal)
    elif choice == "3":
        path, visited = astar(graph_weighted, start, goal, heuristics)
    else:
        print("Invalid choice")
        exit()
    t1 = time.time()
    time_taken = t1 - t0
    distance = compute_total_distance(path, graph_weighted)

    print("\nRESULTS")
    print("Path:", path)
    print("Visited:", visited)
    print("Distance:", distance)
    print(f"Time: {time_taken:.8f} seconds")