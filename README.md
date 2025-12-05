## 🗺️ BLVD World AI Pathfinding Project

## 📌 Overview
This project applies **Artificial Intelligence search algorithms** to simulate a smart navigation system inside *Boulevard World* in Riyadh.  
The system identifies the best path between two locations using BFS, DFS, and A* search.

The project includes:
- A fully designed **graph** representing BLVD World.
- A **web application (Flask)** to visualize and test algorithms.
- A comparison of algorithms based on path, cost, nodes expanded, and execution time.

---

## 🧠 Algorithms Implemented
### 1. **BFS – Breadth First Search**
- Uninformed search  
- Finds shallowest path  
- Ignores weights  

### 2. **DFS – Depth First Search**
- Uninformed search  
- Explores deep paths first  
- May produce longer routes  

### 3. **A\* Search**
- Informed search  
- Uses **heuristic values** assigned to each node  
- Produces the **optimal** path with minimum total distance  

---

## 🗺️ Graph Design
Boulevard World was modeled as a **graph**, where:

- Each **node** represents a zone (e.g., *Saudi_Arabia, Japan, Egypt*)
- Each **edge** represents a valid connection between two zones
- Distances are **approximate**, based on the map layout
- The graph is stored inside `input_file.txt`

---

## 🌐 Web Application (Flask)
A simple, beautiful web interface was built using **Flask**, allowing users to:

- Select **start** and **goal** nodes
- Choose **BFS, DFS, or A\***
- Display:
  - Path  
  - Total cost  
  - Nodes expanded  
  - Execution time  

The interface includes the original BLVD World map for reference.

Main file:
web/Boulevard.py

Templates:
web/templates/index.html

Static images:
web/static/images/Map.png

---

## 👩‍💻 Team Members
- **Rafah Aljabri 412206325@qu.edu.sa**
- **Kady Aldkhil  431201766@qu.edu.sa**  
- **Sahlah Alharbi 422215279@qu.edu.sa**  
- **jory Aljmal 412205540@qu.edu.sa**

## 🏫 Instructor
**Dr. Alanoud Al-Suleiman**  
Qassim University — College of Sciences & Arts, Unaizah  

---

## 🧾 Course
**Artificial Intelligence – CS471**  

