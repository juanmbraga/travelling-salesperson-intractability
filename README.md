Practical Project 02 | DCC207 - Algorithms 2 | December 2023, Federal University of Minas Gerais

# The Travelling Salesperson Problem's intractability and approximations
This project aims to take a look at the real-world challenges of implementing solutions for `hard problems` such as the Travelling Salesperson Problem (TSP). This will be done by comparing the execution time, memory usage and solution quality between the optimal (but expensive) solution and two approximation algorithms.

## Implementation Objectives
- A slightly-better-than-brute-force solution using a **Branch and Bound** approach
- The **Twice Around the Tree** approximation algorithm
- The **Christofides** approximation algorithm
- A comparison of the performance (time and space) and accuracy of the algorithms

## What is the Travelling Salesperson Problem?
The TSP is a well-known `intractable problem`, which in the context of algorithms means that the time and/or space required to solve the problem grows exponentially with the size of the input, making it impractical for even relatively small inputs.

**Problem description:** *A salesperson needs to visit a set of cities to sell their goods. They know how many cities they need to go to and the distances between each city. In what order should the salesperson visit each city exactly once so that they minimize their travel time and so that they end their journey in their city of origin?* (from [Brilliant.org](https://brilliant.org/wiki/traveling-salesperson-problem/)) ([mirror](https://web.archive.org/web/20230926122114/https://brilliant.org/wiki/traveling-salesperson-problem/))

## Important files and execution instructions

- **`documentation.pdf✨`** is a report with all of the descriptions, choices, results and analysis.
- **`main.py`** is the main script that will run and collect the results for each algorithm.
- `results/` folder is where the results will be stored in `.csv` format.
- `dataset_recipe.txt` specifies which problem instances (datasets) should be run and in which order.

For the remaining folders, please refer to their respective *README* files.

### To run the project:
Make sure to have installed all of the packages specified in Section 3 of the documentation file. Then, simply run `main.py` with Python 3.
