import os
import csv
import time
import networkx as nx
from algorithms.twice_around_the_tree import solve as twice_around_the_tree
from algorithms.christofides import solve as christofides
from algorithms.branch_and_bound import solve as branch_and_bound
import preprocessor
from memory_profiler import memory_usage
from functools import partial


def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = round(end_time - start_time, 6)
    return result, execution_time

def measure_memory_usage(func, *args, **kwargs):
    mem_usage = memory_usage((func, args, kwargs))
    max_mem_usage = max(mem_usage)
    return max_mem_usage

def main():
    datasets = []
    datasets_file = 'dataset_schema.txt'
    statistics_file = 'statistics.csv'

    run_twice_around_the_tree = False 
    run_christofides = False
    run_branch_and_bound = False
    skip_problematic_memory_monitoring = True  # Set this to True if you want to skip memory usage for specific datasets
    problematic_datasets = ['rl5915', 'rl5934', 'rl11849', 'usa13509', 'brd14051', 'd15112', 'd18512']  # Add the names of the problematic datasets here

    with open(datasets_file, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            dataset_info = line.strip().split()
            datasets.append(dataset_info)

    with open(statistics_file, 'a', newline='') as file:  # Open the file in append mode
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Dataset Name', 'Number of Nodes', 'Algorithm', 'Total Distance', 'Execution Time', 'Memory Usage', 'Precision'])

        for dataset in datasets:
            dataset_name, num_nodes, optimal_solution = dataset
            graph = preprocessor.generate_graph(dataset_name)

            # Measure execution time and memory usage for each algorithm
            if run_twice_around_the_tree:
                (tt_shortest_path, tt_total_distance), tt_time = measure_execution_time(twice_around_the_tree, graph)
                if skip_problematic_memory_monitoring and dataset_name in problematic_datasets:
                    tt_memory = None
                else:
                    tt_memory = measure_memory_usage(twice_around_the_tree, graph)
                tt_precision = round(tt_total_distance / float(optimal_solution), 2)
                writer.writerow([dataset_name, num_nodes, 'Twice Around the Tree', tt_total_distance, tt_time, tt_memory, tt_precision])
                file.flush()  # Flush the buffer to update the file

            if run_christofides:
                (cf_shortest_path, cf_total_distance), cf_time = measure_execution_time(christofides, graph)
                if skip_problematic_memory_monitoring and dataset_name in problematic_datasets:
                    cf_memory = None
                else:
                    cf_memory = measure_memory_usage(christofides, graph)
                cf_precision = round(cf_total_distance / float(optimal_solution), 2)
                writer.writerow([dataset_name, num_nodes, 'Christofides', cf_total_distance, cf_time, cf_memory, cf_precision])
                file.flush()  # Flush the buffer to update the file

            if run_branch_and_bound:
                (bb_shortest_path, bb_total_distance), bb_time = measure_execution_time(branch_and_bound, graph)
                if skip_problematic_memory_monitoring and dataset_name in problematic_datasets:
                    bb_memory = None
                else:
                    bb_memory = measure_memory_usage(branch_and_bound, graph)
                bb_precision = round(bb_total_distance / float(optimal_solution), 2)
                writer.writerow([dataset_name, num_nodes, 'Branch and Bound', bb_total_distance, bb_time, bb_memory, bb_precision])
                file.flush()  # Flush the buffer to update the file

if __name__ == '__main__':
    main()

