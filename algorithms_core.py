import heapq
from collections import deque

# =========================
# A* Node Structure
# =========================
class NodeA:
    def __init__(self, position, cost=0, heuristic=0):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic
        self.parent = None

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


# =========================
# Load graph (Unweighted)
# =========================
def load_unweighted_graph(filename):
    graph = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue

            node, edges = line.split(":", 1)
            node = node.strip()
            edges = edges.strip()
            graph[node] = []

            for e in edges.split(","):
                e = e.strip()
                if not e:
                    continue
                neighbor = e.split()[0]
                graph[node].append(neighbor)
    return graph


# =========================
# Load graph (Weighted)
# =========================
def load_weighted_graph(filename):
    graph = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip() or ":" not in line:
                continue

            node, neighbors = line.split(":", 1)
            node = node.strip()
            graph[node] = {}

            for n in neighbors.split(","):
                n = n.strip()
                if not n:
                    continue

                parts = n.split()
                if len(parts) < 2:
                    continue

                neighbor = parts[0]
                try:
                    dist = float(parts[1])
                except:
                    continue

                graph[node][neighbor] = dist
    return graph


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
    visited_list = [start]
    parent = {start: None}

    while queue:
        at = queue.popleft()

        if at == goal:
            return reconstruct_path(parent, start, goal), visited_list

        for neighbor in graph.get(at, []):
            if neighbor not in visited:
                visited.add(neighbor)
                visited_list.append(neighbor)
                parent[neighbor] = at
                queue.append(neighbor)

    return None, visited_list


# =========================
# DFS
# =========================
def dfs(graph, start, goal):
    stack = [start]
    visited = set([start])
    visited_list = [start]
    parent = {start: None}

    while stack:
        at = stack.pop()

        if at == goal:
            return reconstruct_path(parent, start, goal), visited_list

        for neighbor in graph.get(at, []):
            if neighbor not in visited:
                visited.add(neighbor)
                visited_list.append(neighbor)
                parent[neighbor] = at
                stack.append(neighbor)

    return None, visited_list


# =========================
# A*
# =========================
def astar(graph, start, goal, heuristics):
    open_set = []
    heapq.heapify(open_set)

    closed_set = set()
    visited_list = [start]

    start_node = NodeA(start, 0, heuristics.get(start, 0))
    heapq.heappush(open_set, start_node)

    while open_set:
        current = heapq.heappop(open_set)

        if current.position == goal:
            path = []
            while current:
                path.insert(0, current.position)
                current = current.parent
            return path, visited_list

        closed_set.add(current.position)

        for neighbor, weight in graph.get(current.position, {}).items():
            if neighbor in closed_set:
                continue

            g = current.cost + weight
            h = heuristics.get(neighbor, 0)

            new_node = NodeA(neighbor, g, h)
            new_node.parent = current

            visited_list.append(neighbor)
            heapq.heappush(open_set, new_node)

    return None, visited_list


# =========================
# Path reconstruction
# =========================
def reconstruct_path(parent, start, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))