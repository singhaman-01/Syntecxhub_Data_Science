"""
Project 1: NumPy Data Explorer
Author: Data Science Intern
Description: End-to-end demonstration of numerical computing, multi-dimensional array operations,
             broadcasting, file I/O operations, and computational performance benchmarking using NumPy.
"""

import time
import numpy as np


def explore_array_operations():
    print("=" * 60)
    print(" 1. ARRAY CREATION, INDEXING & SLICING ")
    print("=" * 60)

    # 1D & 2D Array Instantiation
    vector_1d = np.array([10, 20, 30, 40, 50])
    matrix_2d = np.arange(1, 10).reshape(3, 3)

    print(f"1D Vector:\n{vector_1d}\n")
    print(f"3x3 Matrix:\n{matrix_2d}\n")

    # Slicing: Sub-matrix extraction (Rows 0-1, Columns 1-2)
    sub_matrix = matrix_2d[:2, 1:]
    print(f"Extracted Sub-matrix (Rows 0-1, Cols 1-2):\n{sub_matrix}\n")


def compute_statistics():
    print("=" * 60)
    print(" 2. STATISTICAL & AXIS-WISE COMPUTATIONS ")
    print("=" * 60)

    matrix = np.arange(1, 10).reshape(3, 3)

    print(f"Overall Mean: {np.mean(matrix):.2f}")
    print(f"Column-wise Sums (axis=0): {np.sum(matrix, axis=0)}")
    print(f"Row-wise Sums (axis=1): {np.sum(matrix, axis=1)}")
    print(f"Standard Deviation: {np.std(matrix):.2f}\n")


def demonstrate_broadcasting_and_io():
    print("=" * 60)
    print(" 3. RESHAPING, BROADCASTING & PERSISTENCE ")
    print("=" * 60)

    matrix = np.arange(1, 10).reshape(3, 3)
    offsets = np.array([100, 200, 300])

    # Broadcasting row vector across 2D matrix
    broadcasted_result = matrix + offsets
    print(f"Broadcasting Result (Matrix + Row Vector):\n{broadcasted_result}\n")

    # Persistent Storage
    file_path = "array_data.npy"
    np.save(file_path, broadcasted_result)
    loaded_data = np.load(file_path)
    print(
        f"Successfully saved and reloaded array from '{file_path}'. Matrix Shape: {loaded_data.shape}\n"
    )


def benchmark_performance():
    print("=" * 60)
    print(" 4. PERFORMANCE BENCHMARK: NUMPY VS PYTHON LIST ")
    print("=" * 60)

    element_count = 1_000_000
    py_list = list(range(element_count))
    np_array = np.arange(element_count)

    # Python Native List Benchmark
    start_time = time.time()
    _ = [val * 2 for val in py_list]
    py_duration = time.time() - start_time

    # NumPy Vectorized Operations Benchmark
    start_time = time.time()
    _ = np_array * 2
    np_duration = time.time() - start_time

    speedup = py_duration / np_duration if np_duration > 0 else 0

    print(f"Native Python List Execution Time : {py_duration:.5f} seconds")
    print(f"NumPy Vectorized Array Time       : {np_duration:.5f} seconds")
    print(
        f"--> NumPy Performance Advantage   : {speedup:.2f}x faster execution\n"
    )


if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("# SYNTECXHUB DATA SCIENCE INTERNSHIP - PROJECT 1")
    print("#" * 60 + "\n")

    explore_array_operations()
    compute_statistics()
    demonstrate_broadcasting_and_io()
    benchmark_performance()