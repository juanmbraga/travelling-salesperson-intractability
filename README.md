Practical Project 02 | DCC027 - Algorithms 2 | December 2023, Federal UNiversity of Minas GErais

# The Travelling Salesperson Problem's intractability and approximations
This project aims to take a look at the real-world challenges of implementing solutions for a `hard problem` such as the Travelling Salesperson Problem (TSP). This will be done by implementing an optimal (but expensive) solution and comparing it to two approximation algorithms.

## Implementation Objectives
- A slightly-better-then-brute-force solution using a branch-and-bound algorithm
- A Twice-around-the-tree approximation algorithm
- A Christofides approximation algorithm
- A comparison of the performance (time and space) and accuracy of the algorithms

## What is the Travelling Salesperson Problem?
The TSP is a well-known `intractable problem`, which in the context of algorithms means that the time and/or space required to solve the problem grows exponentially with the size of the input, making it impractical to solve for large inputs.

[Brilliant.org](https://brilliant.org/wiki/traveling-salesperson-problem/) ([mirror](https://web.archive.org/web/20230926122114/https://brilliant.org/wiki/traveling-salesperson-problem/)) explains it as follows:

*A salesperson needs to visit a set of cities to sell their goods. They know how many cities they need to go to and the distances between each city. In what order should the salesperson visit each city exactly once so that they minimize their travel time and so that they end their journey in their city of origin?*

---
**Students:**
[Juan Braga](https://github.com/juanmbraga)
