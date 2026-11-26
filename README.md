# Pract1-DAA-
Summary of Pract1:
                From this practicals i have a gained a information about the various sorting algorithms,i have used the PYTHON as my Programming Language
                      1.Bubble Sort
                      2.Insertion Sort
                      3.Selection Sort 
                      4.Merge Sort
                      5.Quick Sort
                My faculty helped me out the errors throught the practicals ,Sorting the numbers depends on the following factors as Data set size,Memory usage,Data                           order & Performance requirements.
Conclusion:    
           Learning of Sorting Algorithms.
                     1.Bubble Sort
                     2.Insertion Sort
                     3.Selection Sort 
                     4.Merge Sort
                     5.Quick Sort





                                                                # Pract2-DAA
# Summary of pract2:
               From this practicals i have learned about the various Searching Algorithms,which are efficiently used for Searching the particular elements in the given Array.
                     1.Linear Search Algorithms
                     2.Binary Search Algorithms
               My faculty helped me out the errors throught the practicals , There are some kind of Limitations for both the searching Algorithms but these are the widely                    used Data Structure Algorithms 
Conclusion:  
            Learning of the Searching Algorithms. 
               1.Linear Search Algorithms
               2.Binary Search Algorithms




                                                         #Pract3-DAA

# SUMMARY OF PRACTICAL 3: 
In practica 3 we learn about heap sort In that we learn about MAX and MIN heap sort also HEAP SORT:Heap sort is a sorting algorithm that uses a heap data structure to arrange elements in ascending or descending order. MAX HEAP:A Max Heap is a complete binary tree where the parent node is greater than or equal to its children. MIN HEAP:A Min Heap is a complete binary tree where the parent node is smaller than or equal to its children. Ascending order use a Max Heap. Descending order use a Min Heap.
CONCLUSION:
Heap sorting is a simple and efficient sorting method that uses a heap data structure. It arranges the elements in the required order by repeatedly selecting the largest or smallest element. Max Heap is used for ascending order, and Min Heap is used for descending order.



# SUMMARY OF PRACT-4:

In this practical, we learned how to find the factorial of a number using two different methods: iterative and recursive. In the iterative method, we use a loop to multiply the numbers from 1 to the given number. In the recursive method, the function calls itself with a smaller value until it reaches the base condition. Both methods give the same factorial result, but they work in different ways.

CONCLUSION:

From this practical, we understood the difference between iterative and recursive approaches for solving a problem. Both methods are useful for calculating factorials, and this practical helped us understand how loops and recursion can be used to solve the same problem.



# Pract7-DAA
SUMAMRY OF PRACT-7:

The Coin Change Problem is solved using Dynamic Programming to find the minimum number of coins needed to make a given amount. The program takes the number of coins, coin values, and target amount as input from the user. It creates a dynamic programming table where each position stores the minimum number of coins required to form that particular amount. The program checks all available coins and updates the table with the best possible solution. If the amount cannot be formed using the given coins, the program returns -1. The algorithm has a time complexity of O(n × amount) and a space complexity of O(amount).

CONCULSION:

Dynamic Programming makes the Coin Change Problem easier and faster to solve. The program gives the minimum number of coins or returns -1 if the amount cannot be made.

# PRACT5-(DAA)
SUMMARY :

The 0/1 Knapsack problem uses dynamic programming to find the maximum value that can be placed in a knapsack without exceeding its capacity. The program accepts the number of items, weights, values, and capacity from the user and calculates the maximum possible value. Its time complexity is O(n × W), space complexity is O(n × W), and the actual execution time is measured using time.perf_counter().

CONCLUSION:

The 0/1 Knapsack problem is efficiently solved using dynamic programming to maximize the total value within the given capacity. The program accepts user input and calculates the optimal solution while measuring its execution time. The algorithm has a time complexity of O(n × W), making it suitable for solving moderate-sized knapsack problems.

# PRACT6-(DAA)
SUMMARY :

Chain Matrix Multiplication using Dynamic Programming finds the optimal order of multiplying matrices to minimize the total number of scalar multiplications. The algorithm stores intermediate results in a dynamic programming table and efficiently determines the minimum multiplication cost. It has a time complexity of O(n³) and a space complexity of O(n²), with execution time measured using Python’s time.perf_counter().

CONCLUSION:

Chain Matrix Multiplication using Dynamic Programming efficiently finds the best order of matrix multiplication with minimum computation cost. It reduces unnecessary calculations by storing previously solved subproblems. The method is efficient, systematic, and has a time complexity of O(n³).

# PRACT8-(DAA)
SUMMARY :

Graph traversal is an important technique used to visit all the vertices of a graph systematically. DFS explores a graph deeply by visiting a vertex and then recursively visiting its unvisited neighbors. BFS explores the graph level by level using a queue data structure. Both DFS and BFS have a time complexity of O(V + E), where V is the number of vertices and E is the number of edges. These searching techniques are widely used in path finding, network analysis, and many other computer science applications.

CONCLUSION :

The graph traversal program successfully implements both DFS and BFS searching techniques using Python. DFS uses a depth-based approach, while BFS visits vertices level by level. Both methods efficiently traverse the vertices and edges of a graph. The program accepts user input, making it flexible for different graph structures and starting vertices. Thus, DFS and BFS are useful and fundamental techniques for solving various graph-based problems.

# Practical 9: Prim's Algorithm (Greedy Minimum Spanning Tree)
This directory contains the Python implementation of Prim's Algorithm for finding the Minimum Spanning Tree (MST) of a connected, undirected, edge-weighted graph using a Min-Heap (Priority Queue).

📌 Problem Overview & Paradigm
Given a connected, undirected graph 
G
=
(
V
,
E
)
 with non-negative edge weights, a Minimum Spanning Tree (MST) is a subset of edges that connects all 
V
 vertices without any cycles while minimizing the total edge weight.

Method Implemented
Prim's Algorithm (prims_mst(graph, start_vertex))
Starts at an arbitrary seed vertex 
s
 and grows the MST incrementally.
At each step, greedily selects the minimum weight edge 
(
u
,
v
)
 connecting a vertex 
u
 in the tree to a vertex 
v
 outside the tree.
Greedy Choice Property: A locally optimal choice of the minimum cut edge yields a globally optimal MST.
Time Complexity: 
O
(
E
log
⁡
V
)
 using Min-Heap priority queue.
Space Complexity: 
O
(
V
+
E
)
 for adjacency list and heap storage.
⚡ Complexity Summary
Approach	Best Case	Average Case	Worst Case	Auxiliary Space	Paradigm	Guarantees Optimality?
Prim's (Min-Heap)	
O
(
E
log
⁡
V
)
O
(
E
log
⁡
V
)
O
(
E
log
⁡
V
)
O
(
V
+
E
)
Greedy Paradigm	✅ Yes (Always Optimal)
💻 How to Run
Open your terminal or command prompt.
Navigate to the practical_9 directory:
cd practical_9
Execute the Python script:
python prims_algorithm.py
📋 Sample Output
==================================================
        PRIM'S MINIMUM SPANNING TREE (MST)         
==================================================
Default Graph Adjacency List:
  Node 0 -> Node 1 (weight 2), Node 3 (weight 3)
  Node 1 -> Node 0 (weight 2), Node 2 (weight 3), Node 4 (weight 8)
  Node 2 -> Node 1 (weight 3), Node 3 (weight 7), Node 4 (weight 6)
  Node 3 -> Node 0 (weight 3), Node 2 (weight 7), Node 4 (weight 1)
  Node 4 -> Node 1 (weight 8), Node 2 (weight 6), Node 3 (weight 1)

Use custom input? (y/N): n

--- Running Prim's Algorithm ---

========== MINIMUM SPANNING TREE EDGES ==========
Step   | Edge (u -> v)   | Weight    
--------------------------------------
1      | 0 -- 1          | 2         
2      | 1 -- 2          | 3         
3      | 0 -- 3          | 3         
4      | 3 -- 4          | 1         
--------------------------------------

========== RESULTS SUMMARY ==========
Total Vertices (V)    : 5
MST Edge Count        : 4
Total MST Weight      : 9
Execution Time        : 14200.00 ns
======================================
📖 Key Takeaways & Conclusion
Greedy Spanning Tree Construction:
Prim's algorithm operates on vertices, making it ideal for dense graphs (
E
≈
V
2
).
Min-Heap Efficiency:
Using heapq reduces edge extraction cost from 
O
(
V
)
 to 
O
(
log
⁡
V
)
, enabling fast scale to large graphs.
# Practical 10: Kruskal's Algorithm (Greedy Minimum Spanning Tree)
This directory contains the Python implementation of Kruskal's Algorithm for finding the Minimum Spanning Tree (MST) of a connected, undirected, edge-weighted graph using Disjoint Set Union (DSU) with Path Compression and Union by Rank.

📌 Problem Overview & Paradigm
Given a connected graph 
G
=
(
V
,
E
)
, Kruskal's algorithm constructs a Minimum Spanning Tree by sorting all graph edges in non-decreasing order of weight and greedily adding edges that do not form a cycle.

Method Implemented
Kruskal's Algorithm with DSU (kruskals_mst(num_vertices, edges))
Sorts all edges in non-decreasing order: 
O
(
E
log
⁡
E
)
.
Uses Disjoint Set Union (DSU) to test if adding an edge forms a cycle:
find(u): Path compression flattens tree height to nearly 
O
(
1
)
.
union(u, v): Union by rank attaches smaller tree under root of larger tree.
Time Complexity: 
O
(
E
log
⁡
E
)
 or 
O
(
E
log
⁡
V
)
.
Space Complexity: 
O
(
V
+
E
)
 for DSU parent/rank arrays and edge lists.
⚡ Complexity Summary
Approach	Best Case	Average Case	Worst Case	Auxiliary Space	Paradigm	Guarantees Optimality?
Kruskal's (DSU)	
O
(
E
log
⁡
E
)
O
(
E
log
⁡
E
)
O
(
E
log
⁡
E
)
O
(
V
+
E
)
Greedy Paradigm	✅ Yes (Always Optimal)
💻 How to Run
Open your terminal or command prompt.
Navigate to the practical_10 directory:
cd practical_10
Execute the Python script:
python kruskals_algorithm.py
📋 Sample Output
==================================================
      KRUSKAL'S MINIMUM SPANNING TREE (MST)       
==================================================
Default Graph Edges:
  Edge (0 -- 1) with weight 4
  Edge (0 -- 2) with weight 4
  Edge (1 -- 2) with weight 2
  Edge (1 -- 3) with weight 6
  Edge (2 -- 3) with weight 8
  Edge (2 -- 4) with weight 9
  Edge (3 -- 4) with weight 7
  Edge (3 -- 5) with weight 5
  Edge (4 -- 5) with weight 10

Use custom input? (y/N): n

--- Running Kruskal's Algorithm ---

========== SELECTED MST EDGES ==========
Step   | Edge (u -- v)   | Weight    
--------------------------------------
1      | 1 -- 2          | 2         
2      | 0 -- 1          | 4         
3      | 3 -- 5          | 5         
4      | 1 -- 3          | 6         
5      | 3 -- 4          | 7         
--------------------------------------

========== RESULTS SUMMARY ==========
Total Vertices (V)    : 6
Total Graph Edges (E) : 9
MST Edges Selected    : 5
Edges Skipped (Cycles): 4
Total MST Weight      : 24
Execution Time        : 18100.00 ns
======================================
📖 Key Takeaways & Conclusion
Edge-Centric Greedy Strategy:
Unlike Prim's algorithm which grows a connected tree from a vertex, Kruskal's algorithm processes global edges and works exceptionally well on sparse graphs (
E
≪
V
2
).
Nearly Constant DSU Operations:
With path compression and union by rank, DSU operations run in 
O
(
α
(
V
)
)
 time per operation (where 
α
 is the Inverse Ackermann function, effectively 
≤
4
).
# Practical 11: Floyd-Warshall Algorithm (All-Pairs Shortest Path)
This directory contains the Python implementation of the Floyd-Warshall Algorithm for finding All-Pairs Shortest Paths in a directed, weighted graph using Dynamic Programming.

📌 Problem Overview & Paradigm
Given a directed weighted graph 
G
=
(
V
,
E
)
 represented as an adjacency matrix, compute the shortest path distances between every pair of vertices 
i
,
j
∈
V
.

Method Implemented
Floyd-Warshall Tabulation (floyd_warshall(graph))
Maintains a 2D distance matrix 
d
i
s
t
[
i
]
[
j
]
 and a predecessor matrix 
n
e
x
t
n
o
d
e
[
i
]
[
j
]
.
Iterates through all possible intermediate vertices 
k
∈
0
,
1
,
…
,
V
−
1
 and updates paths:
Recurrence Relation: 
D
(
k
)
[
i
]
[
j
]
=
min
(
D
(
k
−
1
)
[
i
]
[
j
]
,
;
D
(
k
−
1
)
[
i
]
[
k
]
+
D
(
k
−
1
)
[
k
]
[
j
]
)
Time Complexity: 
O
(
V
3
)
 (three nested loops over vertices).
Space Complexity: 
O
(
V
2
)
 for intermediate matrices.
⚡ Complexity Summary
Approach	Best Case	Average Case	Worst Case	Auxiliary Space	Paradigm	Guarantees Optimality?
Floyd-Warshall (DP)	
O
(
V
3
)
O
(
V
3
)
O
(
V
3
)
O
(
V
2
)
Dynamic Programming	✅ Yes (Detects negative cycles)
💻 How to Run
Open your terminal or command prompt.
Navigate to the practical_11 directory:
cd practical_11
Execute the Python script:
python floyd_warshall.py
📋 Sample Output
==================================================
      FLOYD-WARSHALL ALL-PAIRS SHORTEST PATH      
==================================================
Default Graph Adjacency Weight Matrix:

========== ALL-PAIRS SHORTEST DISTANCE MATRIX ==========
From\To Node    0   Node    1   Node    2   Node    3
-----------------------------------------------------
Node 0          0          3        INF          7
Node 1          8          0          2        INF
Node 2          5        INF          0          1
Node 3          2        INF        INF          0
-----------------------------------------------------

Use custom input? (y/N): n

--- Running Floyd-Warshall Dynamic Programming Solver ---

========== ALL-PAIRS SHORTEST DISTANCE MATRIX ==========
From\To Node    0   Node    1   Node    2   Node    3
-----------------------------------------------------
Node 0          0          3          5          6
Node 1          5          0          2          3
Node 2          3          6          0          1
Node 3          2          5          7          0
-----------------------------------------------------

========== SAMPLE PATH RECONSTRUCTIONS ==========
Source   -> Target   | Cost   | Path                
------------------------------------------------
Node 0   -> Node 1   | 3      | 0 -> 1              
Node 0   -> Node 2   | 5      | 0 -> 1 -> 2         
Node 0   -> Node 3   | 6      | 0 -> 1 -> 2 -> 3    
...

========== RESULTS SUMMARY ==========
Total Vertices (V)    : 4
Execution Time        : 19800.00 ns
======================================
📖 Key Takeaways & Conclusion
All-Pairs Distance Matrix:
Unlike Dijkstra's or Bellman-Ford algorithms which compute single-source shortest paths, Floyd-Warshall computes shortest paths between all pairs of nodes simultaneously in 
O
(
V
3
)
 time.
Dense Graph Suitability:
Highly effective for dense graphs (
E
≈
V
2
) where running Dijkstra 
V
 times would take 
O
(
V
E
log
⁡
V
)
≈
O
(
V
3
log
⁡
V
)
.
# Practical 12: Travelling Salesman Problem (Dynamic Programming - Held-Karp Algorithm)
This directory contains the Python implementation of the Travelling Salesman Problem (TSP) solved using the Held-Karp Dynamic Programming algorithm with Bitmask State Representation, alongside a comparison against the naive Brute-Force Permutation method.

📌 Problem Overview & Paradigm
Given a set of 
N
 cities and pairwise distances 
d
(
i
,
j
)
 between them, find the minimum cost tour that starts at a designated origin city (e.g., City 0), visits every other city exactly once, and returns to the origin city.

Methods Implemented
Held-Karp Dynamic Programming (tsp_held_karp(matrix))

Uses bitmasks to represent subsets of visited cities. State is defined as 
(
S
,
u
)
, representing the minimum cost to complete the tour starting at city 
u
 having visited city subset 
S
.
Recurrence Relation: 
g
(
S
,
u
)
=
min
v
∉
S
(
d
(
u
,
v
)
+
g
(
S
∪
v
,
v
)
)
Base Case: 
g
(
All Cities
,
u
)
=
d
(
u
,
0
)
 (return cost to start city 0).
Time Complexity: 
O
(
N
2
⋅
2
N
)
Space Complexity: 
O
(
N
⋅
2
N
)
Brute-Force Permutations (tsp_brute_force(matrix))

Generates all 
(
N
−
1
)
!
 possible tour permutations.
Time Complexity: 
O
(
N
!
)
Space Complexity: 
O
(
N
)
⚡ Complexity Summary
Approach	Best Case	Average Case	Worst Case	Auxiliary Space	Paradigm	Guarantees Optimality?
Held-Karp DP	
O
(
N
2
⋅
2
N
)
O
(
N
2
⋅
2
N
)
O
(
N
2
⋅
2
N
)
O
(
N
⋅
2
N
)
Dynamic Programming (Bitmask)	✅ Yes (Always Optimal)
Brute-Force	
O
(
N
!
)
O
(
N
!
)
O
(
N
!
)
O
(
N
)
Exhaustive Search	✅ Yes (Always Optimal)
💻 How to Run
Open your terminal or command prompt.
Navigate to the practical_12 directory:
cd practical_12
Execute the Python script:
python travelling_salesman.py
📋 Sample Output
==================================================
   TRAVELLING SALESMAN PROBLEM (HELD-KARP DP)    
==================================================
Default Distance Matrix (4 Cities):
From\To     City 0    City 1    City 2    City 3
--------------------------------------------------
City 0           0        10        15        20
City 1          10         0        35        25
City 2          15        35         0        30
City 3          20        25        30         0
--------------------------------------------------

Use custom input? (y/N): n

--- Running Dynamic Programming (Held-Karp) Solver ---
--- Running Brute-Force Permutation Solver ---

========== OPTIMAL TOUR PATH ==========
Tour Path : City 0 -> City 1 -> City 3 -> City 2 -> City 0

========== RESULTS & METHOD COMPARISON ==========
Method          | Min Tour Cost   | Execution Time (ns) 
-------------------------------------------------------
Held-Karp (DP)  | 80              | 36400.00            
Brute-Force     | 80              | 28900.00            
=======================================================
📖 Key Takeaways & Conclusion
Exponential Optimization:
The Held-Karp DP algorithm reduces TSP complexity from factorial time 
O
(
N
!
)
 to exponential time 
O
(
N
2
2
N
)
.
Practical Applicability:
Held-Karp makes exact TSP solutions feasible for up to 
N
≈
20
 cities, whereas Brute-Force stalls for 
N
≥
12
.
