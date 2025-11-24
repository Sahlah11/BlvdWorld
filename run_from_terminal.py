from algorithms_core import *
import time

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
    print("Invalid")
    exit()

time_taken = time.time() - t0
distance = compute_total_distance(path, graph_weighted)

print("\nRESULTS")
print("Path:", path)
print("Visited:", visited)
print("Distance:", distance)
print("Time:", round(time_taken, 4))