Practical Project 02 | DCC207 - Algorithms 2 | December 2023, Federal University of Minas Gerais

# The Travelling Salesperson Problem's intractability and approximations
This project aims to take a look at the real-world challenges of implementing solutions for `hard problems` such as the Travelling Salesperson Problem (TSP). This will be done by comparing the execution time, memory usage and solution quality between the optimal (but expensive) solution and two approximation algorithms.

## Implementation Objectives
- A slightly-better-then-brute-force solution using a *Branch and Bound* approach
- A *Twice Around the Tree* approximation algorithm
- A *Christofides* approximation algorithm
- A comparison of the performance (time and space) and accuracy of the algorithms

## What is the Travelling Salesperson Problem?
The TSP is a well-known `intractable problem`, which in the context of algorithms means that the time and/or space required to solve the problem grows exponentially with the size of the input, making it impractical for even relatively small inputs.

[Brilliant.org](https://brilliant.org/wiki/traveling-salesperson-problem/) ([mirror](https://web.archive.org/web/20230926122114/https://brilliant.org/wiki/traveling-salesperson-problem/)) explains it as follows:

*A salesperson needs to visit a set of cities to sell their goods. They know how many cities they need to go to and the distances between each city. In what order should the salesperson visit each city exactly once so that they minimize their travel time and so that they end their journey in their city of origin?*

# File structure and execution instructions

**The files you should pay the most attention to are**:
- **`documentation.pdf`** is the article where all of the descriptions, choices, results and analysis can be found.
- **`main.py`** is the main file that will run all of the algorithms and generate the results.

The remaining files and folders are implementation-specific:
- `algorithms/` folder is where the Python implementation of each algorithm can be found.
- `datasets/` folder is where the datasets, as `.tsp` files, are located.
- `documentation/` foldere is where the *LateX* files and images for the documentation are stored.
- `statistics/` is the folder where the results will be stored in `.csv` format.
- **`dataset_recipe.txt`** is the file that specifies the datasets that will be used and in which order.


### To run the project
Make sure to have installed all of the packages specified in Section 3 of the documentation file. Then, simply run `main.py` with Python 3.

---
**Students:**
[Juan Braga](https://github.com/juanmbraga)
