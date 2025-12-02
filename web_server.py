from flask import Flask, render_template, request
from algorithms_core import *
import time

app = Flask(__name__)

FILE = "input_file.txt"

# تحميل الرسوم
graph_un = load_unweighted_graph(FILE)
graph_w = load_weighted_graph(FILE)

# قيم الهيرستك
heuristics = {
    "Saudi_Arabia": 550, "Asia": 450, "USA": 380, "Turkey": 430,
    "France": 300, "Amazonia": 350, "China": 320, "Korea": 300,
    "Indonesia": 250, "Japan": 400, "Mexico": 370, "Pier": 340,
    "Iran": 310, "India": 290, "Egypt": 200, "Greece": 180,
    "Kuwait": 150, "Warzone": 140, "Levant": 230, "Morocco": 210,
    "Italy": 190, "The_Plant": 170
}

@app.route("/", methods=["GET", "POST"])
def home():

    nodes = list(graph_un.keys())

    path = []
    visited = []
    cost = 0.0
    expanded = 0
    time_taken = 0.0

    selected_start = None
    selected_goal = None
    selected_algo = None

    if request.method == "POST":

        start = request.form["start"]
        goal = request.form["goal"]
        algo = request.form["algorithm"]

        selected_start = start
        selected_goal = goal
        selected_algo = algo

        t1 = time.time()

        if algo == "BFS":
            path, visited = bfs(graph_un, start, goal)
        elif algo == "DFS":
            path, visited = dfs(graph_un, start, goal)
        elif algo == "Astar":
            path, visited = astar(graph_w, start, goal, heuristics)
        else:
            path, visited = [], []

        t2 = time.time()
        time_taken = round(t2 - t1, 8)  # دقة أعلى للوقت

        if path:
            cost = compute_total_distance(path, graph_w)
        expanded = len(visited)

    return render_template(
        "index.html",
        nodes=nodes,
        path=path,
        visited=visited,
        cost=cost,
        expanded=expanded,
        time_taken=time_taken,
        selected_start=selected_start,
        selected_goal=selected_goal,
        selected_algo=selected_algo
    )

if __name__ == "__main__":
    app.run(debug=True)