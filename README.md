# 🗺️ BLVD World AI Map Project

## 📖 Overview
This project applies **Artificial Intelligence search algorithms** to simulate a smart navigation system inside *Boulevard World* in Riyadh, Saudi Arabia.  
The goal is to design a robot or system capable of finding the best route between different areas, such as countries, restaurants, mosques, and facilities.

## 🧠 Algorithms Used
We implemented and compared three main search algorithms:
- **BFS (Breadth-First Search)** – Uninformed search strategy that finds the shortest path.
- **DFS (Depth-First Search)** – Uninformed search that explores paths deeply before backtracking.
- **A\*** – Informed search using heuristics to optimize pathfinding.

## 🗺️ Map Design
The map of *Boulevard World* was represented as a **graph**,  
where:
- Each **node** represents a location (e.g., USA, JAPAN, MOSQUE, RESTAURANT).
- Each **edge** represents a connection/path between two locations.
- Distances between nodes are based on approximate coordinates (x, y).

Files:
- `nodes.csv` → Contains all locations with coordinates and types.  
- `edges.csv` → Contains all paths and distances between locations.

## 🧩 How It Works
1. The program reads the map data from CSV files.  
2. It draws a visual map using **matplotlib**.  
3. The user can select a start and goal point.  
4. The algorithm finds and displays the best route.

## 📸 Example Output
- Visual map of Boulevard World with labeled zones.
- Highlighted route showing the AI’s chosen path.

## 👩‍💻 Team Members
- Rafah Aljabri 412206325@qu.edu.sa
- Kady
- Sahlah Alharbi
- Jory 

## 🏫 Supervised by
Dr.Alanoud Al-Suleiman
Qassim University — College of Science & Arts, Unaizah  

## 🧾 Course
**Artificial Intelligence (AI)** 

## ⚙️ Technologies
- Python  
- Matplotlib  
- CSV Data Files  
- Git & GitHub for version control

---

### 🏁 Project Goal
To simulate a **smart navigation robot** that can automatically plan and optimize routes in a complex environment using Artificial Intelligence.
